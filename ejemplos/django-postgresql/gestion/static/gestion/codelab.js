"use strict";
const sections = [...document.querySelectorAll("[data-step]")];
const boxes = [...document.querySelectorAll("[data-criterion]")];
let busy = false;
const labels = {aprobado:"Aprobado",fallo:"Fallo: revisa la regla y ejecuta las pruebas en terminal",error_entorno:"Error del entorno: revisa conexión, migraciones y dependencias",anterior:"Resultado anterior: vuelve a comprobar",pendiente:"Pendiente: todavía no comprobado"};
function showStep(focus=false){
  const active = sections.find(s=>"#"+s.id===location.hash) || sections[0];
  sections.forEach(s=>s.hidden=s!==active);
  document.querySelectorAll("nav a").forEach(a=>{if(a.hash==="#"+active.id)a.setAttribute("aria-current","step");else a.removeAttribute("aria-current");});
  if(focus) active.focus();
}
showStep();window.addEventListener("hashchange",()=>showStep(true));
function render(box,result){
  const state = result?.estado || "pendiente";
  box.dataset.state=state;
  box.querySelector(".result").textContent=(labels[state]||state)+(result?.mensaje?". "+result.mensaje:"");
  box.querySelector(".evidence").textContent=result?JSON.stringify(result,null,2):"Sin evidencia.";
  box.querySelector(".download").disabled=!result;
  box.proof=result;
}
function unavailable(message){boxes.forEach(b=>render(b,{estado:"error_entorno",mensaje:message}));}
async function refresh(){
  if(busy)return;
  try{
    const response=await fetch("estado/",{cache:"no-store",headers:{Accept:"application/json"}});
    if(!response.ok||response.redirected)throw Error();
    const data=await response.json();
    if(data.estado==="error_entorno"){unavailable(data.mensaje);return;}
    boxes.forEach(b=>render(b,data.resultados[b.dataset.criterion]));
    document.querySelector("#connection").textContent="Vigencia consultada: "+new Date().toLocaleTimeString()+". Se vuelve a consultar cada 5 segundos.";
  }catch{unavailable("No se puede confirmar vigencia. Reabre la página para renovar sesión o revisa el servidor.");}
}
boxes.forEach(box=>{
  box.querySelector(".check").addEventListener("click",async()=>{
    if(busy)return;busy=true;boxes.forEach(b=>{b.querySelector(".check").disabled=true;if(b.proof)render(b,{...b.proof,estado:"anterior"});});
    box.dataset.state="comprobando";box.querySelector(".result").textContent="Comprobando: ejecutando el criterio real…";
    box.proof=null;box.querySelector(".download").disabled=true;box.querySelector(".evidence").textContent="Comprobación en curso.";
    try{
      const response=await fetch("comprobar/"+box.dataset.criterion+"/",{method:"POST",headers:{"X-CSRFToken":document.querySelector("[name=csrfmiddlewaretoken]").value,Accept:"application/json"},signal:AbortSignal.timeout(110000)});
      if(!response.ok||response.redirected)throw Error();
      render(box,await response.json());
    }catch{render(box,{estado:"error_entorno",mensaje:"Sin resultado confirmable. Si hubo 403, recarga como GET; si persiste, revisa CSRF sin desactivarlo. El proceso puede seguir hasta su timeout técnico."});}
    finally{busy=false;boxes.forEach(b=>b.querySelector(".check").disabled=false);}
  });
  box.querySelector(".download").addEventListener("click",()=>{if(!box.proof)return;const url=URL.createObjectURL(new Blob([JSON.stringify(box.proof,null,2)],{type:"application/json"}));const a=document.createElement("a");a.href=url;a.download="pp4-"+box.dataset.criterion+".json";a.click();URL.revokeObjectURL(url);});
});
document.querySelectorAll(".copy").forEach(button=>button.addEventListener("click",async()=>{try{await navigator.clipboard.writeText(button.parentElement.querySelector("code").textContent);button.textContent="Copiado";}catch{button.textContent="Selecciona y copia el texto";}}));
refresh();setInterval(refresh,5000);document.addEventListener("visibilitychange",()=>{if(!document.hidden)refresh();});
