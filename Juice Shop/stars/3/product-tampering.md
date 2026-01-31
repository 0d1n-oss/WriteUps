# Product Tampering
## Change the href of the link within the OWASP SSL Advanced Forensic Tool (O-Saft) product description into https://owasp.slack.com.

El desafio consiste en cambiar el parametro `href` en un producto del que se nos da la url.

Interceptando las peticiones con burpsuite se logra ver que al precionar este producto en su seccion de comentarios este ya tiene una url.
Este cuenta con el parametro `/rest/products/9` el cual proporciona la informacion de el producto.
Investigando un poco las direcciones se encontro `/api/products/9` logrando ver la informacion de el producto en formato json.

Para lograr inyectar codigo para reemplazar el mensaje de `description` se modifico la peticion usando burpsuite.
* cambiando el parametro `GET` por `PUT`
* Agregando el parametro `Content-type: application/json` para que la peticion lo interprete como json.
* agregando `{"description":"<a href=\"https://owasp.slack.com\" target=\"blank_\" >More...</a>"}` al final de la peticion para inyectar el codigo.

Ya solo quedo dirigirse ese producto, abrir su area de info, clickear en el area de `More...` y completar el desafio.

