var loginSection = document.getElementById("login-section");
var registroSection = document.getElementById("registro-section");

function toggleRegistration() {
  if (loginSection.style.display === "none") {
    loginSection.style.display = "block";
    registroSection.style.display = "none";
  } else {
    loginSection.style.display = "none";
    registroSection.style.display = "block";
  }
}
