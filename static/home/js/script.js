document.querySelectorAll(".card-noticia").forEach((elem) => {
    elem.addEventListener("click", () => {
        window.location.href = `/noticias/${elem.querySelector(".notice-slug").value}/`
    });
})