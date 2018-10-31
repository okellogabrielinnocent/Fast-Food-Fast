document.getElementById('user_orders').addEventListener('load', getAllOrders);
let user_userid = localStorage.getItem('Token');

function getAllOrders() {
    fetch(`https://foodiefast.herokuapp.com/API/v1/orders`, {
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
        let orders = data.Orders;
        // Pass ui in template literal
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
                <button class="complete order-button" onClick="completeOrder(${element.orderid})">Complete </button>
                <button class="decline order-button" onClick="declineOrder(${element.orderid})">Decline </button>                                
            </td>
        </tr>
        `;  
    
        });
        document.getElementById('user_orders').innerHTML = htmlInfo;
    
      });
}
// function to mark order as complete
function completeOrder(orderid){
    let status = ''
    fetch(`https://foodiefast.herokuapp.com/API/v1/orders/${orderid}`,{
        method: 'PUT',
        headers: {
            'Content-type':'application/json',
            "Authorization": "Bearer "+ user_userid
        },
        body:JSON.stringify(
            {   
                orderid:orderid,
                order_status:'Complete'
        })
    }).then((res)=>{
        status = res.status;
        return res.json()
    }).then((data)=>{
        if(status==200){
            alert('Do you want to Accept this order');
            location.reload();
        }
    });
}
// Function to decline order
function declineOrder(orderid){
    let status = ''
    fetch(`https://foodiefast.herokuapp.com/API/v1/orders/${orderid}`,{
        method: 'PUT',
        headers: {
            'Content-type':'application/json',
            "Authorization": "Bearer "+ user_userid
        },
        body:JSON.stringify(
            {   
                orderid:orderid,
                order_status:'Cancelled'
        })
    }).then((res)=>{
        status = res.status;
        return res.json()
    }).then((data)=>{
        if(status==200){
            alert('Do you want to Dcline this order');
            location.reload();
        }
    });
}