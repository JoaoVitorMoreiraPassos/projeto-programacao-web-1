if (!localStorage.getItem("cookiesAccepted")) {
    let cookieMessage = document.getElementById('cookie-notification');
    let closeCookie = document.getElementById('cookie-notification-close');

    cookieMessage.style.display = 'block';
    closeCookie.addEventListener("click", function (e) {
        e.preventDefault();
        localStorage.setItem("cookiesAccepted", true);
        cookieMessage.style.display = 'none';
    });
}

try {
    document.getElementById("button-open-menu").addEventListener("click", () => {
        document.getElementById("button-open-menu").style.display = "none";
        document.getElementById("menu-mobile").style.display = "block";
        document.getElementById("menu-mobile").style.width = "100%";
        document.getElementById("main_container").style.display = "none";
    })
} catch { console.log("error") }
document.getElementById("close-mobile-menu").addEventListener("click", () => {
    document.getElementById("menu-mobile").style.width = "0vh";
    document.getElementById("main_container").style.display = "flex";
    document.getElementById("button-open-menu").style.display = "flex";
})

try {
    document.getElementById("move-scroll-right").addEventListener("click", () => {
        let btn = document.getElementById("move-scroll-right");
        if (btn.classList.contains("move-disabled")) {
            return
        }
        let scroll = document.getElementById("cards-container");
        if (scroll.scrollWidth > scroll.scrollLeft + scroll.clientWidth) {
            document.getElementById("cards-container").scrollTo(scroll.scrollLeft + 800, 0);
        } else {
            document.getElementById("cards-container").scrollTo(() => {
                return scroll.scrollWidth - 800;
            });
        }
    })
} catch { console.log("error") }

try {
    document.getElementById("move-scroll-left").addEventListener("click", () => {
        let btn = document.getElementById("move-scroll-left");
        if (btn.classList.contains("move-disabled")) {
            return
        }
        let scroll = document.getElementById("cards-container");
        if (scroll.scrollLeft > 800) {
            document.getElementById("cards-container").scrollLeft -= 800;
        } else {
            document.getElementById("cards-container").scrollLeft = 0;
        }
    })
} catch { console.log("error") }

try {
    document.getElementById("cards-container").addEventListener("scroll", () => {
        let scroll = document.getElementById("cards-container");
        if (scroll.scrollWidth > scroll.scrollLeft + scroll.clientWidth + 10) {
            document.getElementById("move-scroll-right").classList.remove("move-disabled");
        } else {
            document.getElementById("move-scroll-right").classList.add("move-disabled");
        }
        if (scroll.scrollLeft > 0) {
            document.getElementById("move-scroll-left").classList.remove("move-disabled");
        } else {
            document.getElementById("move-scroll-left").classList.add("move-disabled");
        }
    })
} catch { console.log("error") }


document.querySelector(".nav-home").addEventListener("mousemove", () => {
    document.querySelector(".nav-NAE").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-NAE").style.border = "none";
    document.querySelector(".nav-contato").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-sobre").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-sobre").style.border = "none";

    document.querySelector(".nav-home").style.backgroundColor = "#276c65";
    document.querySelector(".nav-home").style.borderRadius = "1rem";
    document.querySelector(".nav-home").style.borderRight = "1.5px solid #fff";
})

document.querySelector(".nav-home").addEventListener("mouseout", () => {
    document.querySelector(".nav-home").style = "";
    document.querySelector(".nav-NAE").style = "";
    document.querySelector(".nav-contato").style = "";
    document.querySelector(".nav-sobre").style = "";
})

document.querySelector(".nav-NAE").addEventListener("mousemove", () => {
    document.querySelector(".nav-home").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-home").style.border = "none";
    document.querySelector(".nav-contato").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-sobre").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-sobre").style.border = "none";

    document.querySelector(".nav-NAE").style.backgroundColor = "#276c65";
    document.querySelector(".nav-NAE").style.borderRadius = "1rem";
    document.querySelector(".nav-NAE").style.borderRight = "1.5px solid #fff";
})

document.querySelector(".nav-NAE").addEventListener("mouseout", () => {
    document.querySelector(".nav-home").style = "";
    document.querySelector(".nav-NAE").style = "";
    document.querySelector(".nav-contato").style = "";
    document.querySelector(".nav-sobre").style = "";
})

document.querySelector(".nav-contato").addEventListener("mousemove", () => {
    document.querySelector(".nav-home").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-home").style.border = "none";
    document.querySelector(".nav-NAE").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-NAE").style.border = "none";
    document.querySelector(".nav-sobre").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-sobre").style.border = "none";

    document.querySelector(".nav-contato").style.backgroundColor = "#276c65";
    document.querySelector(".nav-contato").style.borderRadius = "1rem";
    document.querySelector(".nav-contato").style.borderRight = "1.5px solid #fff";
})

document.querySelector(".nav-contato").addEventListener("mouseout", () => {
    document.querySelector(".nav-home").style = "";
    document.querySelector(".nav-NAE").style = "";
    document.querySelector(".nav-contato").style = "";
    document.querySelector(".nav-sobre").style = "";
})

document.querySelector(".nav-sobre").addEventListener("mousemove", () => {
    document.querySelector(".nav-home").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-home").style.border = "none";
    document.querySelector(".nav-NAE").style.backgroundColor = "#1693a5";
    document.querySelector(".nav-NAE").style.border = "none";
    document.querySelector(".nav-contato").style.backgroundColor = "#1693a5";

    document.querySelector(".nav-sobre").style.backgroundColor = "#276c65";
    document.querySelector(".nav-sobre").style.borderRadius = "1rem";
    document.querySelector(".nav-sobre").style.borderRight = "1.5px solid #fff";
})

document.querySelector(".nav-sobre").addEventListener("mouseout", () => {
    document.querySelector(".nav-home").style = "";
    document.querySelector(".nav-NAE").style = "";
    document.querySelector(".nav-contato").style = "";
    document.querySelector(".nav-sobre").style = "";
})