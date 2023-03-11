window.addEventListener("load", (event) => {
    console.log("Cargando contraseña nueva");

    inicializar();

});

// funcion que inicializa los estados de la etiquetas
function inicializar() {
    // la etiqueta e_caracteres le colocamos un Requerido
    document.getElementById("e_caracteres").innerHTML = "Requerido";
    // la etiqueta e_caracteres le colocamos un color rojo
    document.getElementById("e_caracteres").style.color = "red";

    // la etiqueta e_numero le colocamos un Requerido
    document.getElementById("e_numero").innerHTML = "Requerido";
    // la etiqueta e_numero le colocamos un color rojo
    document.getElementById("e_numero").style.color = "red";

    // la etiqueta e_mayuscula le colocamos un Requerido
    document.getElementById("e_mayuscula").innerHTML = "Requerido";
    // la etiqueta e_mayuscula le colocamos un color rojo
    document.getElementById("e_mayuscula").style.color = "red";

    // la etiqueta e_caracter_esp le colocamos un Requerido
    document.getElementById("e_caracter_esp").innerHTML = "Requerido";
    // la etiqueta e_caracter_esp le colocamos un color rojo
    document.getElementById("e_caracter_esp").style.color = "red";

    // la etiqueta e_confirmar le colocamos un Requerido
    document.getElementById("e_confirmar").innerHTML = "Requerido";
    // la etiqueta e_confirmar le colocamos un color rojo
    document.getElementById("e_confirmar").style.color = "red";

}

