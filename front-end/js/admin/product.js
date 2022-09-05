function add_product(){
    let product_name = document.getElementById("name").value
    let desc = document.getElementById("desc").value
    let mrp = document.getElementById("mrp").value
    let price = document.getElementById("price").value
    let model_name = document.getElementById("model").value
    let brand_id = document.getElementById("brand").value
    let category_id = document.getElementById("category").value
    let return_policy = document.getElementById("return").value
    let product = new XMLHttpRequest()
    product.onreadystatechange =() =>{
        if(product.readyState == 4 && product.status == 200){
            
        }
    }
    product.open("POST","http://127.0.0.1:8000/product",true)
    let body = JSON.stringify({ name: product_name,
        description: desc,
        mrp: mrp ,
        price: price,
        model_name: model_name,
        brand_id: brand_id,
        category_id: category_id,
        return_policy: return_policy})
    product.setRequestHeader('Content-type','application/json;charset=UTF-8')
    product.send(body) 
    alert("successfully product added")
    location.reload(); 
  }

var url = 'http://127.0.0.1:8000/product?search_for='

function get_product(){
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
            obj[i]["product_id"] +
            "</td>" +
    
            "<td class='upper'>" +
            obj[i]["name"] +
            "</td>" +

            "<td class='upper'>" +
            obj[i]["mrp"] +
            "</td>" +

            "<td class='upper'>" +
            obj[i]["price"] +
            "</td>" +

            "<td class='upper'>" +
              parseInt(100 - 100 * obj[i]["price"]/obj[i]["mrp"])+'%'  +
            "</td>" +
              
            "<td><button class='btn btn-primary' id='edit' onclick='run(this)' data-bs-toggle='modal' data-bs-target='#myModal2'>Add More Images</button><button id='deleteu' class='btn btn-danger' data-bs-toggle='modal' data-bs-target='#myModal3' onclick= 'run(this)'>Add More Detail</button></td>" +
           "</tr>"
      
        }
        document.getElementById("product").innerHTML = html_data;
      }
    };
    request.open("GET", url+"product", true);
    request.send();
    
}

window.onload = get_product()

var btn1 = document.querySelector('#btn1')
function add_more_images(){
        var div = document.createElement("div")
        div.innerHTML = file1()
        document.getElementById('image1').appendChild(div)
      
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
   document.getElementById("productid").value = btn.parentElement.parentElement.cells[0].innerHTML
}

function result(){
  var x = document.querySelectorAll(".file1")
  var pid =  document.getElementById("product_id").value
  
      for(i=0;i<x.length;i++){
          var formData = new FormData();
          formData.append("file1",x[i].files[0])
          formData.append("product_id",pid)
         
          var request = new XMLHttpRequest();
          request.onreadystatechange = () => {
            if (request.readyState == 4 && request.status == 200) {
                console.log(request)
            }
          }
    
          request.open("POST", "http://127.0.0.1:8000/product/images", true);
          request.send(formData)
          alert("images succefully added")
      }
     
}

function xml_request(detail){
  detail.onreadystatechange =() =>{
        if(detail.readyState == 4 && detail.status == 200){
            
        }
    }
    detail.open("POST","http://127.0.0.1:8000/product/details",true)
    detail.setRequestHeader('Content-type','application/json;charset=UTF-8')
}

function save(){
  var x = document.querySelectorAll(".key")
  var  value1 = document.querySelectorAll(".value")
  var pid =  document.getElementById("productid").value
  for(i=0;i<x.length;i++)
  {
    console.log(x[i].value,value1[i].value)
    u = x[i].value
    v = value1[i].value
    e = []
    obj = {}
    if(v.indexOf(',') > -1) {
     
      e = v.split(',')
      obj[u] =  e
      body = JSON.stringify({ dict_type:obj, product_id:pid })
      detail = new XMLHttpRequest()
      xml_request(detail)
      detail.send(body)

    }
    else{

       obj[u] =  v
       body = JSON.stringify({ dict_type:obj, product_id:pid })
       detail = new XMLHttpRequest()
       xml_request(detail)
       detail.send(body)
       alert("detail succefully added")

    }
  }
}

function add_more_textbox(){
   var div = document.createElement("div")
   div.classList.add('col1')
   div.innerHTML = gt()
   document.getElementById('product1').appendChild(div)
}

function gt(){
  return "<input type = 'text' class = 'form-control key'><input type = 'text' class = 'form-control value'><button onclick = 'removeit(this)'>remove</button>"
}

function removeit(btn){
  console.log(btn.parentNode)
  document.getElementById('product1').removeChild(btn.parentNode)
  
  
}