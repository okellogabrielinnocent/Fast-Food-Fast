document.getElementById('avialable_menu').addEventListener('load', loadMenu);
let user_userid = localStorage.getItem('Token');

function loadMenu() {
    fetch(`https://foodiefast.herokuapp.com/API/v1/menu`, {
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
        console.log(data);
        let menus = data['Avialable menu'];
        
        let htmlInfo = `
        `;
        // iterate through returned array by element and key
        menus.forEach((element,key) => {
        htmlInfo += `
            <img src="/static/images/image.webp" alt="image" width="100%">
            <p>${element.description}</p>
            <p>shs${element.price}</p>
            <p><button onClick="declineOrder(${element.itemid})">Order</button></p>

            `; 
            // <a href="history.html"></a>
        });
        document.getElementById('avialable_menu').innerHTML = htmlInfo;
    
      })
      .catch(function(error){
            console.log(error);
        });
}
// itemid

function declineOrder(itemid){
    const quantity = prompt("Please add quantity", " ");
    let status = '';
    fetch(`https://foodiefast.herokuapp.com/API/v1/users/orders`,{
        method: 'POST',
        headers: {
            'Content-type':'application/json',
            "Authorization": "Bearer "+ user_userid
        },
        body:JSON.stringify(
            {   
                
                food_item_itemid:itemid,
                quantity:parseInt(quantity)
        })
    })
    .then((res)=>{
        status = res.status;
        return res.json();
    })
    .then((data) => {
        if (status == 201 ){
            window.location = 'history.html';
            error.style.display='none';
            success.style.display= 'block';
        }
    })
    .catch((err) => {
        console.log(err);
    });
}