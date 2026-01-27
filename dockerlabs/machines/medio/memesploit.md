# Maquina: Memesploit
- Dificultad: Medio
- OS: Linux
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/banner.png)

---

## Reconocimiento

La fase de escaneo inicio con un analisis usando la herramienta nmap.
Encontrando varios puertos y servicios expuestos.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/1.png)

Dentro de el navegador se puede ver una pagina web, esta contiene una especie de historia.
Lo importante son algunas palabras que resaltan (es util crear una lista con esta para fututas referencias).

```
memesploit
memesploit_ctf
fuerzabrutasiempre
memehydra
```

![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/1-2.png)

Ya que la web no ofrece mas informacion hay que explorar otras areas.
Usando la herramienta enum4linux se pudieron listar algunos recursos interesantes.
```
enum4linux -a {IP}
```

![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/2-1.png)
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/2-2.png)

Teniendo la informacion de estos usuarios y directorios de trabajo se pudo acceder por smb.
Usando la herramienta crackmapexec se logro hacer un ataque de fuerza bruta, usando la lista que ya se habia creado con la informacion de la web.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/3.png)

Teniendo ya una coneccion por smb se logro encontrar un archivo "secret.zip".
Este es un archivo zip con clave, asi que habra que crackear la clave para acceder a su contenido.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/4.png)

Usando la herramienta "zip2john" se logro extraer el hash de el archivo secret.zip.
Teniendo ya el hash se crackeo la clave usando la herramienta "john", usando la lista que ya habiamos creado.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/5.png)

Obteniendo un archivo llamado secret.txt.
Este contiene un usuario y clave, los cuales seran utiles para una coneccion por ssh.

---

## Explotacion

Ya dentro de la maquina se encontro algo parecido a una flag (aunque en este caso no sabria muy bien para que usarla).
Dentro de la maquina se uso el comando "sudo -l" para encontrar algun recurso que permitiera escalar privilegios.
Se logro encontrar que el archivo service esta ejecutando un programa, uno algo peculiar.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/6.png)

Buscando entre los archivos se pudieron encontrar rutas relacionadas "login_monitor".
Viendo que este servicio posee un directorio "/etc/login_monitor".

Dentro de este servicio se encontraron varios archivos, aunque el que interesa es "actionban.sh".
Este archivo crea logs falsos, creando un archivo "log" que pretende registrar y bloquear direcciones ip, aunque solo crea direcciones aleatorias.

Tras revisar los logs (el archivo que se crea en la ruta /tmp/block_log.txt) y realizar varias pruebas se pudo comprobar que este archivo se activa al iniciar sesion por ssh.
Para la escalada de privilegios se creara un nuevo archivo "actionban.sh" luego de renombrar el anterior.

``` bash
#!/bin/bash

chmod 4777 /bin/bash
```

![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/7.png)

Ya habiendo creado este archivo solo quedaria cerrar la sesion de ssh (todas las que esten abiertas) y acceder nuevamente.
Al acceder nuevamente por ssh el servicio "login_monitor" se active, accediendo a nuestro archivo y ejecutando el script, otorgando permisos a "/bin/bash".
Ya solo quedaria usar el comando "bash -p" en la nueva sesion de ssh, consiguiendo asi el acceso root.

![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/memesploit/8.png)

---

## Conclucion
Esta maquina de dockerlabs me resulto interesante, la web es algo sencilla, aunque cumple su funcion perfectamente.
Las claves de los servicios son sencillas, aunque es astuto que las claves esten en palabras claves de la pagina web, haciendo que haya que crear un mini diccionario para comprometer a todos los servicios.
Una maquina que recomendaria, con una dificultad baja, pero manteniendose entretenida.
