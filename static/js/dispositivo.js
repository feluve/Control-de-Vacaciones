window.addEventListener("load", (event) => {
    console.log("Dispositivo");

    validar_dispositivo();

});

// funcion que valida si esta registrado el dispositivo
function validar_dispositivo() {

    const usuario = "admin"
    const usuarioR = localStorage.getItem("usuarioR");
    console.log(usuarioR);

    if (usuarioR == null) {
        
        console.log("Dispositivo no registrado o huella borrada");
        
        return false;
    }
    // obtenemos el data-dispositivo del div con id div
    const dispositivo = document.getElementById("div").dataset.dispositivo;

    // si el usuarioR es igual a usuario
    if (usuarioR == usuario && dispositivo == "Registrado") {
        
        window.location.href = "/asistenciaQR";

        return true;
    }
}

function RegistrarDispositivo() {

    console.log("RegistrarDispositivo");

    // alerta personalizada
    swal({
        title: "¿Estas seguro?",
        text: "¿Deseas registrar este dispositivo?",
        icon: "warning",

        buttons: {
            No: "No",
            Si: "Si"
        },
    })

    .then((value) => {
        switch (value) {
            case "Si":
                console.log("Si");
                Setear("admin");

                const dominio = "127.0.0.1:8000/"

                window.location.href = "/registroDispositivo";
                break;

            default:
                console.log("Cancelar");
                break;
        }
    });

}

function Borrar() {
    localStorage.removeItem("usuarioR");
    alert("Dispositivo borrado");
}

function Setear(usuarioR) {
    localStorage.setItem("usuarioR", usuarioR);
    console.log("Dispositivo registrado");
}

function Consultar() {
    const usuarioR = localStorage.getItem("usuarioR");
    alert(usuarioR);
}