document.getElementById('avialable_menu').addEventListener('load', loadMenu);
let user_userid = localStorage.getItem('Token');

function loadMenu() {
    fetch(`http://127.0.0.1:5000/API/v1/menu`, {
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
        let menus = data['Avialable menu'];
        
        let htmlInfo = `
        `;
        // iterate through returned array by element and key
        menus.forEach((element,key) => {
        htmlInfo += `
            <img src="images/image.webp" alt="image" width="100%">
            <p>${element.description}</p>
            <p>shs${element.price}</p>
            <p><a href="history.html"><button>Order</button></a></p>
            `;  
    
        });
        document.getElementById('avialable_menu').innerHTML = htmlInfo;
    
      })
      .catch(function(error){
            console.log(error);
        })
}
