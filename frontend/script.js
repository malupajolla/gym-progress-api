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

document.getElementById("form-exercicio").addEventListener("submit", async (evento) => {
  evento.preventDefault(); 

 document.getElementById("form-exercicio").addEventListener("submit", async (evento) => {
  evento.preventDefault(); 

  
  const nome = document.getElementById("nome").value;
  const grupo = document.getElementById("grupo").value;

  
  const resposta = await fetch(API, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      nome: nome,
      grupo_muscular: grupo
    })
  });

 
  evento.target.reset();
  listarExercicios();
});
});

listarExercicios();