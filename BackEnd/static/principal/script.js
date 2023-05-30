function openTab(event, tabName) {
    // Oculta todos los elementos con la clase "tabcontent"
    var tabcontent = document.getElementsByClassName("tabcontent");
    for (var i = 0; i < tabcontent.length; i++) {
      tabcontent[i].style.display = "none";
    }
  
    // Elimina la clase "active" de todos los elementos con la clase "tablinks"
    var tablinks = document.getElementsByTagName("a");
    for (var i = 0; i < tablinks.length; i++) {
      tablinks[i].classList.remove("active");
    }
  
    // Muestra el contenido de la pestaña seleccionada y marca el enlace como activo
    document.getElementById(tabName).style.display = "block";
    event.currentTarget.classList.add("active");
  }
  
  function togglePower(event, appliance) {
    var isChecked = event.target.checked;
  
    // Aquí iría la lógica para encender o apagar el aparato seleccionado
    if (isChecked) {
      console.log(`El aparato '${appliance}' ha sido encendido.`);
    } else {
      console.log(`El aparato '${appliance}' ha sido apagado.`);
    }
  }
  
  