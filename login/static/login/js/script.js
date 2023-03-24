document.querySelector(".switch-signin").addEventListener("click", () => {
    let signin = document.getElementById("signin");
    let create = document.getElementById("create-account");
    let welcome = document.getElementById("welcome-back");
    let hello = document.getElementById("hello");

    signin.classList.toggle("move2");
    signin.classList.toggle("show");
    create.classList.toggle("move2");
    create.classList.toggle("hidden");
    create.classList.toggle("show");
    signin.classList.toggle("hidden");
    welcome.classList.toggle("move1");
    welcome.classList.toggle("hidden");
    welcome.classList.toggle("show");
    hello.classList.toggle("move1");
    hello.classList.toggle("show");
    hello.classList.toggle("hidden");
    console.log(hello + " " + welcome);
});
document.querySelector(".switch-signup").addEventListener("click", () => {
    let signin = document.getElementById("signin");
    let create = document.getElementById("create-account");
    let welcome = document.getElementById("welcome-back");
    let hello = document.getElementById("hello");

    create.classList.toggle("move2");
    create.classList.toggle("hidden");
    signin.classList.toggle("move2");
    signin.classList.toggle("show");
    signin.classList.toggle("hidden");
    create.classList.toggle("show");
    welcome.classList.toggle("move1");
    welcome.classList.toggle("hidden");
    welcome.classList.toggle("show");
    hello.classList.toggle("move1");
    hello.classList.toggle("show");
    hello.classList.toggle("hidden");

});