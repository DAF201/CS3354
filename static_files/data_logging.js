function request(method, URL, param, callback = function () { }, callback_args = []) {
    let http_request = new XMLHttpRequest();
    try {
        http_request.open(method, URL, true);
        http_request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        http_request.send(param);
        http_request.onloadend = function () {
            let data_backup = http_request.responseText;
            callback(http_request.responseText, callback_args);
        };
    } catch (err) {
        console.error(err);
    }
}

// Add event listener for the form submission
document.getElementById('dataForm').addEventListener('submit', function(e) {
    e.preventDefault();
    let workoutType = this.workoutType.value;
    let duration = this.duration.value;
    let caloriesBurned = this.caloriesBurned.value;

    // Construct the parameters as a URL-encoded string
    let params = `workoutType=${encodeURIComponent(workoutType)}&duration=${encodeURIComponent(duration)}&caloriesBurned=${encodeURIComponent(caloriesBurned)}`;

    request('POST', 'https://your-backend-url.com/data-log', params, function(response) {
        console.log('Data logged:', response);
        // Handle the response here
    });
});
