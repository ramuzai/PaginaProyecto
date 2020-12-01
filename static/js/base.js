const btnTop = document.getElementById('backToTop')

btnTop.addEventListener("click", function () {
	window.scrollTo({
		top: 0,
		left: 0,
		behavior: "smooth"
	});
});