# Maquina: Vulnvault
- Dificultad: Facil
- OS: Linux
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/banner.png)

## Reconocimiento.
Se inicio con un escaneo de nmap, descubriendo dos puertos que contienen el servicio ssh en el puerto 22 y otro en el puerto 80 con una web de apache.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/1.png)

Centrandonos en la web esta presenta un panel que sirve para crear reportes, permitiendo asignar un nombre y fecha.
el metodo vulnerable fue un command injection, usando el panel para el nombre de los reportes.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/2.png)

Se intento crear una reverse shell usando esta vulnerabilidad, pero no dio resultados.
Siguiendo con la exploracion se empezo a buscar entre los archivos de la web y sus permisos, descubriendo un usuario samara.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/3.png)

Este usuario contiene su propio directorio, con dos archivos.
El archivo user.txt no permite ser leido, y el artchivo message.txt devuelve un mensaje de "no deberias estar aqui :(" asi que no hay nada que hacer con ellos de momento.
Explorando el directorio se descubrio un directorio **.ssh** y viendo dentro de el una clave id_rsa.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/4.png)

Copiando esta clave y usandola desde nuestra maquina se pudo conseguir acceder a la maquina victima, usando el usuario samara.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/5.png)
## Explotacion.

Dentro de la maquina como el usuario samara se intento interactuar con los archivos.
El archivo user.txt ahora se puede abrir, pero su contenido es ilegible, parece un hash pero no pude identificar cual era.

Buscando archivos con permisos y bianarios con actividad de escritura se encontro un script llamado echo.sh (disfrazado con el nombre de un binario comun de linux)
buscando en los procesos ejecutados por root se encontro que este binario era ejecutado junto a los servicios iniciales de el sistema (apache y ssh)
Este se encargaba de una tarea simple, escribir un archivo, estando dentro de un loop. 
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/6-1.png)
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/6-2.png)

Habiendo descubierto este archivo y su funcionamiento se procedio a modificarlo, agregando una reverse shell en bash y escuchando en el puerto 443 con netcat
Pudiendo asi establecer una coneccion desde otra terminal siendo ya el usuario root.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/7.png)

## Conclusion.
La maquina es facil, es entretenida y util para practicar command injection.
El tener que buscar entre los procesos de el sistema y encontrar un archivo oculto y modificarlo para alterar su funcionamiento fue muy interesante.

# Pickle rick!!!
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/vulnvault/pickle.png)
