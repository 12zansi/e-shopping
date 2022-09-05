function redirect() {
    window.location= "login.html";
 }
function register(){
   
    let username = document.getElementById("username").value
    let email = document.getElementById("email").value
    let password = document.getElementById("password").value
    let register = new XMLHttpRequest()
    register.onreadystatechange =() =>{
        if(register.readyState == 4 && register.status == 200){
            redirect()
        }
    }
    register.open("POST","http://127.0.0.1:8000/auth/register",true)
    let body = JSON.stringify({username:username,email:email,password:password})
    register.setRequestHeader('Content-type','application/json;charset=UTF-8')
    register.send(body)
    alert("successfully registered")
}