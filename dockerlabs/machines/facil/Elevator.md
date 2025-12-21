# Maquina: Elevator
- Dificultad: Facil
- OS: Linux

![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/main.png)

## Reconocimiento

Se uso nmap para realizar un analisis a la maquina, explorando sus puertos y servicios abiertos.
Dentro de esta se encontro un servicio Apache 2.4.62 corriendo en el pueto 80, con una pagina que llevaba "El Ascensor Embrujado" por nombre.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/1.png)

Esta web pone un contexto, un ascensor misterioso en un hotel que aparenta estar embrujado.
Esta historia no es relevante para el ctf, y el boton de la pagina solo da un mensaje emergente de "Este misterio ah sido resuelto" asi que no hay nada importante aqui.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/2.png)
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/2-2.png)

La siguiente fase de el reconocimiemto se centro en el fuzzing web, usando la herramienta gobuster.
Encontrando con esta un directorio llamado themes.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/4.png)

Dentro de este directorio se encontraron archivos interesantes, una web que permite subir archivos de imagen y su respectivo directorio de almacenamiento.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/4-2.png)

Esta web solo permite subir archivos .jpg, de lo contrario son rechazados.
Con esta informacion se intento burlar la seguridad de la web, usando la conocida revershell de pentestmonkey y agregando la extencion .jpg pata que el sistema lo reconociera como un archivo de imagen.

*nota*
La reverse shell debe ser modificada, los parametros mas importantes son el host y el puerto.
``` bash
$ip = '127.0.0.1';  // CHANGE THIS
$port = 1234;       // CHANGE THIS
```

![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/5.png)
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/6.png)

Ya con esto se empezo a escuchar con netcat en el puerto asignado, consiguiendo una reverse shell con la maquina victima.
*nota*
Para la explotacion de la maquina es bastante util usar GTFOBins.
Una pagina que contiene informacion sobre la explotacion de muchos binarios, lo cual es util para este tipo de ctfs.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/7.png)

## Explotacion
El inicio de la explotacion comienza buscando archivos con permisos especiales para hacer una escalada de privilegios.
Buscando que usuarios comprometer para conseguir el acceso root.

### Daphne
Desde el usuario www-data (el usuario predeterminado de apache) se buscaron archivos con privilegios, encontrando al usuario daphne con permisos sobre el archivo /usr/bin/env.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/8.png)

### Vilma
Desde el usuario Daphne se realizo la misma tecnica enontrando el binario /usr/bin/ash el cual contiene permisos con el usuario vilma.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/9.png)

### Shaggy
Desde el usuario vilma (y si, se que esta mal escrito pero asi esta en la maquina) se encontro el binario /usr/bin/ruby que contiene permisos de el usuario shaggy.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/10.png)

### Fred
Desde el usuario shaggy se encontro el binario /usr/bin/lua el cual contiene permisos de el usuario fred.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/11.png)

### Scooby
Desde el usuario fred se encontro el binario /usr/bin/gcc el cual contiene permisos de el usuario scooby.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/12.png)

### Root
Desde el usuario scooby se encontro el binario /usr/bin/sudo (el obvio final de la maquina) que contiene permisos de el usuario root
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/13.png)

## Conclucion.
Esta maquina me parecio interesante, el usar la tematica de "misterio a la orden" de la serie de scooby doo me parecio creativa, logrando apelar a mi parte nostalgica.
El escalar privilegios sobre cada usuario de el grupo fue interesante, aunque algo largo por la cantidad de miembros de el grupo.
Con la tematica de scooby doo esperaba algun misterio como algun programa que analizar, u n bot atacando, un programa fantasma, etc...

# Pickle Rick!!!
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/elevator/pickle.png)

