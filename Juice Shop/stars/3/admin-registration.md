# Admin Registration
## Register as a user with administrator privileges.

El desafio consiste en crear un usuario que contenga los privilegios de administrador.
En el apartado `administration` se encuentra una lista con todos los usuarios, usando la opcion `network` en las herramientas de desarrolllador se puede ver una peticion que contiene los datos en json de estos usuarios.


Con esta info se pueden ver cosas interesantes, como que los usuarios pueden usar el parametro `role` para asignarles un rol en la web.
Ya solo queda:

* Crear un usuario en la web.
* Capturar la peticion con burpsuite.
* agregar el paraemtro `role`.
* Enviar la peticion para crear nuestro usuario con permisos de administrador.

`Nota`
`Al agregar el rol en la peticion de burpsuite se recomienda usar el formato raw`
`Para evitar errores de tabulacion`
