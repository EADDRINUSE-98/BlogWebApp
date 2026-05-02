const toggleButton = document.querySelectorAll("#theme-btn");
const bodyElement = document.querySelector("body");

const savedTheme = localStorage.getItem("theme");
if (savedTheme === "light") {
  bodyElement.classList.add("lightmode");
}

toggleButton.forEach((btn) => {
  btn.addEventListener("click", () => {
    bodyElement.classList.toggle("lightmode");
    let currentTheme = bodyElement.classList.contains("lightmode") ? "light" : "dark";
    localStorage.setItem("theme", currentTheme);
  });
});
