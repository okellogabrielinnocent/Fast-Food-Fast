document.getElementById('UserOrders').addEventListener('load', loadUserOrders);
let user_userid = localStorage.getItem('Token');

function loadUserOrders() {
    fetch(`http://127.0.0.1:5000/API/v1/users/orders`, {
		method:'GET',
        headers:{"Content-Type": "application/json",
                "Authorization": "Bearer "+ user_userid}
    })
    .then(function(response){
         return response.json();
    })
    .then(function(orders){
         let html = '';

         orders.forEach(function(order){
            html += `
            
            `;
         });
         document.getElementById('order').innerHTML = html;
    })
    .catch(function(error){
         console.log(error);
    })
}