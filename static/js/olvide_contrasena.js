window.addEventListener("load", (event) => {
    console.log("Pagina olvide contraseña cargada completamente.");

});

function buscar_usuario(usuarios, dominio){

    console.log("Buscando usuario");

    // obtenemos el valor del campo de texto
    var usuario = document.getElementById("usuario").value;

    // imprime el valor del campo de texto
    console.log(usuario);

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
