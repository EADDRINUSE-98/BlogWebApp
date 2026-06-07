// import EasyMDE from "https://esm.sh/easymde";
//
// const editor = new EasyMDE({ "element": document.getElementById("content_input") });
const csrfToken = document.cookie.split("=")[1]
window.addEventListener("DOMContentLoaded", () => {

  const textarea = document.getElementById("content_input");

  const editor = new EasyMDE({
    element: textarea,
    toolbar: ["bold", "italic", "heading", "|", "quote", "unorderer-list", "ordered-list", "check-list", "|", "link", "upload-image", "|", "preview", "side-by-side", "fullscreen", "|", "guide", "|"],
    uploadImage: true,
    imageUploadFunction: function imageUpload(imgfile, onSuccess, onError) {
      const form = new FormData();
      form.append("image", imgfile);
      fetch("/dashboard/upload_image/", {
        method: "POST",
        body: form,
        headers: { "X-CSRFToken": csrfToken, },
      }).then(response => response.json()).then(data => onSuccess(data.url)).catch(error => onError(error));
    },
  });
});

