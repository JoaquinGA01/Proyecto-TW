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


async function iniciarSesion() {
  var user = document.getElementById('username').value;
  var pass = document.getElementById('password').value;
  const url = 'api/personas/getAll/';
  params = { email: user, password: pass };
  console.log(JSON.stringify(params));

  const response = await fetch('api/personas/getAll/', {
    method: 'POST',
    body: JSON.stringify(params),
    headers: {
      'Content-Type': 'application/json'
    }
  });

  const data = await response.text();
  document.open();
  document.write(data);
  document.close();
}

