#! /bin/bash

# ciclo while infinito
while true
do
    # con el comando top obtemer la cantidad de procesos con el nombre del comando python3
    c=$(top -b -n 1 | grep python3 | wc -l)

    # si la cantidad de procesos es igual a 0
    if [ $c -eq 0 ]
    then
        # obtener la fecha y hora
        fecha=$(date +"%a_%d_%b_%Y")

        echo "**********************************************************" |& tee -a /home/feluve/logs/server_$fecha.log
        echo "[-] Por alguna razon el servidor python3 se encuentra abjo" |& tee -a /home/feluve/logs/server_$fecha.log
        echo "**********************************************************" |& tee -a /home/feluve/logs/server_$fecha.log

        # inica el servidor
        echo "Iniciando servidor nuevamente..." |& tee -a /home/feluve/logs/server_$fecha.log

        # ejecutar el servidor
        python3 manage.py runserver 192.168.1.1:8000 |& tee -a /home/feluve/logs/server_$fecha.log

        # retrazar 10 segundos
        sleep 10
    fi

done

# matar el proceso llamada down.sh
kill $(ps aux | grep '[d]own.sh' | awk '{print $2}')

# matar el proceso llamada python3
kill $(ps aux | grep '[p]ython3' | awk '{print $2}')


# del comando uptime obtener load average
load=$(uptime | awk '{print $9,$10,$11}')


