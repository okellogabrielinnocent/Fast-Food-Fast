import {loginPageUrl, hostAndPortUrl} from './main.js'

let signupErrorArea = document.getElementById('signupErrorArea');
//signupErrorArea.style.display = 'none';

let form = document.getElementById('SignUpForm');
form.addEventListener('submit', function signup(event) {
    event.preventDefault();
    let data = {
        username: form.username.value,
        email: form.email.value,
        password: form.password.value
    };
    let myHeader = new Headers({"Content-Type": "application/json", "Accept": "application/json"});
    const signup_api_url = hostAndPortUrl+'/v1/auth/user/signup';
    let option = {
        headers: myHeader,
        method: "POST",
        body: JSON.stringify(data)
    };
    let signup_request = new Request(signup_api_url, option);
    function readResponseAsJSON(response) {

        return response.json().then(json => {
          return {
                   responseData: json,
                   status: response.status
                 }
        })
    }
    function signupJSON(requestPath) {
        fetch(requestPath)
            .then(readResponseAsJSON)
            .then(function (response) {
                if(response.status >= 200 && response.status < 300){
                    // when  signup succeds
                    alert(response.responseData.message);
                    window.location.replace(loginPageUrl);

                }else {
                    // when signup fails
                    signupErrorArea.innerText = response.responseData.message;
                    signupErrorArea.style.display = 'block';
                }
            })
    }
    signupJSON(signup_request);
    form.reset()
});