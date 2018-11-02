/**
 * Created by Okello Gabriel Innocent.
 */
document.getElementById('SignInForm').addEventListener('submit', loginUser);

function loginUser(event){
    event.preventDefault();

    let email = document.getElementById('email').value;
    let passWord = document.getElementById('userPass').value;
    let error = document.getElementById('error');
    // Let pass in the route to fetch from
    fetch(`https://foodiefast.herokuapp.com/API/v1/auth/login`, {
        method: 'POST',
        headers: {
            'Content-type':'application/json'
        },
        body:JSON.stringify(
            {
                email:email,
                password:passWord
        })
    })
    .then((res) => {
        status = res.status;
        return res.json();
    })
    .then((data) => {
        if (status >= 404){
            error.style.display='block';
            document.getElementById('error').innerHTML = data["Message"];
        }
        if (status == 200 ){
            window.localStorage.setItem('Token', data.Token);
            if(email=='okellogabrielinnocent@gmail.com'){
                window.location = 'admin.html';
            }else{
                window.location = 'home.html';
            }

        }
    })
    .catch(err => console.log(err));
}
function logout(){
    localStorage.removeItem('Token');
    window.location.href = 'index.html';
}