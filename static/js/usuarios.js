window.addEventListener("load", (event) => {
    console.log("Pagina usuarios cargada completamente.");

    // coloca la fecha actual en el campo de texto fecha_ingreso
    document.getElementById("fecha_ingreso").value = new Date().toISOString().slice(0, 10);

    // colocamos la fecha 1990-01-01 en el campo de texto fecha_nacimiento
    document.getElementById("fecha_nacimiento").value = "1990-01-01";

    // obtenemos el atributo data-jefes del campo de texto jefe
    var jefes = document.getElementById("jefe").getAttribute("data-jefes");
    // convertimos a un array el string de jefes
    jefes = jefes.replace(/'/g, "").replace("[", "").replace("]", "").split(",");

    // agregamos la opcion de seleccionar jefe del array de jefes
    for (var i = 0; i < jefes.length; i++) {
        var option = document.createElement("option");
        option.text = jefes[i];
        option.value = jefes[i];
        document.getElementById("jefe").add(option);
    }

    // obtenemos el atributo data-roles del campo de texto rol
    var roles = document.getElementById("rol").getAttribute("data-roles");
    // convertimos a un array el string de roles
    roles = roles.replace(/'/g, "").replace("[", "").replace("]", "").split(",");

    // agregamos la opcion de seleccionar rol del array de roles
    for (var i = 0; i < roles.length; i++) {
        var option = document.createElement("option");
        option.text = roles[i];
        option.value = roles[i];
        document.getElementById("rol").add(option);
    }

    // obtenemos el atributo data-areas del campo de texto area
    var areas = document.getElementById("area").getAttribute("data-areas");
    // convertimos a un array el string de areas
    areas = areas.replace(/'/g, "").replace("[", "").replace("]", "").split(",");

    // agregamos la opcion de seleccionar area del array de areas
    for (var i = 0; i < areas.length; i++) {
        var option = document.createElement("option");
        option.text = areas[i];
        option.value = areas[i];
        document.getElementById("area").add(option);
    }

    // obtenemos el atributo data-semana del campo de texto semana
    var semanas = document.getElementById("semana").getAttribute("data-semana");
    // convertimos a un array el string de semanas
    semanas = semanas.replace(/'/g, "").replace("[", "").replace("]", "").split(",");

    // agregamos la opcion de seleccionar semana del array de semanas
    for (var i = 0; i < semanas.length; i++) {
        var option = document.createElement("option");
        option.text = semanas[i];
        option.value = semanas[i];
        document.getElementById("semana").add(option);
    }

});

function previewImage() {
    
    // print("previewImage");

    var file = document.getElementById("imagen").files
    if (file.length > 0) {
        var fileReader = new FileReader()

        fileReader.onload = function (event) {
            document.getElementById("preview").setAttribute("src", event.target.result)
        }

        fileReader.readAsDataURL(file[0])
    }
}

// listener del campo de texto usuario
document.getElementById("usuario").addEventListener("keyup", (event) => {

    // colocar el texto en minusculas
    event.target.value = event.target.value.toLowerCase();

    // eliminar los espacios en blanco
    event.target.value = event.target.value.replace(/ /g, "");

    // eliminar los acentos
    event.target.value = event.target.value.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

});

// listener del campo de texto usuario unfocus
document.getElementById("usuario").addEventListener("blur", (event) => {

    // obtenemos el atributo data- del campo de texto usuario
    var usuarios = document.getElementById("usuario").getAttribute("data-usuarios");

    // imprimimos el valor del atributo data-usuario
    // console.log("usuarios: " + usuarios);

    // convertimos el string de usuarios en un array elimando los espacios en blanco los caracteres comilla simple [ y ]
    usuarios = usuarios.replace(/ /g, "").replace(/'/g, "").replace("[", "").replace("]", "").split(",");
    
    // imprimimos el array de usuarios
    // for (var i = 0; i < usuarios.length; i++) {
    //     console.log("usuario: " + usuarios[i]);
    // }

    // si el usuario ya existe
    if (usuarios.includes(event.target.value)) {
        // mostramos alerta de error
        swal({
            title: "Información",
            text: "El usuario "+ event.target.value +" ya existe! Coloque otro nombre de usuario.",
            icon: "info",

            buttons: {
                Ok: "Ok",
            },    
        });

        // borramos el valor del campo de texto usuario
        event.target.value = "";    

        // borramos el valor de la etiqueta e_usuario
        document.getElementById("e_usuario").innerHTML = "";

        // ponemos el foco en el campo de texto usuario
        document.getElementById("usuario").focus();

    } 
    // si el usuario es null
    else if (event.target.value == "") {

        // colocamos el texto requerido en el campo de texto usuario
        document.getElementById("usuario").placeholder = "Requerido";

        // mostramos alerta de error
        swal({
            title: "Información",
            text: "El usuario no puede ser un valor vacio! Coloque un nombre de usuario valido.",
            icon: "info",

            buttons: {
                Ok: "Ok",
            },
        })
        .then((value) => {
            // borramos el valor del campo de texto usuario
            event.target.value = "";    

            // borramos el valor de la etiqueta e_usuario
            document.getElementById("e_usuario").innerHTML = "";

            // ponemos el foco en el campo de texto usuario
            document.getElementById("usuario").focus();
        });
    }
    else {
        //colo OK en la etiqueta e_usuario
        document.getElementById("e_usuario").innerHTML = "OK";
        document.getElementById("e_usuario").style.color = "green";
    }

});

// listener del campo de texto nombre
document.getElementById("nombre").addEventListener("keyup", (event) => {
    // colocar la primera letra en mayuscula 
    event.target.value = event.target.value.replace(/^\w/, (c) => c.toUpperCase());

    // eliminar los acentos
    event.target.value = event.target.value.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

    // si se captura un espacio en blanco
    if (event.target.value.slice(-1) == " ") {
        // borramos el ultimo caracter
        event.target.value = event.target.value.slice(0, -1);
    }

    // si hay mas de 3 caracteres
    if (event.target.value.length > 3) {
        //colo OK en la etiqueta e_nombre
        document.getElementById("e_nombre").innerHTML = "OK";
        document.getElementById("e_nombre").style.color = "green";
    } else {
        //colo OK en la etiqueta e_nombre
        document.getElementById("e_nombre").innerHTML = "";
    }   

});

// listener del campo de texto apellidos
document.getElementById("apellidos").addEventListener("keyup", (event) => {
    // colocar la primera letra en mayuscula y despues de cada espacio
    event.target.value = event.target.value.replace(/\w\S*/g, (w) => (w.replace(/^\w/, (c) => c.toUpperCase())));

    // eliminar los acentos
    event.target.value = event.target.value.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

    // si hay mas de 3 caracteres
    if (event.target.value.length > 3) {
        //colo OK en la etiqueta e_apellidos
        document.getElementById("e_apellidos").innerHTML = "OK";
        document.getElementById("e_apellidos").style.color = "green";
    } else {
        //colo OK en la etiqueta e_apellidos
        document.getElementById("e_apellidos").innerHTML = "";
    }

});

// listener del campo de texto apellidos unfocus

document.getElementById("apellidos").addEventListener("blur", (event) => {

    // si el ultimo caracter es un espacio
    if (event.target.value.slice(-1) == " ") {
        // borramos el ultimo caracter
        event.target.value = event.target.value.slice(0, -1);
    }
});

// listener del campo de texto contraseña
// document.getElementById("contrasena").addEventListener("keyup", (event) => {
//     // si hay mas de 8 caracteres
//     if (event.target.value.length >= 8) {
//         //colo OK en la etiqueta e_contrasena
//         document.getElementById("e_contrasena").innerHTML = "OK";
//         document.getElementById("e_contrasena").style.color = "green";
//     } else {
//         //colo OK en la etiqueta e_contrasena
//         document.getElementById("e_contrasena").innerHTML = "";
//     }
// });

// listener del campo de texto contraseña unfocus
// document.getElementById("contrasena").addEventListener("blur", (event) => {
//     // si no hay mas de 8 caracteres
//     if (event.target.value.length < 8) {
//         // mostramos alerta de error

//         swal({
//             title: "Información",
//             text: "La contraseña debe tener al menos 8 caracteres!",
//             icon: "info",

//             buttons: {
//                 Ok: "Ok",
//             },
//         })
//         .then((value) => {
//             // coloca el foco en el campo de texto contraseña
//             document.getElementById("contrasena").focus();
                
//             // borramos el valor del campo de texto contraseña
//             event.target.value = "";
//         });
//     }
// });

// listener del campo de texto email
document.getElementById("correo").addEventListener("keyup", (event) => {
    // colocar el texto en minusculas
    event.target.value = event.target.value.toLowerCase();
    // validar que el email tenga el formato correcto

    // eliminar los acentos
    event.target.value = event.target.value.normalize("NFD").replace(/[\u0300-\u036f]/g, "");

    // borramos el ultimo caracter si es un espacio
    if (event.target.value.slice(-1) == " ") {
        // borramos el ultimo caracter
        event.target.value = event.target.value.slice(0, -1);
    }

});

// listener del campo de texto email unfocus
document.getElementById("correo").addEventListener("blur", (event) => {

    // Define our regular expression.
    var validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;

    // si el email no tiene el formato correcto y el campo no esta vacio
    if (!validEmail.test(event.target.value)) {
        // mostramos alerta de error
        swal({
            title: "Información",
            text: "El email "+ event.target.value +" no tiene el formato correcto! Coloque un email valido.",
            icon: "info",

            buttons: {
                Ok: "Ok",
            },
        })
        .then((value) => {
            // borrando el valor del campo de texto email
            event.target.value = "";
            // ponemos el foco en el campo de texto email
            document.getElementById("correo").focus();
        });
    }
    else {
        //colo OK en la etiqueta e_correo
        document.getElementById("e_correo").innerHTML = "OK";
        document.getElementById("e_correo").style.color = "green";
    }

});

// listener del campo de texto telefono que solo acepta numeros y como maximo 10 caracteres
document.getElementById("telefono").addEventListener("keyup", (event) => {

    // si el telefono no es un numero
    if (isNaN(event.target.value)) {
        // borramos el ultimo caracter
        event.target.value = event.target.value.slice(0, -1);
    }

    // si el telefono tiene mas de 10 caracteres
    if (event.target.value.length > 10) {
        // borramos el ultimo caracter
        event.target.value = event.target.value.slice(0, -1);
    } 

    // si el telefono tiene mas 10 caracteres
    if (event.target.value.length == 10) {
        // coloco OK en la etiqueta e_telefono
        document.getElementById("e_telefono").innerHTML = "OK";
        document.getElementById("e_telefono").style.color = "green";
    } else {
        // coloco OK en la etiqueta e_telefono
        document.getElementById("e_telefono").innerHTML = "";
    }

});

function guardar_usuario(){
    console.log("Guardando nuevo usuario...");

    // validamos que e_usuario tenga un valor OK
    if (document.getElementById("e_usuario").innerHTML != "OK") {
        // nos concentramos en el campo de texto usuario
        document.getElementById("usuario").focus();
        return false;
    }

    // validamos que e_nombre tenga un valor OK
    if (document.getElementById("e_nombre").innerHTML != "OK") {
        // nos concentramos en el campo de texto nombres
        document.getElementById("nombre").focus();
        return false;
    }

    // validamos que e_apellidos tenga un valor OK
    if (document.getElementById("e_apellidos").innerHTML != "OK") {
        // nos concentramos en el campo de texto apellidos
        document.getElementById("apellidos").focus();
        return false;
    }

    // validamos que e_correro tenga un valor OK
    if (document.getElementById("e_correo").innerHTML != "OK") {
        // nos concentramos en el campo de texto correo
        document.getElementById("correo").focus();
        return false;
    }

    // validamos que e_telefono tenga un valor OK
    if (document.getElementById("e_telefono").innerHTML != "OK") {
        // nos concentramos en el campo de texto telefono
        document.getElementById("telefono").focus();
        return false;
    }

    // validamos que la fecha de nacimiento no sea mayor a la fecha de ingreso
    if (document.getElementById("fecha_nacimiento").value > document.getElementById("fecha_ingreso").value) {
        // mostramos alerta de error
        swal({
            title: "Información",
            text: "La fecha de nacimiento no puede ser mayor a la fecha de ingreso!",
            icon: "info",

            buttons: {
                Ok: "Ok",
            },
        })

        // nos concentramos en el campo de texto fecha_ingreso
        document.getElementById("fecha_ingreso").focus();
        return false;
    }
    
    // mostramos una alerta de confirmacion
    swal({
        title: "Confirmación",
        text: "¿Está seguro de crear el usuario?",
        icon: "success",

        buttons: {
            No: "No",
            Si: "Si",
        },
    })
    .then((value) => {
        switch (value) {
            case "Si":
                document.getElementById('form').submit();
                console.log('Se envio la solictud para crear el usuario');
                break;
            case "No":
                // swal("Cancelado", "No se creo el usuario", "error");
                break;
        }
    });

}