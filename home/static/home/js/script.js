try{
    document.getElementById("button-open-menu").addEventListener("click", () => {
        document.getElementById("button-open-menu").style.display = "none";
        document.getElementById("menu-mobile").style.display = "block";
        document.getElementById("menu-mobile").style.width = "100%";
        document.getElementById("main_container").style.display = "none";
    })
}catch{alert("error")}
document.getElementById("close-mobile-menu").addEventListener("click", () => {
    document.getElementById("menu-mobile").style.width = "0vh";
    document.getElementById("main_container").style.display = "flex";
    document.getElementById("button-open-menu").style.display = "flex";
})

try{
    document.getElementById("move-scroll-right").addEventListener("click", () => {
        let scroll = document.getElementById("cards-container");
        if (scroll.scrollWidth > scroll.scrollLeft + scroll.clientWidth) {
            document.getElementById("cards-container").scrollTo(scroll.scrollLeft + 800, 0);
        }
        else{
            document.getElementById("cards-container").scrollTo(scrollWidth - 800);
        }
    })
}catch{}

try{
    document.getElementById("move-scroll-left").addEventListener("click", () => {
        let scroll = document.getElementById("cards-container");
        if (scroll.scrollLeft > 0) {
            document.getElementById("cards-container").scrollLeft -= 800;
        }
        else{
            document.getElementById("cards-container").scrollLeft = 0;
        }
    })
}catch{}

