function redirectToSelected() {
    var recommendationType = document.getElementById("recommendation-type").value;
    console.log(recommendationType);
    if (recommendationType === "movie") {
        window.location.href = "http://127.0.0.1:5000/option/content";
    } else if (recommendationType === "rating") {
        window.location.href = "http://127.0.0.1:5000/option/rating";
    }
}