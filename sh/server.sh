#! /bin/bash
# crea un script para ejecutar el servidor

sleep 30

# obtener la ip de la wlan0
ipWlan0=$(ifconfig wlan0 | grep "inet " | cut -d' ' -f10)
# ontenemos la ip de la eth0
ipEth0=$(ifconfig eth0 | grep "inet " | cut -d' ' -f10)

# en un ciclo infinito si la ip es diferente de 192.168.1.2 o la ipEth0 es diferente de 192.168.1.1
#while [ "$ipWlan0" != "192.168.1.2" ] && [ "$ipEth0" != "192.168.1.1" ]
#do
    # esperamos 1 segundos
#    sleep 1
    # obtener la ip de la wlan0
#    ipWlan0=$(ifconfig wlan0 | grep "inet " | cut -d' ' -f10)

    # ontenemos la ip de la eth0
#    ipEth0=$(ifconfig eth0 | grep "inet " | cut -d' ' -f10)

#    echo "No tenemos ip"
#done

# actualizamos la hora
sudo date +"%d %b %Y %T %Z" -s "$(curl -s --head http://google.com | grep '^Date:' | cut -d' ' -f 3-)"

# obtener la fecha y hora
fecha=$(date +"%a_%d_%b_%Y")

echo "Fecha y hora actualizada" |& tee -a /home/feluve/logs/server_$fecha.log
echo "IP eth0: $ipEth0" |& tee -a /home/feluve/logs/server_$fecha.log
echo "IP wlan0: $ipWlan0" |& tee -a /home/feluve/logs/server_$fecha.log

# cambiar al directorio de app
cd CEGMEX/Control-de-Vacaciones/

echo "Iniciando servidor..." |& tee -a /home/feluve/logs/server_$fecha.log

# ejecutar el servidor
python3 manage.py runserver $ipEth0:8000 |& tee -a /home/feluve/logs/server_$fecha.log


# obtener la ip de la wlan0
ipWlan0=$(ifconfig wlan0 | grep "inet " | cut -d' ' -f10)

# imrpimir la ip
echo "IP wlan0: $ipWlan0"

# obtener la ip de la eth0
ipEth0=$(ifconfig eth0 | grep "inet " | cut -d' ' -f10)

# imrpimir la ip
echo "IP eth0: $ipEth0"