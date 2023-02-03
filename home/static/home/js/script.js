document.getElementById("move-scroll-right").addEventListener("click", () => {
    let scroll = document.getElementById("cards-container");
    if (scroll.scrollWidth > scroll.scrollLeft + scroll.clientWidth) {
        document.getElementById("cards-container").scrollTo(scroll.scrollLeft + 800, 0);
        // document.getElementById("cards-container").scrollLeft += 500;
    }
    else{
        document.getElementById("cards-container").scrollTo(scrollWidth - 800);
    }
})

document.getElementById("move-scroll-left").addEventListener("click", () => {
    let scroll = document.getElementById("cards-container");
    if (scroll.scrollLeft > 0) {
        document.getElementById("cards-container").scrollLeft -= 800;
    }
    else{
        document.getElementById("cards-container").scrollLeft = 0;
    }
})