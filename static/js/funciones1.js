function validaciones(ususario, token, dominio){

    // console.log("validando...");

    // obtenemos los valores de los campos de texto
    var pass1 = document.getElementById("pass1").value;
    var pass2 = document.getElementById("pass2").value;

    // si pass1 y pass2 no tienen datos
    if(pass1 == "" || pass2 == ""){

        // sweet alert
        swal({
            title: 'Contraseña inválida',
            text: 'Asegurate de escribir una contraseña.',
            icon: 'error',

            buttons: {
                Ok: 'Ok'

            },
        })

        return false;
    }
    // si pass1 y pass2 no coinciden
    if(pass1 != pass2){

        // sweet alert
        swal({
            title: 'Contraseña inválida',
            text: 'Asegurate de escribir bien ambas contraseñas.',
            icon: 'error',

            buttons: {
                Ok: 'Ok'

            },
        })

        return false;
    }
    // si pass1 y pass2 tienen al menos 8 caracteres
    if(pass1.length < 8){

        // sweet alert
        swal({
            title: 'Contraseña inválida',
            text: 'Asegurate de escribir una contraseña más segura. La contraseña debe tener al menos 8 caracteres.',
            icon: 'warning',

            buttons: {
                Ok: 'Ok'

            },
        })

        return false;
    }
    
    // si pass1 y pass2 tienen al menos un caracter especial y un número
    if(pass1.match(/([!,%,&,@,#,$,^,*,_,~])/) && pass1.match(/([0-9])/)){

        // sweet alert
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

                    // imprime la contraseña
                    // console.log(pass1);

                    // encripta la contraseña
                    pass1 = encriptar(pass1);

                    // imprime la contraseña encriptada
                    // console.log(pass1);

                    // crea una variable con la url y usuario y pass1 separados un "/"
                    var url = dominio + "/cambiar_contrasena/" + ususario + "/" + token + "/" + pass1;

                    // imprime url
                    // console.log(url);
                    window.location.href = url;

                    break;
            }
        });

        return true;

        // si no tiene al menos un caracter especial y un número
    }else{

        // sweet alert
        swal({
            title: 'Contraseña poco segura',
            text: 'Asegurate de escribir una contraseña más segura. La contraseña debe tener al menos un caracter especial (!,%,&,@,#,$,^,*,_,~) y un número.',
            icon: 'warning',

            buttons: {
                Ok: 'Ok'

            },
        })

        // alert("La contraseña debe tener al menos un caracter especial (!,%,&,@,#,$,^,*,?,_,~) y un número");
        return false;
    }
}

function buscar_usuario(usuarios, dominio){

    // console.log("buscando usuario...");

    // obtenemos el valor del campo de texto
    var usuario = document.getElementById("usuario").value;

    // imprime el valor del campo de texto
    // console.log(usuario);

    // convierte el string de usuarios en un array quitando los espacios y los caracteres [ , ] y comilla simple
    usuarios = usuarios.replace(/ /g, "").replace(/[\[\]']+/g,'').split(",");
    
    // si el usuario no está en el array de usuarios
    if(usuarios.indexOf(usuario) == -1){
        // sweet alert
        swal({
            title: 'Usuario inválido',
            text: 'Asegurate de escribir bien tu usuario.',
            icon: 'error',

            buttons: {
                Ok: 'Ok'

            },
        })
        .then((value) => {
            switch (value) {

                case "Ok":
                    // si el usuario da click en ok
                    // redirecciona a la pagina de inicio de sesion
                    var url = dominio + "/olvide_contrasena";
                    window.location.href = url;
                    // console.log(url);

                    break;
            }
        });

        return false;

    }else{
        // sweet alert
        swal({
            title: 'Confirmacion',
            text: 'Usuario encontrado. Se te enviara un correo con un link para cambiar tu contraseña.',
            icon: 'success',

            buttons: { 
                Ok: 'Ok'
            },
        })
        .then((value) => {

            switch (value) {

                case "Ok":
                    // si el usuario da click en ok
                    // url con el dominio la ruta "correo_recuperacion" y el usuario
                    var url = dominio + "/link_recuperacion/" + usuario;
                    window.location.href = url;
                    // console.log(url);

                    break;
            }
        });

        return true;
    }

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



