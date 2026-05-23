const deleteBtn = document.getElementById("delete-btn");
const divModalContainer = document.getElementById("modal-container");
const modalCancelBtn = document.getElementById("modal-cancel-btn");

deleteBtn.addEventListener("click", () => {
  divModalContainer.toggleAttribute("hidden");
});
