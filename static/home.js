const tabButtons = document.querySelectorAll("button[role='tab']");
const panelElements = document.querySelectorAll("div[role='tabpanel']");
let activeIndex = 0;

tabButtons.forEach((tab, index) => {
  tab.addEventListener("click", () => {
    setActiveTab(index);
  });
});

const setActiveTab = (index) => {
  tabButtons[activeIndex].setAttribute("aria-selected", "false");
  tabButtons[index].setAttribute("aria-selected", "true");
  setActivePanel(index);
  activeIndex = index;
};

const setActivePanel = (index) => {
  panelElements[activeIndex].setAttribute("hidden", "");
  panelElements[index].removeAttribute("hidden");
};
