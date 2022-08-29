var url = 'http://127.0.0.1:8000/product?search_for='
var id = [];
var category = [];
function load() {
    var request = new XMLHttpRequest();
    request.onreadystatechange = () => {
      if (request.readyState == 4 && request.status == 200) {
        var obj = JSON.parse(request.response);
        console.log(obj)
        for(i=0;i<=obj.length-1;i++){
          var div = document.createElement("option")
          var div1 = document.createElement("option")
          document.getElementById('brand').appendChild(div1)
          div1.innerHTML = obj[i]["brand_name"]
          document.getElementById('sel1').appendChild(div)
          div.innerHTML = obj[i]["category_name"]

          category.push(obj[i]["category_name"])
          id.push(obj[i]["category_id"])
        }
      }
    };
    request.open("GET", url+"category", true);
    request.send();
    
  }

window.onload = load(),get_product()

function add_product(){

  sel1 = document.getElementById("sel1")
  var get_value = sel1.options[sel1.selectedIndex].value; 
  for(i = 0;i<category.length;i++){
     if(category[i] == get_value)
     {
        u = id[i]
        console.log(u)
     }
  }

}


function get_product(){
    var request = new XMLHttpRequest();
    request.onreadystatechange = () => {
      if (request.readyState == 4 && request.status == 200) {
        var obj = JSON.parse(request.response);
        console.log(obj)
        var html_data = "";
        for(i=0;i<=obj.length-1;i++){
          console.log(obj[i])

       
          html_data +=
            
            "<tr>" +
            "<td>" +
            obj[i]["product_id"] +
            "</td>" +
            "<td>" +
            obj[i]["name"] +
            "</td>" +
            "<td class='upper'>" +
            obj[i]["brand_name"] +
            "</td>" +
            "<td class='upper'>" +
            obj[i]["category_name"] +
            "</td>" +
            "<td class='upper'>" +
            obj[i]["price"] +
            "</td>" +
            "<td><button class='btn btn-primary' id='edit' onclick='run(this)' data-bs-toggle='modal' data-bs-target='#myModal2'>Add More Images</button><button id='deleteu' class='btn btn-danger' data-bs-toggle='modal' data-bs-target='#deleteModal' onclick='deleter(this)'>Add More Detail</button></td>" +
           "</tr>"
      
        }
        document.getElementById("product").innerHTML = html_data;
      }
    };
    request.open("GET", url+"product", true);
    request.send();
    
}

var btn1 = document.querySelector('#btn1')
function add_more_images(){
        var div = document.createElement("div")
        div.innerHTML = file1()
        document.getElementById('image1').appendChild(div)
        // console.log(document.getElementById('file1').files[0]['name'])
}

function result(){
    var x = document.querySelectorAll(".file1")
    var y = document.getElementById('color')
    var pid =  document.getElementById("product_id").value
    var total_stock = document.getElementById("total_product").value
        for(i=0;i<x.length;i++){
            var formData = new FormData();
            formData.append("file1",x[i].files[0])
            // console.log(x[i].files[0]['type'])
            
            formData.append("product_id",pid)
            formData.append("color",y.value)
            formData.append("total_product",total_stock);
            var request = new XMLHttpRequest();
            request.onreadystatechange = () => {
              if (request.readyState == 4 && request.status == 200) {
                  console.log(request)
              }
            }
            // let body = JSON.stringify({
            // //     Object.fromEntries(formData)
            //     // file1: x[i].files[0]['name'],
            //     // product_id: pid,
            //     // color: y.value,
            //     // total_product: total_stock 
            //     file1: '@'+x[i].files[0]['name']+';type=image/png',
            //     product_id:pid, color:y.value,total_product:total_stock 
            // });
            request.open("POST", "http://127.0.0.1:8000/product/add_product_images", true);
          
            // request.send("file1=",x[i].files[0],"&product_id=",product_id,"&color=",color,"&total_product=",total_stock);
            request.send(formData)
        }
       
}

function file1()
{
    return "<input type='file' class='file1'><button onclick = 'remove_it(this)'>remove</button>"
}

function remove_it(btn){
    console.log(btn.parentNode)
    document.getElementById('image1').removeChild(btn.parentNode)
    
 }

function run(btn){
   document.getElementById("product_id").value = btn.parentElement.parentElement.cells[0].innerHTML
}

function add_t(){
  var t = document.getElementById("file23")
  console.log(t.value)
  var request = new XMLHttpRequest();
  request.onreadystatechange = () => {
    if (request.readyState == 4 && request.status == 200) {
        console.log(request.response)
    }
  }
  var formData = new FormData();
  formData.append("file",t.files[0])
  request.open("POST", "http://127.0.0.1:8000/file", true);
  // request.setRequestHeader(
  //   'accept','application/json')
  // request.send("file1=",x[i].files[0],"&product_id=",product_id,"&color=",color,"&total_product=",total_stock);
  request.send(formData)
}