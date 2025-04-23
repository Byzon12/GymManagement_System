function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            let latitude = position.coords.latitude;
            let longitude = position.coords.longitude;
            document.getElementById("locationField").value = latitude + "," + longitude;
        }, function(error) {
            console.log("Error getting location:", error);
        });
    } else {
        console.log("Geolocation is not supported by this browser.");
    }
}

document.getElementById("enquiryForm").addEventListener("submit", function(event) {
    getLocation();  // Fetch the location
});
