window.addEventListener("load", (event) => {
    console.log("Cargando Nuevo usuario");

    // coloca la fecha actual en el campo de texto fecha_ingreso
    document.getElementById("fecha_ingreso").value = new Date().toISOString().slice(0, 10);

    // coloca la fecha de hace 18 años en el campo de texto fecha_nacimiento
    var fecha = new Date();
    fecha.setFullYear(fecha.getFullYear() - 18);
    document.getElementById("fecha_nacimiento").value = fecha.toISOString().slice(0, 10);

});

// listener del campo de texto usuario
document.getElementById("usuario").addEventListener("keyup", (event) => {

    // colocar el texto en minusculas
    event.target.value = event.target.value.toLowerCase();

    // eliminar los espacios en blanco
    event.target.value = event.target.value.replace(/ /g, "");

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

    // verifica cada 5 segundos si el usuario ya existe
    setTimeout(() => {
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
            })
            .then((value) => {
                switch (value) {
                    case "Ok":
                        // borramos el valor del campo de texto usuario
                        event.target.value = "";    

                        // borramos el valor de la etiqueta e_usuario
                        document.getElementById("e_usuario").innerHTML = "";

                        // ponemos el foco en el campo de texto usuario
                        document.getElementById("usuario").focus();
                        break;
                }
            });
        }
    }, 5000);

    // si hay mas de 3 caracteres
    if (event.target.value.length > 3) {
        //colo OK en la etiqueta e_usuario
        document.getElementById("e_usuario").innerHTML = "OK";
        document.getElementById("e_usuario").style.color = "green";
    }else {
        //colo OK en la etiqueta e_usuario
        document.getElementById("e_usuario").innerHTML = "";
    }

});

// listener del campo de texto nombre
document.getElementById("nombre").addEventListener("keyup", (event) => {
    // colocar la primera letra en mayuscula 
    event.target.value = event.target.value.replace(/^\w/, (c) => c.toUpperCase());

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

    // verfica cada 5 segundos si el nombre tiene espacios en blanco al final
    setTimeout(() => {
        // si el ultimo caracter es un espacio
        if (event.target.value.slice(-1) == " ") {
            // borramos el ultimo caracter
            event.target.value = event.target.value.slice(0, -1);
        }
    }, 5000);

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

// listener del campo de texto contraseña
document.getElementById("contrasena").addEventListener("keyup", (event) => {
    // si hay mas de 1 caracteres
    if (event.target.value.length >= 1) {
        //colo OK en la etiqueta e_contrasena
        document.getElementById("e_contrasena").innerHTML = "OK";
        document.getElementById("e_contrasena").style.color = "green";
    } else {
        //colo OK en la etiqueta e_contrasena
        document.getElementById("e_contrasena").innerHTML = "";
    }

});



// listener del campo de texto email
document.getElementById("correo").addEventListener("keyup", (event) => {
    // colocar el texto en minusculas
    event.target.value = event.target.value.toLowerCase();
    // validar que el email tenga el formato correcto

    // borramos el ultimo caracter si es un espacio
    if (event.target.value.slice(-1) == " ") {
        // borramos el ultimo caracter
        event.target.value = event.target.value.slice(0, -1);
    }

    // verfica cada 5 segundos si el nombre tiene espacios en blanco al final
    setTimeout(() => {
        // valida que el email al menos tenga un @ y un .
        if (!(event.target.value.includes("@") && event.target.value.includes("."))) {
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
                switch (value) {
                    case "Ok":
                        // borramos el valor del campo de texto email
                        event.target.value = "";
                        // ponemos el foco en el campo de texto email
                        document.getElementById("correo").focus();
                        break;
                }
            });
        }
    }, 10000);

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

});


function guardar_usuario(){
    console.log("Nuevo usuario");

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
                console.log('Se envio la solictud');
                break;
            case "No":
                swal("Cancelado", "No se creo el usuario", "error");
                break;
        }
    });

}

