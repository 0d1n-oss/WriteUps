# Maquina: Report
- Dificultad: Medio
- OS: Linux
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/banner.png)

---

## Reconocimiento

La fase de escaneo inicia con nmap, mapeando los puertos abiertos de la maquina para descubrir posibles accesos.
Encontrando los puertos 80, 22 y 3306 en el host.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/1.png)

`Nota`
Hay que agregar el host a nuestro sistema en el archivo "/etc/hosts", de lo contrario la web no respondera correctamente.
``` bash
{IP}    realgob.dl
```

Teniendo el puerto 80 abierto se le dio un vistaso a la web.
La pagina web cuenta con un aspecto gubernamental, teniendo apartados de noticias, informacion, acceso, etc...
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/2.png)

`Nota`
Esta maquina tiene varias vulnerabilidades a explotar, use solo una "ruta" para resolverla, pero aun asi documentare las demas vulnerabilidades que encontre.

---

## Vulnerabilidades

### Sql Injection
Dentro de el apartado de "noticias" se puede ver algo peculiar, las noticias tienen una especie de identificador que se refleja en la url.
Ya habiendo confirmado el puerto 3306 y el servicio MaruaDB en el escaneo de nmap es obvio que hay una base de datos sql detras.

Usando la herramienta sqlmap se logro vulnerar la base de datos a traves de la url de la pagina, consiguiendo todos los datos relevantes.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/3.png)

``` bash
#Mostrar las bases de datos
sqlmap -u http://realgob.dl/noticias.php?id=1 --dbs --batch
```

### LFI
En la ruta /about.php tambien se encontro una vulnerabilidad vista en la url, pudiendo ver el parametro "file" en esta se intento injectar varios tipos de rutas con fuzzing.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/4-1.png)
Logrando leer archivos de el sistema mediante las peticiones web, cargando el contenido de estos como parte de la pagina.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/4-2.png)

### Clave debil
El servidor web posee un apartado de login para acceder a sus sistema, este es un panel de acceso comun y corriente.
Tan comun y corriente que contenia credenciales ....fragiles, pudiendo hacer un ataque de fuerza bruta y descubriendo un usuario y clave validos para acceder.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/5.png)

---

Ya habiendo desglosado las vulnerabilidades solo faltaria acceder al sistema para proseguir con la explotacion.
Habiendo comprometido el panel de login se puede acceder a un area que nos permite subir un archivo, aunque solo un archivo de imagen.
Usando la reverse shell de pentest monkey (y modificando la ip y puertos dentro de el archivo) se logro subir un backdoor en php.
Obviamente modificando la peticion en burpsuite, haciendo creer al sistema que es un archivo de imagen tipo GIF.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/6-1.png)

El mensaje de aprovacion indica que el archivo se subio correctamente.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/6-2.png)

Luego de iniciar nuestra coneccion de escucha con netcat solo quedaria acceder al archivo que subimos, este deberia encontrarse en el directorio /uploads
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/6-3.png)
``` bash
# Coneccion en escucha
nc -lvp 443
```
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/6-4.png)

---

## Explotacion.

Estando dentro de la maquina se puede corroborar que el usuario es "www-data"
Dando vueltas y buscando se logro ver algo interesante, un directorio ".git"
Habiendo investigado un poco me di cuenta que puedo interactuar con git dentro de este contenedor.
creando un entorno de trabajo para poder ver informacion sobre los logs.

```
# Creacion de la variable
export HOME=/var/www/html/uploads

# Agregar el directorio seguro
git config --global --add safe.directory /var/www/html/desarrollo/.git

# Acceder a los logs
git logs
```
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/7.png)

Dentro de la informacion de los logs se puede ver que hay varios usuarios.
Usando el comando "git show {Numero de commit}" se pudo ver mas informacion sobre el usuario adm (escoji este primero por que contaba con un directorio de trabajo en el sistema)
Pudiendo ver la clave de este usuario, logrando acceder por ssh (ahorrandome el tratamiento de tty)
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/8.png)

Siendo el usuario adm solo faltario encontrar algo que lleve hacia el usuario root.
Tras un rato de revisar cosas se encontro una variable que resaltaba entre las demas, conteniendo un mensaje que parecia ser hexadecimal.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/9.png)
Tras convertir esto a texto (si era hexadecimal) da la clave "dockerlabs4u"

---

# Pickle
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/report/pickle.png)
