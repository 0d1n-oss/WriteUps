# Command Injection

#### Que es una injeccion de comandos?
La inyección de comandos es un ciberataque que consiste en ejecutar comandos arbitrarios en un sistema operativo (SO) host. Normalmente, el atacante inyecta los comandos aprovechando una vulnerabilidad de la aplicación, como una validación de entrada insuficiente.

---

![2](./images/2)

Este reto muestra un input, el cual solicita una direccion ip a la cual hacer ping, comprobando que el sistema esta ejecutando comandos.

Usando parametros de bash se logran injectar comandos para ejecutarlos en el sistema, parametros como ";", "&& " o "|"
