const API = "/exercicios/";

async function listarExercicios() {
  const resposta = await fetch(API);
  const exercicios = await resposta.json();

  const lista = document.getElementById("lista-exercicios");
  lista.innerHTML = "";

  for (const ex of exercicios) {
    const item = document.createElement("li");

    const nome = document.createElement("strong");
    nome.textContent = ex.nome;

    const tag = document.createElement("span");
    tag.className = "tag";
    tag.textContent = ex.grupo_muscular;

    item.append(nome, tag);
    lista.appendChild(item);
  }
}

// DESAFIO: enviar o formulário como POST para a API
document.getElementById("form-exercicio").addEventListener("submit", async (evento) => {
  evento.preventDefault(); // impede a página de recarregar

  // 1. pegar os valores dos inputs #nome e #grupo
  // 2. fetch(API, { method: "POST", headers: ..., body: JSON.stringify(...) })
  //    dica: o body precisa ter o mesmo formato do ExercicioCreate do Swagger
  // 3. limpar o formulário e chamar listarExercicios() de novo
});

listarExercicios();