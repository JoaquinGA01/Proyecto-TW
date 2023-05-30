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
  var user = document.getElementById('username');
  var pass = document.getElementById('password');
  const url = 'http://localhost:8000/api/personas/getAll';
  const params = {
    correo: user,
    password: pass
  };
  console.log(params)
  fetch(url, {
    method: 'POST',
    headers: {
      'accept':' application/json',
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: JSON.stringify(params)
  })
    .then(response => response.json())
    .then(data => {
      // Aquí puedes trabajar con la respuesta de la API
      mostrarRespuesta(data);
    })
    .catch(error => {
      // Manejo de errores
      console.error('Error:', error);
    });
}

function mostrarRespuesta(data) {
  var responseDiv = document.getElementById('response');
  responseDiv.innerHTML = JSON.stringify(data);
}
