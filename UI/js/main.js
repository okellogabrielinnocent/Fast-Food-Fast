/**
 * Created by Okello Gabriel Innocent
 */

export let loginPageUrl = "index.html";
export let menuItemsUrl = "UI/home.html";
export let hostAndPortUrl = "http://127.0.0.1:5000";


// this currently returns the user token
export function getToken() {
    return localStorage.getItem('Token');
}

export function getFromCurrentUserName() {
    return localStorage.getItem('username')
}
export function getCurrentUserEmail() {
    return localStorage.getItem('email')
}
export function getFromCurrentUserid() {
    return localStorage.getItem('userid')
}
export function logoutUser() {
    // logout the current user by learing token info
    localStorage.clear();
    window.location.replace(loginPageUrl)
}

// Also include the URL to where the page should be redirected
function fetchCurrentUserInfo(pathToResource, RedirectUrlParameter) {
    fetch(pathToResource)
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        if(data.message){
            window.location.replace(loginPageUrl)
        }else {
            logResult("username", data.User_info.username);
            logResult("email", data.User_info.email);
            window.location.replace(RedirectUrlParameter);
        }
    })
}


export function getUserInfo(RedirectUrlParameter) {
        // This function retrieves the info of the current user
        
        const userInfoUrl = hostAndPortUrl+"/API/v1/auth/login";

        let header = new Headers({"Content-Type": "application/json",
                                  "Authorization": getTokenFromVerifyUser()});

        
        let option = {
            method: "GET",
            headers: header
        };

        let req = new Request(userInfoUrl, option);

        // call to the function that fetches the current user info
        fetchCurrentUserInfo(req, RedirectUrlParameter);

    }

export function logResult(key, value) {
    localStorage.setItem(key, value);
}