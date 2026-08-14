const createBtn = document.getElementById("crte_btn");
const createForm = document.getElementById("create_form");
const overlay = document.getElementsByClassName("overlay")[0];

createBtn.addEventListener("click", () => {
  if (!overlay.style.display || overlay.style.display === "none") {
    overlay.style.display = "flex";
  } else {
    overlay.style.display = "none";
  }
});

const removeOverlay = () => {
  overlay.style.display = "none";
};
overlay.addEventListener("click", removeOverlay);

modalNoBtn.addEventListener("click", removeOverlay);
