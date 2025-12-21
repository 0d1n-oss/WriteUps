# Maquina: Bashpariencias
- Dificultad: Medio
- OS: Linux

![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/main.png)

## Reconocimiento
La face de reconocimiento se realizo con con nmap, encontrando varios puertos abiertos con sus respectivos servicios.
Encontrando en el escaneo una web en el puerto 80 y un servicio ssh en el puerto 8899.
- 8899 (ssh | openssh)
- 80 (http | apache)

Dentro de la web se puede ver un dashboard clasico pero limpio, teniendo varios botones y demas cosas que conducen a otras rutas.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/1.png)

Dentro de el codigo de la web hay un boton que lleva a un formulario.
dentro de este hay un item oculto, que contiene un posible usuario y clave (algo despectivos estos datos)
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/2.png)

Teniendo las credenciales de ssh se logro acceder a la maquina, teniendo el usuario **rosa** y la clave **lacagadenuevo**
Estando listos para proceder con la fase de explotacion.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/3.png)

## Explotacion
Dentro de la maquina se identificaron los usuarios, teniendo una guia clara de los usuarios que comprometer en una escalada de privilegios.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/4.png)

### Rosa
El usuario **rosa** contenia una trampa en su directorio (parece que no era mas habil de lo que parecia)
El directorio de rosa contenia un fichero llamado **-** siendo casi invisible, hasta que se logro acceder a el directorio y ver los archivos dentro de este.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/5.png)

Dentro de el directorio se encontraron dos archivos, una nota para **rosa** de parte de **juan** que hace una especie de reto para rosa.
La prueva consiste en hackear un archivo zip, para descargar esto en nuestra maquina se creo un servidor de archivos usando python, descargando este en nuestra maquina con wget.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/6.png)

Usando la herramienta **zip2john** se logro crear el hash de el archivo.
Ya con el hash creado se uso la herramienta **john the ripper** para descencriptar el hash y obtener la clave.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/7.png)
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/7_2.png)

Ya con el zip descomprimido se encontro un archive que contenia la clave de el usuario juan.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/7_3.png)

### Juan
Dentro de el usuario juan se encontraron dos binarios con permisos de el usuario **carlos**
Usando el binario tree se pudieron listar las carpetas de **home/** encontrando en el directorio **/home/carlos/** un archivo llamado password.
Se uso el binario **cat** para ver el contenido de este archivo, encontrando la palabra **chocolateado**
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/8.png)

### Carlos
Ya con la clave descubierta se accedio al usuario carlos, viendo que el binario **/usr/bin/tee** tiene permisos de root.
El comando tee en Unix/Linux se utiliza para leer desde la entrada estándar y escribir tanto a la salida estándar como a uno o más archivos.
Usando el binario tee se logro modificar el archivo sudoers otorgandole permisos ilimitados al usuario carlos, logrando desde la terminal de este acceder a la consola de el usuario root.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/9.png)

## Conclusion
La maquina fue entretenida, el estilo classico de vulnerar una web y acceder por ssh estuvo bien, aunque me hizo gracia la inclucion de el usuario rosa.
La escalada de privilegios no es complicada, y a sinceridad creo que esta maquina deberia catalogarse como facil, Ya que no presenta desafios muy complejos.

# Picle rick!!
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/bashpariencias/pickle.png)
