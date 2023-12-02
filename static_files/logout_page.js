// app.js
function request(method, URL, param, callback = function () { }, callback_args = []) {
    let http_request = new XMLHttpRequest();
    try {
        http_request.open(method, URL);
        http_request.send(param);
        http_request.onloadend = function () {
            let data_backup = http_request.responseText;
            callback(http_request.responseText, callback_args);
        };
    } catch (err) {
        console.error(err);
    }
}

// Function to handle the 'Log In Again' button click
function handleLoginAgain() {
    // Here you might want to direct to a logout handler on the backend
    // For simplicity, we're just redirecting to a login page
    window.location.href = 'login.html';
}

// When the DOM content is loaded, attach the event to the 'Log In Again' button
document.addEventListener('DOMContentLoaded', function() {
    var loginAgainButton = document.getElementById('returnHome');
    if (loginAgainButton) {
        loginAgainButton.addEventListener('click', handleLoginAgain);
    }
});