// listener del campo de texto contrasena1
document.getElementById("contrasena1").addEventListener("keyup", (event) => {
    
    // eliminamos los espacios en blanco
    event.target.value = event.target.value.replace(/ /g, "");


    // si el campo de texto contrasena1 tiene caracteres diferntes a letras, numeros y los caracteres !, %, &, @, #, $, ^, *, _, ~
    if (event.target.value.match(/[^a-zA-Z0-9!,%,&,@,#,$,^,*,_,~]/)) {
        // borramos el ultimo caracter
        event.target.value = event.target.value.slice(0, -1);
    }

    // si el campo de texto pass1 tiene al menos 8 caracteres
    if (event.target.value.length >= 8) {
        //colo OK en la etiqueta e_pass1
        document.getElementById("e_caracteres").innerHTML = "OK";
        document.getElementById("e_caracteres").style.color = "green";
    }
    else {
        //colo Requerido en la etiqueta e_caracteres
        document.getElementById("e_caracteres").innerHTML = "Requerido";
        document.getElementById("e_caracteres").style.color = "red";
    }

    // si el campo de texto pass1 tiene al menos un caracter especial
    if (event.target.value.match(/([!,%,&,@,#,$,^,*,_,~])/)) {
        //colo OK en la etiqueta e_caracter_esp
        document.getElementById("e_caracter_esp").innerHTML = "OK";
        document.getElementById("e_caracter_esp").style.color = "green";
    } 
    else {
        //colo Requerido en la etiqueta e_caracter_esp
        document.getElementById("e_caracter_esp").innerHTML = "Requerido";
        document.getElementById("e_caracter_esp").style.color = "red";
    }

    // si el campo de texto pass1 tiene al menos una letra mayuscula
    if (event.target.value.match(/([A-Z])/)) {
        //colo OK en la etiqueta e_mayuscula
        document.getElementById("e_mayuscula").innerHTML = "OK";
        document.getElementById("e_mayuscula").style.color = "green";
    }
    else {
        //colo Requerido en la etiqueta e_mayuscula
        document.getElementById("e_mayuscula").innerHTML = "Requerido";
        document.getElementById("e_mayuscula").style.color = "red";
    }

    // si el campo de texto pass1 tiene al menos un numero
    if (event.target.value.match(/([0-9])/)) {
        //colo OK en la etiqueta e_numero
        document.getElementById("e_numero").innerHTML = "OK";
        document.getElementById("e_numero").style.color = "green";
    }
    else {
        //colo Requerido en la etiqueta e_numero
        document.getElementById("e_numero").innerHTML = "Requerido";
        document.getElementById("e_numero").style.color = "red";
    }   

});

// listener del campo de texto contrasena2
document.getElementById("contrasena2").addEventListener("keyup", (event) => {
    // eliminamos los espacios en blanco
    event.target.value = event.target.value.replace(/ /g, "");

    // elimina los caracteres ? y /
    event.target.value = event.target.value.replace(/[\?\/]/g, "");

    // si el campo de texto pass2 es igual al campo de texto pass1
    if (event.target.value == document.getElementById("contrasena1").value) {
        // coloca OK en la etiqueta e_confirmar
        document.getElementById("e_confirmar").innerHTML = "OK";
        document.getElementById("e_confirmar").style.color = "green";
    }
    else {
        // coloca Requerido en la etiqueta e_confirmar
        document.getElementById("e_confirmar").innerHTML = "Requerido";
        document.getElementById("e_confirmar").style.color = "red";
    }

});

function confirmar_contrasena(ususario, token, dominio){

    // si el texto de la etiqueta e_caracteres es no es igual a OK
    if (document.getElementById("e_caracteres").innerHTML != "OK") {
        // sweet alert
        swal({
            title: 'Contraseña inválida',
            text: 'Asegurate de escribir una contraseña con al menos 8 caracteres.',
            icon: 'error',

            buttons: {
                Ok: 'Ok'
            },
        })

        // borra el campo de texto contrasena1
        document.getElementById("contrasena1").value = "";
        // borra el campo de texto contrasena2
        document.getElementById("contrasena2").value = "";

       inicializar();

        // enfoca el campo de texto contrasena1
        document.getElementById("contrasena1").focus();

        return false;
    }

    // si el texto de la etiqueta e_numero es no es igual a OK
    if (document.getElementById("e_numero").innerHTML != "OK") {
        // sweet alert
        swal({
            title: 'Contraseña inválida',
            text: 'Asegurate de escribir una contraseña con al menos un número.',
            icon: 'error',

            buttons: {
                Ok: 'Ok'
            },
        })

        // borra el campo de texto contrasena1
        document.getElementById("contrasena1").value = "";
        // borra el campo de texto contrasena2
        document.getElementById("contrasena2").value = "";

        inicializar();

        return false;
    }

    // si el texto de la etiqueta e_mayuscula es no es igual a OK
    if (document.getElementById("e_mayuscula").innerHTML != "OK") {
        // sweet alert
        swal({
            title: 'Contraseña inválida',
            text: 'Asegurate de escribir una contraseña con al menos una letra mayúscula.',
            icon: 'error',
            
            buttons: {
                Ok: 'Ok'
            },
        })

        // borra el campo de texto contrasena1
        document.getElementById("contrasena1").value = "";
        // borra el campo de texto contrasena2
        document.getElementById("contrasena2").value = "";
        // enfoca el campo de texto contrasena1
        document.getElementById("contrasena1").focus();

        inicializar();

        return false;
    }

    // si el texto de la etiqueta e_caracter_esp es no es igual a OK
    if (document.getElementById("e_caracter_esp").innerHTML != "OK") {
        // sweet alert
        swal({
            title: 'Contraseña inválida',
            text: 'Asegurate de escribir una contraseña con al menos un caracter especial.',
            icon: 'error',
            
            buttons: {
                Ok: 'Ok'
            },
        })

        // borra el campo de texto contrasena1
        document.getElementById("contrasena1").value = "";
        // borra el campo de texto contrasena2
        document.getElementById("contrasena2").value = "";
        // enfoca el campo de texto contrasena1
        document.getElementById("contrasena1").focus();

        inicializar();

        return false;
    }

    // si el texto de la etiqueta e_confirmar es no es igual a OK
    if (document.getElementById("e_confirmar").innerHTML != "OK") {
        // sweet alert
        swal({
            title: 'Contraseña inválida',
            text: 'Asegurate de escribir la misma contraseña en ambos campos.',
            icon: 'error',
            
            buttons: {
                Ok: 'Ok'
            },
        })

        // borra el campo de texto contrasena2
        document.getElementById("contrasena2").value = "";
        // enfoca el campo de texto contrasena2
        document.getElementById("contrasena2").focus();

        return false;
    }
    

    // si el campo de texto contrasena1 es igual al campo de texto contrasena2
    if (document.getElementById("contrasena1").value == document.getElementById("contrasena2").value) {
        // alerta de confirmación
        swal({
            title: 'Confirmación',
            text: 'La contraseña será cambiada. Se te enviara un correo de confirmación.',
            icon: 'success',

            buttons: {
                Ok: 'Ok'
            },
        })
        .then((value) => {
            switch (value) {
                case "Ok":

                    // obtenemos los valores de los campos de texto
                    var contrasena1 = document.getElementById("contrasena1").value;

                    // encripta la contraseña
                    contrasena1 = encriptar(contrasena1);

                    // imprime la contraseña encriptada
                    // console.log(contrasena1);

                    // crea una variable con la url y usuario y pass1 separados un "/"
                    var url = dominio + "/cambiar_contrasena/" + ususario + "/" + token + "/" + contrasena1;

                    // imprime url
                    // console.log(url);
                    window.location.href = url;

                    break;
            }
        });
}

// funcion que encritpa la contraseña sumando 3 a cada caracter
function encriptar(pass){
    
        // crea una variable que contendra la contraseña encriptada
        var pass_encriptada = "";
    
        // recorre cada caracter de la contraseña
        for(var i = 0; i < pass.length; i++){
    
            // obtiene el codigo ascii del caracter
            var ascii = pass.charCodeAt(i);
    
            // suma 3 al codigo ascii
            ascii += 3;
    
            // convierte el codigo ascii a caracter
            var caracter = String.fromCharCode(ascii);
    
            // concatena el caracter encriptado a la variable pass_encriptada
            pass_encriptada += caracter;
        }

        // imprime la contraseña encriptada
        // console.log(pass_encriptada);

        // convierte la contraseña encriptada a base64
        // pass_encriptada = btoa(pass_encriptada);

        // imprime la contraseña encriptada en base64
        // console.log(pass_encriptada);
    
        // retorna la contraseña encriptada
        return pass_encriptada;
}


}
