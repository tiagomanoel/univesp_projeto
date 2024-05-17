const menuIcon = document.querySelector("#menuIcon");
const closeMenu = document.querySelector("#closeMenu");
const menuMobile = document.querySelector("#menuMobile");

menuIcon.addEventListener("click", function () {
    menuMobile.classList.add("flex");
});


closeMenu.addEventListener("click", function (){
    menuMobile.classList.remove("flex");
});








