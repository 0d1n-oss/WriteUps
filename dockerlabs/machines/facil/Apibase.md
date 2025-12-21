# Maquina: Elevator
- Dificultad: Facil
- OS: Linux

![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/banner.png)

## Reconocimiento

El reconocimiento inicia con un escaneo de nmap para analizar los puertos y servicios expuestos.
El escaneo deja ver dos puertos, el puerto 5000 que usa un servicio werkzeug, y una coneccion ssh por el pueto 22.

![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/1.png)

Este servicio no parece ser un servicio web comun.
Werkzeug es una biblioteca WSGI (Web Server Gateway Interface) completa y robusta para Python, que proporciona un conjunto de utilidades para construir aplicaciones web, en lugar de ser un framework completo como Flask o Django.

En la web se muestra un mensaje de error, aunque hace alucion a una ruta llamada "users/" dentro de el sistema.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/2.png)
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/3.png)

Experimentando un poco se intento listar un usuario, descubriendo que el sistema usa sql como base de datos, lo cual es un dato bastante interesante para una inyeccion,
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/4.png)

Usando el parametro clasico " 'or+1=1+--+- " desde la url para la inyeccion, logrande ver al usuario **pingu** con la clave **pinguinasio**
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/5.png)
Teniendo estas credenciales se logro una coneccion exitosa por ssh.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/6.png)

## Explotacion.

Dentro de el sistema se tenia el control de el usuario pingu.
Este usuario en su directorio no tenia nada interesante, pero en el directorio "/home" se encontraron varios archivos como la base de datos, la app, y una especie de captura de trafico web.
Esta contiene algunas palabras minimas legibles, dentro de ellas esta "PASS balulero" la cual hace alucion a una clave.
Efectivamente, el usuario root tenia como clave balulero, pudiendo comprometer la maquina.
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/7.png)

# Pickle rick !!!
![](https://github.com/0d1n-oss/Writeups/dockerlabs/assets/apibase/pickle.png)
