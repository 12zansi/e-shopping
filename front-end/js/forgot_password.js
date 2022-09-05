
function forgot_password(){

        
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;
        var confirm_password = document.getElementById('confirm_password').value;
        
        if(password == confirm_password)
        {

        
        var url= "http://127.0.0.1:8000/user"
        var request = new XMLHttpRequest
        
        // let object1 = JSON.parse(request.response)
        // localStorage.setItem("users",JSON.stringify(object1.access_token))
        request.onreadystatechange = () =>{
            if(request.readyState == 4 && request.status == 200){
                let object1 = JSON.parse(request.response)
                console.log(object1)
    
                window.location= "login.html";
            }
        }
        if(username=="" || password=="")
        {
            alert("please enter the value")
        }
        else{
            request.open("PUT",url,true)
            request.setRequestHeader('Content-type','application/json;charset=UTF-8')
            var body = JSON.stringify({username:username,password:password});
            request.send(body)
        }
         
    }
    else{
        alert("password not matched")
    }
        
      }