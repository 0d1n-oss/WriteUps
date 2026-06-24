# Maquina: Gotham
- Dificultad: Facil
- OS: Linux

![](../../assets/images/gotham/banner.png)

---

## Reconocimiento.

La fase de reconocimiento inicio con un escaneo simple de nmap, descubriendo el puerto 80 con un servicio web, y el puerto 22 con ssh.

![](../../assets/images/gotham/1.png)

Desde el navegador se puede ver una web con un panel de login.
Explorando el codigo de la web, se puede ver un mensaje que indica que las credenciales son **guest:guest**.

![](../../assets/images/gotham/2.png)
![](../../assets/images/gotham/3.png)

Dentro de la web se puede ver un dashboard, este indica que somos el usuario **guest** con el rol de **user**.

![](../../assets/images/gotham/4.png)

Explorando algunas rutas se encontro la ruta **/admin.php**, explorando esto desde burpsuite se puede ver el factor interesante....una cookie.

![](../../assets/images/gotham/5.png)

Usando [JWTDebuger](https://www.jwt.io/) se pudo ver la info de la cookie, viendo que esta tiene un segmento "secreto".

![](../../assets/images/gotham/6.png)

Usando john the ripper con el diccionario rockyou se pudo crackear la clave de JWT.

![](../../assets/images/gotham/7.png)

Ya con la clave de este se procedio a modificar la cookie, cambiando el rol de el usuario a **admin** seguido de el nombre.

![](../../assets/images/gotham/8.png)

Accediendo a el dashboard con la nueva cookie se pude ver el nuevo rol que tenemos, pudiendo acceder al nuevo apartado de **network Operations Center (Admin)**.

![](../../assets/images/gotham/9.png)

Ya en esta nueva pagina se puede agregar una direccion ip para que el servidor lo verifique.
Usando un **|** en el area de input se puede hacer que le servidor linux salte el primer comando y ejecute el segundo comando, en este caso un **whoami**.

![](../../assets/images/gotham/10.png)

Usando este nuevo punto vulnerable se uso una reverse shell para acceder a la maquina.

![](../../assets/images/gotham/11.png)

Viendo los archivos de la web se pudieron encontrar credenciales dentro de un archivo de configuracion perteneciente a una base de datos.
Y ya que el usuario bruce (Que encontramos viendo el archivo /etc/passwd) repitio la misma clave en dos servicios se pudo acceder a su usuario.

![](../../assets/images/gotham/12.png)

Desde el usuario bruce se encontro una flag (aunque no se use en estos casos) y un binario con permisos de root.
Usando el parametro **exec** de el binario **find** se pudo ejecutar una shell siendo root.

![](../../assets/images/gotham/13.png)

---

## Pickle !!!

![](../../assets/images/gotham/pickle.png)
