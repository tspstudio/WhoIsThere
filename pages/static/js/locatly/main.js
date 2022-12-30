function setText() {
	document.querySelector(".indicator").innerHTML = "No people found. Try again later.";
}
function main() {
	document.querySelector(".indicator").setAttribute("style","visibility: visible;");
	locate();
	setTimeout(setText,1500);
}