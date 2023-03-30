let init = () => {
    let container = document.querySelector('.container');
    let tela = document.querySelector('html');

    if (tela.offsetWidth > 900) {
        container.innerHTML = `
        <section class="section create-account" id="create-account">
        <h1>Crie uma Conta</h1>
        <form>
        <input required type="text" name="nome" id="nome-cadastro" class="nome-input" placeholder="Seu nome">
        <input required type="email" name="email" id="email-cadastro" class="email-input" placeholder="Seu email">
        <input required type="password" name="senha" id="senha-cadastro" class="senha-input" placeholder="Sua senha">
        <button class="confirm-button">Cadastrar</button>
        </form>
        <div class="div-ou">
            <div class="horizontal-line"></div>
            <p>ou</p>
            <div class="horizontal-line"></div>
        </div>
        <div class="icons">
            <i class="fab fa-facebook-f icon"></i>
            <i class="fab fa-google-plus-g icon"></i>
            <i class="fab fa-linkedin-in icon"></i>
        </div>
        </section>
        <section class="section signin" id="signin">
            <h1>Entrar</h1>
            <form>
            <input required type="email" name="email" id="email-login" class="email-input" placeholder="Seu email">
            <input required type="password" name="senha" id="senha-login" class="senha-input" placeholder="Sua senha">
            <button class="confirm-button">Confirmar</button>
            </form>
            <div class="div-ou">
                <div class="horizontal-line"></div>
                <p>ou</p>
                <div class="horizontal-line"></div>
            </div>
            <div class="icons">
                <i class="fab fa-facebook-f icon"></i>
                <i class="fab fa-google-plus-g icon"></i>
                <i class="fab fa-linkedin-in icon"></i>
            </div>
        </section>
        <section class="section welcome-back back-red" id="welcome-back">
            <div class="section-logo">
                <i class="fas fa-book"></i>
                <h3>INFO UFPI</h3>
            </div>
            <h1>Olá, Estudante!</h1>
            <p>Já possui uma conta?</p>
            <button class="switch-signin">Sign In</button>
        </section>
        <section class="section hello back-red" id="hello">
            <div class="section-logo">
                <i class="fas fa-book"></i>
                <h3>INFO UFPI</h3>
            </div>
            <h1>Olá, Estudante!</h1>
            <p>Ainda não possui uma conta?</p>
            <button class="switch-signup">Sign Up</button>
        </section>
        
        `
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
    } else {
        container.innerHTML = `
        <section class="section signin active" id="signin">
        <h1>Entrar</h1>
        <form>
            <input required type="email" name="email" id="email-login" class="email-input" placeholder="Seu email">
            <input required type="password" name="senha" id="senha-login" class="senha-input"
                placeholder="Sua senha">
            <button class="confirm-button">Confirmar</button>
        </form>
        <div class="div-ou">
            <div class="horizontal-line"></div>
            <p>ou</p>
            <div class="horizontal-line"></div>
        </div>
        <div class="icons">
            <i class="fab fa-facebook-f icon"></i>
            <i class="fab fa-google-plus-g icon"></i>
            <i class="fab fa-linkedin-in icon"></i>
        </div>
        <p class="p-cadastrar">
            Não tem uma conta?
            <button class="move-to-creator">Cadastre-se</button>
        </p>
    </section>
    <section class="section create-account hidden" id="create-account">
        <h1>Crie uma Conta</h1>
        <form>
            <input required type="text" name="nome" id="nome-cadastro" class="nome-input" placeholder="Seu nome">
            <input required type="email" name="email" id="email-cadastro" class="email-input"
                placeholder="Seu email">
            <input required type="password" name="senha" id="senha-cadastro" class="senha-input"
                placeholder="Sua senha">
            <button class="confirm-button">Cadastrar</button>
        </form>
        <div class="div-ou">
            <div class="horizontal-line"></div>
            <p>ou</p>
            <div class="horizontal-line"></div>
        </div>
        <div class="icons">
            <i class="fab fa-facebook-f icon"></i>
            <i class="fab fa-google-plus-g icon"></i>
            <i class="fab fa-linkedin-in icon"></i>
        </div>
        <p class="p-cadastrar">Já tem uma conta?<button class="move-to-signin">Entrar</button></p>
    </section>
        `
        document.querySelector(".move-to-creator").addEventListener("click", () => {
            let signin = document.querySelector(".signin");
            let create = document.querySelector(".create-account");
            signin.style.animation = "fecha .5s ease-in-out";
            signin.classList.toggle("hidden");
            signin.classList.toggle("active");
            create.style.animation = "abre .5s ease-in-out";
            create.classList.toggle("active");
            create.classList.toggle("hidden");
        });
        document.querySelector(".move-to-signin").addEventListener("click", () => {
            let signin = document.querySelector(".signin");
            let create = document.querySelector(".create-account");
            signin.style.animation = "abre .5s ease-in-out";
            signin.classList.toggle("hidden");
            signin.classList.toggle("active");
            create.style.animation = "fecha .5s ease-in-out";
            create.classList.toggle("active");
            create.classList.toggle("hidden");
        });
    }
}

init();


window.onresize = init;