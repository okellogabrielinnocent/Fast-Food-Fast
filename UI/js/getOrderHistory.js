document.getElementById('user_orders').addEventListener('load', getUserOrderHistory);
let user_userid = localStorage.getItem('Token');

function getUserOrderHistory() {
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
        let orders = data['Orders'];
        let htmlInfo = ` 
        <h3>Order History</h3>
        
        `;
        orders.forEach((element,key) => {
        htmlInfo += ` 
            <div class="order-user">
                <div class="description">
                    <p>Order Date: ${element.order_date} By: Innocent</small></p>
                </div>
            </div>
            <div class="order-content">
                <div class="title">
                    Fast Food - <span class="price">${element.price} UGX</span> 
                </div>
                <div class="description">
                    ${element.description}
                </div>
              </div>
              <div class="quantity">
                <div class="description">
                    ${element.quantity}
                </div>
              </div>
              <div class="pend-button">
                  <a href="history.html" class="button" onclick="update()" >${element.order_status}</a>
              </div>
        `;  
    
        });
        document.getElementById('user_orders').innerHTML = htmlInfo;
    
      });
}

function update(){
    fetch(`https://foodiefast.herokuapp.com/API/v1/orders/<orderid>`, {
        method:'PUT',
        // pass in the header so that one can ge the token
        headers:{'Accept': 'application/json, text/plain, */*',
                "Content-Type": "application/json",
                "Authorization": "Bearer "+ user_userid}
    })
    .then(function(response){
        // console.log(response);
        return response.json();
         
    })

}