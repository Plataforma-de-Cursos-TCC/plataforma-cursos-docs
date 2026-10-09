// Mostra só os blocos cujo data-estado lista o estado de ?estado= (padrão: "padrao").
// ?tema=claro|escuro põe data-theme no <html> e marca a opção correspondente do seletor de tema;
// sem o parâmetro vale o tema do sistema (prefers-color-scheme, ver _base.css).
const params = new URLSearchParams(location.search);
const estado = params.get("estado") || "padrao";
const tema = params.get("tema");
if (tema === "claro" || tema === "escuro") {
  document.documentElement.dataset.theme = tema;
  const opcao = document.querySelector(`input[name="tema"][value="${tema}"]`);
  if (opcao) opcao.checked = true;
}
document.querySelectorAll("[data-estado]").forEach(el => { if (el.dataset.estado.split(" ").includes(estado)) el.removeAttribute("data-estado"); });
// Pré-visualização da foto: o arquivo escolhido vira o fundo do círculo indicado em data-preview.
document.querySelectorAll('input[type="file"][data-preview]').forEach(entrada => entrada.addEventListener("change", () => {
  const arquivo = entrada.files[0];
  if (arquivo) document.getElementById(entrada.dataset.preview).style.backgroundImage = `url("${URL.createObjectURL(arquivo)}")`;
}));
