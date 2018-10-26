// Function for signup
document.getElementById('SignUpForm').addEventListener('submit', userSignup)


function userSignup(event){
	event.preventDefault();
    let username = document.getElementById('username').value;
    let address = document.getElementById('address').value;
	let email = document.getElementById('email').value;
	let password = document.getElementById('password').value;
    let error = document.getElementById('error');
    let success = document.getElementById('success');
	let status = '';
	fetch(`http://127.0.0.1:5000/API/v1/auth/user/signup`, {
		method:'POST',
		headers: {
            'Content-type':'application/json'
        },
        
        body:JSON.stringify(
            {
                username:username,
                password:password,
                address:address,
                email:email
               
        })
    })
    .then((res) => {
        status = res.status;
        return res.json();
    })
    .then((data) => {
        if (status >= 409){
            error.style.display='block';
            document.getElementById('error').innerHTML = data["message"];
        }
        if (status == 201 ){
            window.location = 'index.html';
            success.style.display= 'block';
            document.getElementById('success').innerHTML = data["message"];

        }
    })
}
