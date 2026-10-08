// Mostra só os blocos cujo data-estado lista o estado de ?estado= (padrão: "padrao").
// ?tema=escuro põe data-theme="escuro" no <html>; sem o parâmetro vale o tema claro de :root.
const params = new URLSearchParams(location.search);
const estado = params.get("estado") || "padrao";
if (params.get("tema") === "escuro") document.documentElement.dataset.theme = "escuro";
document.querySelectorAll("[data-estado]").forEach(el => { if (el.dataset.estado.split(" ").includes(estado)) el.removeAttribute("data-estado"); });
