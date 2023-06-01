# Utilizamos la imagen base de eclipse-mosquitto
FROM eclipse-mosquitto

# Copiamos los archivos de configuración, datos y registros a la ubicación dentro del contenedor
COPY ./config /mosquitto/config
COPY ./data /mosquitto/data
COPY ./log /mosquitto/log

# Exponemos los puertos 1883 y 9001
EXPOSE 1883 9001

# Establecemos el comando de inicio del contenedor
CMD ["mosquitto"]
