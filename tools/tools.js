
function print(str) {
    console.log(str)
}

function replace_innerHTML(id, str) {
    document.getElementById(id).innerHTML = str
}

async function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function request(mathod, URL, param, callback = function () { }, callback_args = []) {
    let http_request = new XMLHttpRequest()
    try {
        http_request.open(mathod, URL)
        http_request.send(param)
        http_request.onloadend = function () {
            data_backup = http_request.responseText
            callback(http_request.responseText, callback_args)
        }
    } catch (err) {
        print(err)
    }
}