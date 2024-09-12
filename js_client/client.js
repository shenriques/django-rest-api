// get the log in form, event handler
const loginForm = document.getElementById('login-form');

const baseEndpoint = "http://localhost:8000/api";

const contentContainer = document.getElementById('content-container');

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
    .then(
        authData => { 
            handleAuthData(authData, getProductList) // after authdata is set, list products
        })
    .catch (err => {
        console.log('error', err)
    })
}

function handleAuthData(authData, callback) {
    // set these token
    localStorage.setItem('access', authData.access)
    localStorage.setItem('refresh', authData.refresh)

    // call the function passed in (list products)
    if (callback) {
        callback()
    }
}

function writeToContainer(data) {
    if (contentContainer) {
        contentContainer.innerHTML = "<pre>" + JSON.stringify(data, null, 4) + "</pre>"
    }
}

function getFetchOptions(method, body) {
    return {
        // GET request if method undefined, otherwise method
        method: method === null ? "GET" : method,
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${localStorage.getItem('access')}`
        },
        body: body ? body : null
    }
}

function isTokenNotValid(jsonData) {
    if (jsonData.code && jsonData.code === "token_not_valid") {
        // or run a refresh token fetch
        alert("Please log in again")
        return false
    }
    return true
}

function getProductList() {
    const endpoint = `${baseEndpoint}/products/`
    const options = getFetchOptions()

    fetch(endpoint, options)
    .then(response => {
        console.log(response)
        return response.json()
    })
    .then(data => {
        const validData = isTokenNotValid(data) 
        if (validData) {
            writeToContainer(data)
        }
    })
}