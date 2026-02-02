const body = document.querySelector("body");
const h2 = document.querySelector("h2");
const btn = document.querySelector("button");

function colorns() {
  return Math.floor(Math.random() * 256);
}

btn.addEventListener("click", () => {
    const r = colorns();
    const g = colorns();
    const b = colorns();

    body.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;

    h2.textContent = `rgb(${r}, ${g}, ${b})`;
});