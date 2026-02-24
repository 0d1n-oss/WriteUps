# Cross-site request forgery (CSRF)

#### Que es un CSRF?

La falsificación de solicitud entre sitios (CSRF), Sea Surf o Session Riding, es un vector de ataque que engaña a un navegador web para que ejecute una acción no deseada en una aplicación en la que un usuario ha iniciado sesión.

---

![3-1](../images/3-1)
Este reto incluye un formulario, el cual solicita cambiar la clave de el sitio.
Cambiando la clave como nos pide, se puede observar que la url refleja el como se cambio la clave en la web.

![3-2](../images/3-2)
La url muestra parametros interesantes, observando estos parametros se pueden ver como se cambia la clave, y obviamente se puede alterar, consiguiendo alterar la clave desde la url.

