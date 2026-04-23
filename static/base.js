const toggleButton = document.querySelectorAll("#theme-btn");
const bodyElement = document.querySelector("body");

toggleButton.forEach((btn) => {
  btn.addEventListener("click", () => {
    bodyElement.classList.toggle("lightmode");
  });
});
