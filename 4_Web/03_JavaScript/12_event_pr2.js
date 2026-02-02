const form = document.querySelector("form");
const idinput = document.querySelector("#userid");
const commentinput = document.querySelector("#comment");
const commentlist = document.querySelector(".comment-list");

form.addEventListener("submit", (e) => {
    e.preventDefault();

    const id = idinput.value;
    const comment = commentinput.value;


    const li = document.createElement("li");

    li.innerHTML = `<strong>${id}</strong> - ${comment}`;

    commentlist.appendChild(li);

    idinput.value = "";
    commentinput.value = "";
});