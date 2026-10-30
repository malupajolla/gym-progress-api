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
  evento.preventDefault(); // impede a página de recarregar

   
  const nome = document.getElementById("???").value;
  const grupo = ???;

  
  const resposta = await fetch(API, {
    method: "???",
    headers: { "Content-Type": "???" },
    body: JSON.stringify({
      nome: nome,
      grupo_muscular: ???
    })
  });


  evento.target.reset();
  ???
});

listarExercicios();