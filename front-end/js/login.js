function redirect() {
    window.location= "home.html";
}

document.addEventListener('DOMContentLoaded', function(){
    document.getElementById('login').onclick = function(){
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;
        var url= "http://127.0.0.1:8000/auth/login"
        var request = new XMLHttpRequest
    
        request.onreadystatechange = () =>{
            if(request.readyState == 4 && request.status == 200){
                let user = JSON.parse(request.response)
                localStorage.setItem("users",JSON.stringify(user.access_token))
                if(user['is_admin'] == 1)
                {
                    window.location = "admin/home.html";
                }
                else
                {
                  window.location= "home.html";
                }
            }
        }
        if(username=="" || password=="")
        {
            alert("please enter the value")
        }
        else{
            request.open("POST",url,true)
            request.setRequestHeader('Content-type','application/json;charset=UTF-8')
            var body = JSON.stringify({username:username,password:password});
            request.send(body)
            if (localStorage.getItem("users") === null) {
                var spinner = document.getElementById("spinner")
                spinner.style.display = "block";
            }
            // alert("succesfully login")
        }
         
        
      }
    })