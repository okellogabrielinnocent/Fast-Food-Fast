// Function for add item to menu by admin

document.getElementById('addItem').addEventListener('submit', addItem)

let user_userid = localStorage.getItem('Token');
let error = document.getElementById('error');

function addItem(event){
	event.preventDefault();
    let description = document.getElementById('description').value;
    let price = document.getElementById('price').value;
    // let user_userid = localStorage.getItem('Token');
	let status = '';
	fetch(`https://foodiefast.herokuapp.com/API/v1/menu`, {
		method:'POST',
        headers:{"Content-Type": "application/json",
        "Authorization": "Bearer "+ user_userid
    },
        
        body:JSON.stringify(
            {
                description:description,
                price:parseInt(price)
               
        })
        
	}).then((response) => {
        status = response.status;
        return response.json();
    })
    .then((data) => {
        if (status >= 404){
            error.style.display='block';
            document.getElementById('error').innerHTML = data["message"];
        }
        if (status == 201 ){
            window.location = 'addItem.html';
            error.style.display='none';
            success.style.display= 'block';
        }
    })
    .catch((err) => {
        console.log(err);
    })
}
