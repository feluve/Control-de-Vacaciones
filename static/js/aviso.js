
// crear listener para el evento load

window.addEventListener("load", function() {

    // obtener el texto de la etiqueta parrafo con id aviso
    var aviso = document.getElementById("aviso").innerHTML;

    // la variable aviso reemplazar los caracters _ por espacios
    aviso = aviso.replace(/_/g, " ");

    // mostrar la variable aviso en aviso
    document.getElementById("aviso").innerHTML = aviso;

    // console.log("aviso.js ejecutado");

});