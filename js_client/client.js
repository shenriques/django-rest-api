// get the log in form, event handler
const loginForm = document.getElementById('login-form');

const baseEndpoint = "http://localhost:8000/api";

if (loginForm) {

    // add event listener to the handler
    loginForm.addEventListener('submit', handleLogin)
}

function handleLogin(event) {

    event.preventDefault();

    const loginEndpoint = `${baseEndpoint}/token/`

    // doesnt matter what input is, which make it form data
    let loginFormData = new FormData(loginForm)
    let loginObjectData = Object.fromEntries(loginFormData) // actual object data (jsO)

    // JSON string of the data (jsON)
    let bodyData = JSON.stringify(loginObjectData) 

    const options = {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: bodyData
    }

    fetch(loginEndpoint, options) // basically requests.POST. returns a promise
    .then(response => {
            return response.json()
    })
    .then (x => {
        console.log(x)
    })
    .catch (err => {
        console.log('error', err)
    })
}