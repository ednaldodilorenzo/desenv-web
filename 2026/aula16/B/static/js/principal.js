let titulo = document.querySelector("#tituloPagina");
titulo.addEventListener("click", function() {
    titulo.textContent = "Bem-vindo ao sistema - " + titulo.textContent;
});

let mensagem = document.querySelector("#mensagem");
let inputLogin = document.querySelector("#login");
inputLogin.addEventListener("input", function() {
    mensagem.textContent = "Você digitou: " + inputLogin.value;
})
let inputSenha = document.querySelector("#senha");
let formulario = document.querySelector("#form");
formulario.addEventListener("submit", function(e) {

    if (inputLogin.value.trim() === "" || inputSenha.value.trim() === "") {
        mensagem.textContent = "Campos obrigatórios não preenchidos!";
        e.preventDefault();
    }
});

