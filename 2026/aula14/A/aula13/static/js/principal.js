const titulo = document.querySelector("#titulo");   
titulo.addEventListener("click", function() {
    if(!titulo.textContent.startsWith("Bem vindo - ")) {
        titulo.textContent = "Bem vindo - " + titulo.textContent;
    }
});

const inputLogin = document.querySelector("#login");
const inputSenha = document.querySelector("#senha");
const mensagem = document.querySelector("#mensagem");
inputLogin.addEventListener("input", function() {
    console.log("Valor do input de login: " + inputLogin.value);
    mensagem.textContent = "Você digitou: " + inputLogin.value;
});
const formulario = document.querySelector("#form");
formulario.addEventListener("submit", function(e) {
    const inputs = document.querySelectorAll("input");
    for (let i = 0; i < inputs.length; i++) {
        if(inputs[i].value.trim() === "") {
            mensagem.textContent = "Campos obrigatórios não preenchidos!";
            e.preventDefault();
            return;
        }
    }
});
