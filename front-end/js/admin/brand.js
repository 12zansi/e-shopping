function add_brand(){
    let brand_name = document.getElementById("brand_name").value
   
    let brand = new XMLHttpRequest()
    brand.onreadystatechange =() =>{
        if(brand.readyState == 4 && brand.status == 200){
            
        }
    }
    brand.open("POST","http://127.0.0.1:8000/brand",true)
    let body = JSON.stringify({brand_name:brand_name})
    brand.setRequestHeader('Content-type','application/json;charset=UTF-8')
    brand.send(body) 
    alert("successfully brand added")
    location.reload(); 
}

var url = 'http://127.0.0.1:8000/product?search_for='

function get_brand(){
    var request = new XMLHttpRequest();
    request.onreadystatechange = () => {
      if (request.readyState == 4 && request.status == 200) {
        var obj = JSON.parse(request.response);
        console.log(obj)
        var html_data = "";
        for(i=0;i<=obj.length-1;i++){
          
       
          html_data +=
            
            "<tr>" +
            "<td>" +
            obj[i]["brand_id"] +
            "</td>" +
    
            "<td class='upper'>" +
            obj[i]["brand_name"] +
            "</td>" +

           "</tr>"
      
        }
        document.getElementById("brand").innerHTML = html_data;
      }
    };
    request.open("GET", url+"brand", true);
    request.send();
    
}

window.onload = get_brand()

