window.addEventListener("DOMContentLoaded", () => {
  const links = document.querySelectorAll("a");
  let clickedLink = null;

  links.forEach((link) => {
    link.addEventListener("click", () => {
      if (clickedLink) {
        clickedLink.classList.remove("clicked");
      }
      link.classList.add("clicked");
      clickedLink = link;
    });
  });
});
