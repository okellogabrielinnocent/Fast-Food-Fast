// Function for placing an order by user

document.getElementById('placeOrder').addEventListener('click', placeOrder)

let user_userid = localStorage.getItem('Token');

function placeOrder(event){
	event.preventDefault();
    let price = document.getElementById('quantity').value;
	// let status = '';
	fetch(`https://foodiefast.herokuapp.com/API/v1/users/orders`, {
		method:'POST',
        headers:{"Content-Type": "application/json",
        "Authorization": "Bearer "+ user_userid
    },
        
        body:JSON.stringify(
            {
                quantity:quantity
                
               
        })
	}).then((res) => {
        status = res.status;
        return res.json();
    })
    .then((data) => {
        if (status == 201 ){
            window.location = 'home.html';
            error.style.display='none';
            success.style.display= 'block';
        }
    })
}
