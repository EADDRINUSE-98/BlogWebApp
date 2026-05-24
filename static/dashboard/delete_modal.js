const deleteBtn = document.getElementById("delete-btn");
const modalNoBtn = document.getElementById("modal-cancel-btn");
const modalYesBtn = document.getElementById("modal-delete-btn");
const overlay = document.getElementsByClassName("overlay")[0];


deleteBtn.addEventListener("click", () => {
  if (!overlay.style.display || overlay.style.display === "none") {
    overlay.style.display = "flex";
  }
  else {
    overlay.style.display = "none";
  }
});

const removeOverlay = () => {
  overlay.style.display = "none";
}
overlay.addEventListener("click", removeOverlay);

modalNoBtn.addEventListener("click", removeOverlay);
// inspiration: https://www.tutorialspoint.com/article/how-to-create-an-overlay-effect-with-css
