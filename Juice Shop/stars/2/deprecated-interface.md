# Deprecated Interface
## Use a deprecated B2B interface that was not properly shut down.

Para este reto se empezo buscando en el main.js de la web la palabra b2b, logrando descubrir una linea de codigo que indica algo interesante.
La linea de codigo indica que hay un area de input que permite archivos PDF,XML,ZIP dandonos la oportunidad de inyectar un archivo en la web.
```
Input area for uploading a single invoice PDF or XML B2B order file or a ZIP archive containing multiple invoices or orders<!---->'
```

Buscando las areas de input mas comunes se encontro complaint (http://172.17.0.3:3000/#/complain) el cual permite subir archivos.
Corroborando los tipos de archivos soportados se intento subir un archivo de imagen, siendo este obviamente rechazado.

El mensaje de error emergente dice que solo acepta archivos PDF o ZIP, aunque en el codigo vimos que esto no era cierto.
Pudiendo crear un archivo con extencion xmly subiendolo a la pagina, completando el desafio.
