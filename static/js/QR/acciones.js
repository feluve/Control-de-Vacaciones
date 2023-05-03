
// listener wind
window.addEventListener('load', function() {
    console.log("Cargando acciones QR...");

    obtenerDatosDigitales();

});

// funcion para obtener los datos digitales del usuario
function obtenerDatosDigitales() {
    const userAgent = navigator.userAgent;

    // nombre del dispositivo
    const regex = /\(([^)]+)\)/;
    const matches = regex.exec(userAgent);
    const nombre_dispositivo = matches[1];
    console.log("Nombre dispositivo: ", nombre_dispositivo);

    // tamaño de la pantalla
    const screenWidth = screen.width;
    const screenHeight = screen.height;
    const pantalla = screenWidth + " x " + screenHeight;
    console.log("Pantalla: ", pantalla);

    // plataforma
    const platform = navigator.platform;
    const useragent = navigator.userAgent;
    console.log("Agente de usuario: ", useragent);
    console.log("Plataforma: ", platform);

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

    alert(
        nombre_dispositivo + "\n" +
        platform + "\n" +
        useragent + "\n" +
        pantalla + "\n" +
        gpu + "\n"+
        nucleos + "\n"
    );

};

// obtenemos el data-dominio de id resultado
var dominio = document.getElementById("resultado").dataset.dominio;

function onScanSuccess(qrCodeMessage) {
    
    // colocar en el input el valor del QR
    document.getElementById("resultado").innerHTML = qrCodeMessage;

    console.log(qrCodeMessage);

    // registramos asistencia
    // nos vamos a la url 
    window.location.href = dominio + "/registroAsistenciaQR/" + qrCodeMessage;

}

function onScanError(errorMessage) {
    //handle scan error
}

var html5QrcodeScanner = new Html5QrcodeScanner("reader", { fps: 10, qrbox: 250 });
html5QrcodeScanner.render(onScanSuccess, onScanError);
