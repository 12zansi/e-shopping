function add_category(){
  let category_name = document.getElementById("category_name").value
  let parent_id = document.getElementById("parent_id").value
  let brand = new XMLHttpRequest()
  brand.onreadystatechange =() =>{
      if(brand.readyState == 4 && brand.status == 200){
          
      }
  }
  brand.open("POST","http://127.0.0.1:8000/category",true)
  let body = JSON.stringify({category_name:category_name,parent_id:parent_id})
  brand.setRequestHeader('Content-type','application/json;charset=UTF-8')
  brand.send(body) 
  alert("successfully category added")
  location.reload(); 
}

var url = 'http://127.0.0.1:8000/product?search_for='
var html_data = "";
function get_category(){
    var request = new XMLHttpRequest();
    request.onreadystatechange = () => {
      if (request.readyState == 4 && request.status == 200) {
        var obj = JSON.parse(request.response);
        console.log(obj)
      
        for(i=0;i<=obj.length-1;i++){
          
       
          html_data +=
            
            "<div class='cont'>" +
            "<div class='const'>"+
            "<div onclick = 'child(this)' class='fa  category'>-</div>"+
            // "<div onclick = 'childhide(this)' class='fa category opacity'>+</div>"+
            "<div class='category'>" +
            obj[i]["category_id"] +
            "</div>" +
    
            "<div class='category'>" +
            obj[i]["category_name"] +
            "</div>" +
            "</div>"+
            "<div id = 'child'></div>"+
           "</div>"
      
        }
        document.getElementById("category").innerHTML = html_data;
      }
    };
    request.open("GET", url+"category", true);
    request.send();
    
}

window.onload = get_category()
var html_data1 = '';
function child(td)
{
  console.log(td.parentNode.childNodes[1].innerHTML)
  // const boxes = document.querySelectorAll(".fa");
  // boxes.forEach((fa) => {
  //   fa.classList.remove("opacity");
  // });
  // let ur = td;
  // ur.classList.add("opacity");
  var request = new XMLHttpRequest();
    request.onreadystatechange = () => {
      if (request.readyState == 4 && request.status == 200) {
        var obj = JSON.parse(request.response);
       
        for(i=0;i<=obj.length-1;i++){
          
            
            html_data1 +=
              
            "<div class='cont'>" +
            "<div class='const'>"+
            "<div onclick = 'child(this)' class='category'>-</div>"+
            "<div class='category'>" +
            obj[i]["category_id"] +
            "</div>" +
    
            "<div class='category'>" +
            obj[i]["category_name"] +
            "</div>" +
            "</div>" +
            "<div id = 'child1'></div>"+
           "</div>"
      
        }
        document.getElementById("child").innerHTML = html_data1;
      }
    }
    
    request.open("GET", 'http://127.0.0.1:8000/category?parent_id='+td.parentNode.childNodes[1].innerHTML, true);
    request.send();
   
    
}
