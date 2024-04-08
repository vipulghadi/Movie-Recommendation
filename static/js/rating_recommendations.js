var slider = document.getElementById("myRange");
var output = document.getElementById("demo");
output.innerHTML = slider.value; // Display the default slider value

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = this.value;
}

var recommendationsContainer = document.getElementById("ratingbase-recommendations");

function getRatingRecommendations() {
    var ratingRange = document.getElementById("rating").value;
    var genre = document.getElementById("genre").value;
    var numberOfRecommendations = parseInt(document.getElementById("demo").innerHTML);
    var language = document.getElementById("language").value;

    fetch('http://127.0.0.1:5000/rating', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                genre: genre,
                rating: ratingRange,
                num: numberOfRecommendations,
                lang: language
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log the response data for testing
            displayRecommendations(data.data); // Call a function to display recommendations
        })
        .catch(error => alert("error while searching data"));
}

function displayRecommendations(data) {

    recommendationsContainer.innerHTML = ""; // Clear previous recommendations
    recommendationsContainer.style.display = "block"
    data.forEach(function(movie, index) {
        if (movie.title) {
            var movieElement = document.createElement("div");
            movieElement.classList.add("d-flex", "m-2", "p-2", "movie-card-design"); // Add Bootstrap classes for card and margin/padding

            // Set inner HTML content for the movie recommendation
            movieElement.innerHTML = `
            <div class="movie-image"> <img src="${movie.image_url}" class="" alt="Movie Poster"  ></div>
           
                <div class="movie-info">
                    <h3 class="card-title">${movie.title}</h3>
                    <p class="card-text">${movie.movie_desc}</p>
                  
                </div>
              
            `;

            // Append the movie recommendation element to the recommendations container
            recommendationsContainer.appendChild(movieElement);
        }

    })
}