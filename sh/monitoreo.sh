#! /bin/bash

# crea un script para ejecutar el servidor
# ciclo infinito
while true
do
    sleep 10

    # obtener la temperatura
    temp=$(vcgencmd measure_temp | cut -d '=' -f 2 | cut -d "'" -f 1)

    # obtenermo la hora
    hora=$(date +"%H:%M:%S")

    # fecha
    fecha=$(date +"%a_%d_%b_%Y") 

    # obtener del comando free -h solo la memoria usada
    memoria=$(free -h | grep Mem | awk '{print$2,$3}')

    # del comando df -h obtener el espacio total y el espacio usado
    disco=$( df -h | grep root | awk '{print $2,$3}' )

    # obtenemos del comando uptime la carga del sistema
    load=$(uptime | awk '{print $9,$10,$11}')

    # guradamos la temperatura en un archivo
    echo "$fecha $hora $temp'C $memoria $disco $load " |& tee -a /home/feluve/logs/monitor_$fecha.log
done