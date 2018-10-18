/**
 * Created by Okello Gabriel Innocent.
 */

// import {getUserInfo, logResult, menuItemsUrl, hostAndPortUrl} from './main.js';


// /************ Login user ****************************/

// let form = document.getElementById("SignInForm");

// // hide by default| padding makes it visible
// let loginErrorArea = document.getElementById("loginError");



// function readResponseAsJSON(response) {
//     return response.json();
// }

// function fetchJSON(pathToResource) {
//     fetch(pathToResource) 
//     .then(readResponseAsJSON) 
//     .then((data) => {
//         if(data.Token){
//             logResult("Token", data.Token); 
//             // setting user token

//             // specify the url to the page you want to go
//             getUserInfo(menuItemsUrl);
//             //window.location.replace(menuItemsUrl)
//         }else{
//             loginErrorArea.innerText = data.message;
//             loginErrorArea.style.display = 'block';
//         }

//     })
// }


// form.addEventListener('accept-btn', function getInfo(event){
//     event.preventDefault();

//     // Login with passwprd or email
//     let data = {
//     password: form.password.value
//     };

//     let userInput = form.email.value,
//     at = "@",
//     dot = ".";

//     if (userInput.includes(at) && userInput.includes(dot)){
//         data['password'] = form.password.value;
//     }else {
//         data['email'] = form.email.value;
//     }


//     const login_uri = hostAndPortUrl+"/api/v1/auth/login";

//     let head = new Headers({"Content-Type": "application/json", "Accept": "application/json"});
//     let option = {
//         method: "POST",
//         headers: head,
//         body: JSON.stringify(data)
//     };
//     let req = new Request(login_uri, option);
//     fetchJSON(req);
//     form.reset();
// });

document.getElementById('SignInForm').addEventListener('submit', loginUser);

function loginUser(event){
    event.preventDefault();

    let email = document.getElementById('email').value;
    let passWord = document.getElementById('userPass').value;

    //declaring errors,messages and status variables to be used
    // let error = document.getElementById('error');
    // let success = document.getElementById('message');
    // let status = '';

    fetch(`http://127.0.0.1:5000/API/v1/auth/login`, {
        method: 'POST',
        headers: {
            'Content-type':'application/json'
        },
        body:JSON.stringify(
            {
                email:email,
                password:passWord
        })
    }).then((res) => {
        status = res.status;
        return res.json();
        // console.log(res)
    })
    .then((data) => {
        // if (status >= 400){
        //     error.style.display='none';
        //     error.style.display='block';
        //     // document.getElementById('error').innerHTML = data["error"];
        // }
        if (status == 200 ){
            window.localStorage.setItem('Token', data.Token);
            if(email=='okellogabrielinnocent@gmail.com'){
                window.location = 'admin.html';
            }else{
                window.location = 'home.html';
            }

        }
    })
    .catch((err)=>console.log(err))
}
//redirect user to orders made if user already has an access token
// if (location.href.match(/index/)){
//     if (localStorage.getItem('Token') != null){
//         window.location.href = 'home.html';
//     }
// }
//logout
function logout(){
    localStorage.removeItem('Token');
    window.location.href = 'index.html';
}