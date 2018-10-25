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
        <h3>Menu</h3>
        <table>
                    <tr>
                        <th class="narrow">NO:</th>
                        <th>Details</th>
                        <th class="narrow">Price (Shs)</th>
                        <th>Action</th>
                    </tr>
        `;
        // iterate through returned array by element and key
        menus.forEach((element,key) => {
        htmlInfo += `
        <tr>
            <td>${element.itemid}</td>
            <td> ${element.description}</td>
            <td>${element.price}</td>                           
            <td>
                <a href="addItem.html"><button class="complete order-button">Edit</button></a>
                <button class="decline order-button">Delete </button>                               
            </td>
        </tr>
            `;  
    
        });
        document.getElementById('avialable_menu').innerHTML = htmlInfo;
    
      })
      .catch(function(error){
            console.log(error);
        })
}
