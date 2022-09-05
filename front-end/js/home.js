function logout(){
    localStorage.removeItem("users");
    window.location = "home.html";
}

function onload_event() {
    var x = JSON.parse(localStorage.getItem("users"));
    let xhr = new XMLHttpRequest();
  
    xhr.onreadystatechange = () => {
      if (xhr.readyState === 4 && xhr.status === 200) {
        let object1 = JSON.parse(xhr.response);
        let user = object1.username;
        let z = document.getElementById("pi");
        z.innerHTML = user;
        let out = document.getElementById("logout");
        if (localStorage.getItem("users") !== null) {
          let login = document.getElementById("log");
          let r = document.getElementById("regs");
          r.style.display = "none";
          login.style.display = "none";
          out.style.display = "block";
        }
        
      }
    };
    xhr.open("GET", "http://127.0.0.1:8000/user", true);
    xhr.setRequestHeader("token", x);
    xhr.send();
  }

window.onload = onload_event;