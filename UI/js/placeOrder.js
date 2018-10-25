// Function for placing an order by user

document.getElementById('placeOrder').addEventListener('click', placeOrder)

let user_userid = localStorage.getItem('Token');

function placeOrder(event){
	event.preventDefault();
    let price = document.getElementById('quantity').value;
	// let status = '';
	fetch(`http://127.0.0.1:5000/API/v1/users/orders`, {
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


























// function placeOrder(meal_name, quantity, location){
//     token = window.localStorage.getItem('token');
//     fetch('http://127.0.0.1:5000/api/v2/users/orders', {
//           method:'POST',
//           headers: {
//             'content-type':'application/json',
//             'Authorization': 'Bearer ' + token
//           },
//         //   mode: 'cors',
//           body:JSON.stringify({
//             'meal_name':meal_name,
//             'quantity':quantity,
//           })  
//     }
//     ).then((res)=>{
//       code = res.code;
//       return res.json();
//     })
//     .then(data=>{
//       console.log(data);
//       if (data.msg=='order placed'){
//         window.location = 'history.html'
//       }
//     })
// }

// document.getElementById('submit').addEventListener('click', function(e){
// e.preventDefault();
// var location = document.getElementById('location').value;
// var quantity = document.getElementById('number-of-piece').value;
// var meal_name = document.getElementById('meals2').value;
// placeOrder(meal_name, quantity, location);

// });