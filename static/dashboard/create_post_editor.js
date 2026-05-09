// import EasyMDE from "https://esm.sh/easymde";
//
// const editor = new EasyMDE({ "element": document.getElementById("content_input") });
window.addEventListener("DOMContentLoaded", () => {

  const textarea = document.getElementById("content_input");

  const editor = new EasyMDE({
    element: textarea,
  });

});
