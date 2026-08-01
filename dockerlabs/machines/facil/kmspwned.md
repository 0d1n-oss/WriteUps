# Maquina: Kmspwned
- Dificultad: Facil
- OS: Linux

![](../../assets/images/kmspwned/banner.png)

---

## Reconocimiento.

La fase de reconocimiento inicia usando **nmap** para realizar un escaneo de puertos y servicios.
Encontrando que el puerto 22 y el puerto 80 estan abiertos.

![](../../assets/images/kmspwned/1.png)

Accediendo desde el navegador se puede ver una web simple, esta haciendo alucion a servicio de **dominios y aplicaciones en la nube.**

![](../../assets/images/kmspwned/2.png)

Explorando un poco la pagina se puede ver que esta permite crear un usuario.
Creando nosotros al usuario fulano para futuras pruebas.

![](../../assets/images/kmspwned/3.png)

Ya logeados y explorando un poco la pagina se probaron varios ejemplos comunes (y de paso una inyeccion sql *cof cof)

![](../../assets/images/kmspwned/7.png)

Viendo que la inyeccion da frutos, se capturo la peticion desde burpsuite y se guardo en un archivo.

![](../../assets/images/kmspwned/8.png)

Logrando usar la herramienta **sqlmap** con esta peticion, logrando acceder a la base de datos y encontrando dos flags (algo irrelevante para los retos de dockerlabs, pero se agradece el detalle)

![](../../assets/images/kmspwned/9.png)

Y logrando encontrar credenciales de otros usuarios ya existentes dentro de el servidor.

![](../../assets/images/kmspwned/11.png)

``` bash
sqlmap -r peti.txt --batch --dump
```

> NOTA

> Tambien pudimos ver nuestra propia informacion

![](../../assets/images/kmspwned/10.png)


Y por ultimo encontrando una pista que nos guia hacia el panel de administracion (aunque era un poco obvio).

![](../../assets/images/kmspwned/12.png)

Ya dentro de el panel (con las credenciales de el usuario admin) se pudo ver el dashboard de este.

![](../../assets/images/kmspwned/13.png)

Aprovechando las nuevas credenciales obtenidas se accedio a la maquina por ssh siendo el usuario carlos.

---

## Escalada de privilegios

### Carlos > Root

Dentro de la maquina vemos una flag, y aparte de esto recordamos una de las dos pistas que vimos en la base de datos, el comentario que hacia alucion a la ruta **/opt**.
Entrando a esta ruta se pudo ver un archivo llamado **backup.sh**, el cual pertenece al usuario root.

Este archivo crea una copia de seguridad diraria, y crea unos logs registrando la hora.

![](../../assets/images/kmspwned/14.png)

Ya que ...raramente tenemos permisos de escritura agregamos una linea al archivo que nos permitira una reverse shell.
Quedando solo a la escucha en el puerto seleccionado y esperando a que el script se ejecute para la proxima copia de seguridad.

![](../../assets/images/kmspwned/16.png)

Consiguiendo asi el control sobre el usuario root.

---

## Pickle Rick!

![](../../assets/images/kmspwned/pickle.png)
