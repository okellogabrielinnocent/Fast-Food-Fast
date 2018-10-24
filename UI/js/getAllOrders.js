document.getElementById('user_orders').addEventListener('load', getAllOrders);
let user_userid = localStorage.getItem('Token');

function getAllOrders() {
    fetch(`http://127.0.0.1:5000/API/v1/orders`, {
        method:'GET',
        // pass in the header so that one can ge the token
        headers:{'Accept': 'application/json, text/plain, */*',
                "Content-Type": "application/json",
                "Authorization": "Bearer "+ user_userid}
    })
    .then(function(response){
        // console.log(response);
        return response.json();
         
    })
    .then(data=>{
        // console.log(data);
        let orders = data['Orders'];
        let htmlInfo = ` 
        <h3>Orders</h3>
        <table>
        <tr>
            <th class="narrow">Order Number</th>
            <th>Details</th>
            <th>Order Status</th>
            <th>Quantity</th>
            <th class="narrow">Amount Due (Ugsh)</th>
            <th>Order Date</th>
            <th>Actions</th> 

        </tr>
        `;
        orders.forEach((element,key) => {
        htmlInfo += ` 
              
        <tr>
            <td>${element.orderid}</td>
            <td> ${element.description}</td>
            <td>${element.order_status} </td>
            <td>${element.quantity}</td>
            <td>${element.price}</td>            
            <td>${element.order_date}</td>                             
            <td>
                <a href="admin.html"><button class="complete order-button">Complete </button></a>
                <a href="admin.html"><button class="decline order-button">Decline </button></a>                                 
            </td>
        </tr>
        `;  
    
        });
        document.getElementById('user_orders').innerHTML = htmlInfo;
    
      });
}