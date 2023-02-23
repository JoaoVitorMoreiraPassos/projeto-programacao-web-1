try {
    document.getElementById("button-open-menu").addEventListener("click", () => {
        document.getElementById("button-open-menu").style.display = "none";
        document.getElementById("menu-mobile").style.display = "block";
        document.getElementById("menu-mobile").style.width = "100%";
        document.getElementById("main_container").style.display = "none";
    })
} catch { alert("error") }
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
} catch { }

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
} catch { }

try {
    document.getElementById("cards-container").addEventListener("scroll", () => {
        let scroll = document.getElementById("cards-container");
        console.log(scroll.scrollWidth, scroll.scrollLeft, scroll.clientWidth);
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
} catch { }