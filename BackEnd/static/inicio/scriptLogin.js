var loginSection = document.getElementById("login-section");
var registroSection = document.getElementById("registro-section");
var btnEnviar = document.getElementById('Ingresar');
btnEnviar.addEventListener('click', iniciarSesion);

function toggleRegistration() {
  if (loginSection.style.display === "none") {
    loginSection.style.display = "block";
    registroSection.style.display = "none";
  } else {
    loginSection.style.display = "none";
    registroSection.style.display = "block";
  }
}


function iniciarSesion() {
  var user = document.getElementById('username').value;
  var pass = document.getElementById('password').value;
  const url = 'http://localhost:8000/api/personas/getAll/';
  params = {correo: user,password: pass};
  console.log(JSON.stringify(params))
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: JSON.stringify(params)
  })
    .then(response => response.json())
    .then(data => {
      // Aquí puedes trabajar con la respuesta de la API
    })
    .catch(error => {
      // Manejo de errores
      console.error('Error:', error);
    });
}

