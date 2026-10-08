// Mostra só os blocos cujo data-estado lista o estado de ?estado= (padrão: "padrao").
const estado = new URLSearchParams(location.search).get("estado") || "padrao";
document.querySelectorAll("[data-estado]").forEach(el => { if (el.dataset.estado.split(" ").includes(estado)) el.removeAttribute("data-estado"); });
