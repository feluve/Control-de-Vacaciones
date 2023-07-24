window.addEventListener("load", (event) => {
    console.log("Dispositivo");

    // validar_dispositivo();

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
    console.log("Obteniendo datos digitales del dispositivo...");

    // obtenemos el data-user del id btn_registrar
    const usuario = document.getElementById("btn_registrar").dataset.user;

    // funcion para obtener los datos digitales del usuario
    const userAgent = navigator.userAgent;

    // nombre del dispositivo
    const regex = /\(([^)]+)\)/;
    const matches = regex.exec(userAgent);
    const nombre = matches[1];
    console.log("Nombre dispositivo: ", nombre);

    // tamaño de la pantalla
    const screenWidth = screen.width;
    const screenHeight = screen.height;
    const pantalla = screenWidth + " x " + screenHeight;
    console.log("Pantalla: ", pantalla);

    // plataforma
    const plataforma = navigator.platform;
    const agente = navigator.userAgent;
    console.log("Agente de usuario: ", agente);
    console.log("Plataforma: ", plataforma);

    // GPU
    const canvas = document.createElement('canvas');
    const gl = canvas.getContext('webgl');
    var gpu = "";
    if (gl) {
        const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
        const renderer = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL);
        gpu = renderer;
        console.log("GPU: ", gpu);
    } else {
        console.error('WebGL no está disponible en este dispositivo.');
    }

    // console.log("Agente de usuario: ", navigator.userAgent);
    // console.log("Idioma: ", navigator.language);
    // console.log("Plataforma: ", navigator.platform);
    // console.log("Cookies habilitadas: ", navigator.cookieEnabled);
    // console.log("En línea: ", navigator.onLine);
    // console.log("Puntos táctiles: ", navigator.maxTouchPoints);
    // console.log("Núcleos de CPU: ", navigator.hardwareConcurrency);

    const nucleos = navigator.hardwareConcurrency;
    console.log("Núcleos de CPU: ", nucleos);

    // localStorage.setItem('laazaz_id', '4587ff526d');
    // localStorage.getItem('laazaz_id'); //returns 4587ff526d

    // const memoryTotal = performance.memory.totalJSHeapSize / (1024 * 1024);
    // console.log("Memoria total: " + memoryTotal.toFixed(2) + " MB");
    // console.log(performance.memory);
    // console.log(navigator)

    // localStorage.setItem('usuario', 'admmin');

    // localStorage.getItem('usuario'); 

    // console.log(localStorage.getItem('usuario'));

    // obtener la direccion ip publica del cliente y guardarle en una variable global


    // alerta personalizada
    swal({
        title: "Confirmar",
        text: "¿Está seguro de registrar este dispositovo con el usuario " + usuario + "? Al confirmar solo podra registrar sus asistencia con este dispositivo.",
        icon: "success",

        buttons: {
            No: "No",
            Si: "Si"
        },
    })

    .then((value) => {
        switch (value) {
            case "Si":
                console.log("Si");

                Setear(usuario);

                url = "/registroDispositivo/" + pantalla + "/" + plataforma + "/" + nucleos;
                // eliminar de url todos los espacio en blanco y los carcaters especiales
                url = url.replace(/ /g, "");
                url = url.replace(/[(]/g, "");
                url = url.replace(/[)]/g, "");
                url = url.replace(/[,]/g, "");
                url = url.replace(/[:]/g, "");
                url = url.replace(/[;]/g, "");
                url = url.replace(/[.]/g, "");
                url = url.replace(/[-]/g, "");
                url = url.replace(/[_]/g, "");

                window.location.href = url
                break;

            default:
                console.log("Cancelar");
                break;
        }
    });

}

function Borrar() {
    localStorage.removeItem("usuarioR");
    alert("usuarioR borrado");
}

function Setear(usuarioR) {
    localStorage.setItem("usuarioR", usuarioR);
    // alert("usuarioR seteado a: " + usuarioR);
}

function Consultar() {
    const usuarioR = localStorage.getItem("usuarioR");
    alert("Consulta usuarioR: " + usuarioR);
}