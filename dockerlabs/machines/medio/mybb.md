# Maquina: Database
- Dificultad: Medio
- OS: Linux
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/banner.png)

## Reconocimiento
Se inicio con un escaneo de nmap para identificar puertos abiertos y sus servicios.
El escaneo revelo un servicio apache en el puerto 80.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/1.png)

Dentro de la web se puede ver un dashboard minimalista (por no decir que no hace nada y no contiene casi informacion.)
Lo unico relevante es una url a la que nos envia (http://panel.mybb.dl) la cual debemos agregar a nuestro sistema para poder interactuar con ella.

``` bash
# ip victima        # dominio que nos recomienda
172.17.0.2          panel.mybb.dl
```

Teniendo este dominio agregado al archivo /etc/hosts se logra acceder a una web completamente nueva.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/2.png)
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/2-2.png)

Usando gobuster se pueden apreciar muchos directorios (mas de los que presenta la imagen), el que nos interesa de momento es el directorio "/backups"
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/3.png)

Este archivo parece un archivo dedicado a los logs, colocado por error (o a proposito) en la carpeta destinada a los backups.
Contiene informacion de peticiones a una base de datos, usuarios existentes y hasta un intento de session con una clave (aunque esta este encriptada)
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/4.png)
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/5.png)

El fuzzing tambien revelo un directorio "/admin" haciendo alucion a un panel de login.
Efectivamente era un panel de login, pudiendo analizar la peticion de este con las herramientas de desarrollador de el navegadorse puede ver la peticion o "request" que se le hace a la web.
Con esta info, y el mensaje de error se pudo proceder con un ataque de fuerza bruta, usando hydra se pudieron identificar posibles claves validas.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/6.png)
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/6-2.png)
Con estos resultados solo queda probar cual es el correcto para lograr acceder al panel de administracion.

**nota**
**El sistema se cierra al fallar 5 veces (y ya se gasto una de esas al probar una peticion erronea)**
**En caso de fallar los 5 intentos habria que reiniciar la maquina desde cero (desde el script de dockerlabs)**
**No funciona atacar desde otro contenedor o reiniciar el contenedor con un "docker restart" **

Intuyendo la clave se logro identificar la correcta (la maquina se llama MyBB, usa el servicio mybb y una de las opciones es babygirl...solo sentido comun) que era babygirl.
Logrando acceder al panel de administracion como un usuario con privilegios.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/mybb/7.png)

Dentro de este sistema se puede apreciar la version de los servicios que se estan ejecutando.
Con esta informacion se busco alguna vulnerabilidad conocida, encontrando la vulnerabilidad CVE-2023-41362.

*nota*
*La vulnerabilidad consiste en command injection, mybb permite crear plantillas que seran usadas en el foro, para evitar que estas contengan codigo malicioso el sistema usa "filtros con expresiones regulares" o "regex" para buscar patrones peligrosos.*
*En este caso se pudo introducir una entrada creada para atascar a la regex y que aborte antes de detectar el codigo malicioso.*

Y logrando encontrar un script en github que logra un command injection siempre y cuando se tengan el usuario y clave de administracion.
