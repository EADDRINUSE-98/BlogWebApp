const textArray = [
  "&xlarr; Pick your poison!",
  "Continue where you left off.",
  "Put your thoughts on pixels.",
  "Typing a day keeps the mediocrity at bay.",
  "Gaining knowledge is good, but sharing it is even better."
]
let indx = 0

const p = document.getElementById("rotating_text");

const updateText = () => {
  p.style.transform = "translateY(-20px)";
  p.style.opacity = 0;

  setTimeout(() => {
    p.innerHTML = textArray[indx];
    p.style.transform = "translateY(0)";
    p.style.opacity = 1;
    indx = (indx + 1) % textArray.length;
  }, 500);

  setTimeout(() => {
    p.style.transform = "translateY(20px)";
    p.style.opacity = 0;
  }, 4000);
}

updateText();

setInterval(updateText, 5000);
