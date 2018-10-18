document.getElementById('menu').addEventListener('click', loadMenu);

function loadMenu() {
    fetch('http://127.0.0.1:5000/API/v1/menu')
    .then(function(response){
         return response.json();
    })
    .then(function(menus){
         let html = '';

         menus.forEach(function(menu){
              html += `
                   <li>
                       ${menu.description}
                       ${menu.price}
                   </li>
              `;
         });
         document.getElementById('result').innerHTML = html;
    })
    .catch(function(error){
         console.log(error);
    })
}