// import EasyMDE from "https://esm.sh/easymde";
//
// const editor = new EasyMDE({ "element": document.getElementById("content_input") });
window.addEventListener("DOMContentLoaded", () => {

  const textarea = document.getElementById("content_input");

  const editor = new EasyMDE({
    element: textarea,
    uploadImage: true,
    imageUploadFunction: function imageUpload(imgfile, onSuccess, onError) {
      const form = new FormData();
      form.append("image", imgfile);
      fetch("/dashboard/upload_image/", {
        method: "POST",
        body: form,
        headers: { "X-CSRFToken": csrfToken, },
      }).then(response => response.json()).then(data => onSuccess(data)).catch(error => onError(error));
    },
  });
});

