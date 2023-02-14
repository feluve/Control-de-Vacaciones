
function resta_dias(){

    if (parseInt(document.getElementById('dias_sol').value) > 1) {
        document.getElementById('dias_sol').value = parseInt(document.getElementById('dias_sol').value) -1;
        console.log("Restamos");
    }
}

function suma_dias(){
    
    if (parseInt(document.getElementById('dias_sol').value) < 6) {
        document.getElementById('dias_sol').value = parseInt(document.getElementById('dias_sol').value) +1;
        console.log("Sumamos");
    }
}

function verifica_domingo(fecha){
    const fecha1 = new Date(fecha);

    console.log("Dia de la semana: " + fecha1.getDay())

    if(fecha1.getDay() === 6){
        console.log("Es domingo")  
        return true
    }
    else{
        console.log("No es domingo")
        return false
    }

}

function validacion(){

    console.log("Verificando fecha ....");

    const dias_disp = parseInt(document.getElementById('dias_disp').innerText);
    const dias_sol = parseInt(document.getElementById('dias_sol').value);
    const fecha_sol = new Date(document.getElementById('fecha_sol').value);
    const fecha_sol_str = document.getElementById('fecha_sol').value;

    const solicitudes_pendientes = 0

    const fecha_actual = new Date();
    const diffTime = (fecha_sol - fecha_actual);
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24)); 

    console.log("Diferencia de dias: " + diffDays)


    // Validadmos que tenga una fecha seleccionada
    if(fecha_sol_str.length == 0){
        // console.log("fecha nula")

        swal({
            title: 'Información',
            text: 'Debe seleccionar una fecha.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que la fecha seleccionado no sea menos a la fecha actual
    else if(diffDays < 15){

        swal({
            title: 'Fecha invalida',
            text: 'La fecha seleccionada debe ser mayor a la fecha actual y 15 dias de acticipacion.',
            icon: 'error',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    // Validamos que no tenga solicitudes pendinetes
    else if (solicitudes_pendientes > 0){

        swal({
            title: 'Información',
            text: 'No puede hacer más solicitudes ya que tiene una pendiente por autorizar.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    //Validamos que tiene dias disponibles suficientes
    else if(dias_sol > dias_disp ){

        swal({
            title: 'Información',
            text: 'Estas solicitando ' + dias_sol +' dia(s) y solo cuentas con ' + dias_disp + ' dia(s) disponibles.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    //Validamos que la fecha seleccionado no se adomingo
    else if (verifica_domingo(fecha_sol)){

        swal({
            title: 'Información',
            // text: 'La fecha '+ document.getElementById('fecha_sol').value +' seleccionada es Domingo. Selecciona una fecha diferente.',
            text: 'La fecha seleccionada es Domingo. Selecciona una fecha diferente.',
            icon: 'warning',
    
            buttons: {
                OK: "OK"
            },
        })

    }
    //Confimamos el envio de la solicitud
    else{

        // const fecha_format = fecha_sol.getDay + "-" + fecha_sol.getMonth + "-" + fecha_sol.getFullYear

        swal({
            title: 'Confirmación',
            text: 'Esta seguro de enviar la solicitud por '+ dias_sol +' dia(s) en la fecha ' + fecha_sol_str + ' ?',
            icon: 'success',
    
            buttons: {
                No: "No",
                Si: "Si"
            },
        })

        .then((value) => {
            switch (value) {

                case "Si":
                    document.getElementById('form').submit();
                    console.log('Se envio la solictud');

                    // swal({
                    //     title: 'Confirmación',
                    //     text: 'Solicitud envida correctamente.',
                    //     icon: 'success',
                    //     buttons: 'OK'
                    // })

                    break;

                case "No":
                    console.log('No se enevio la solitud');
                    break;

            }
        })

    }
}

function post(){

    console.log(document.getElementById('token').innerText)

    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/registra_solicitud/", true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        fecha_sol: '2023-01-01',
        dias_sol: 6
    }));


    xhr.onload = function() {
    console.log("Hola")
    console.log(this.responseText);
    var data = JSON.parse(this.responseText);
    console.log(data);
    }

}
