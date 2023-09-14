document.addEventListener('DOMContentLoaded', function () {
    // Get the popup element and close button
    var popup = document.getElementById('cookiePopup');
    var closeButton = document.getElementById('closePopup');

    // Check if the session storage flag is set
    var popupDisplayed = sessionStorage.getItem('popupDisplayed');

    if (!popupDisplayed) {
        // Display the popup if it hasn't been displayed during this session
        popup.style.display = 'block';

        // Close the popup when the close button is clicked
        closeButton.addEventListener('click', function () {
            popup.style.display = 'none';

            // Set a flag in session storage to indicate the popup has been displayed during this session
            sessionStorage.setItem('popupDisplayed', 'true');
        });
    }
});
