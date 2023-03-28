#! /bin/bash

# mensaje de inicio
echo "Iniciando carga.sh"

# ciclo for para 100 iteraciones
for i in {1..10000}
do 
    # con el comando curl hacer una petición a la url cegmex.ddns.net:8000 y no mostrar la salida
    curl -s cegmex.ddns.net:8000
done

# mensaje de finalización
echo "Finalizando carga.sh"