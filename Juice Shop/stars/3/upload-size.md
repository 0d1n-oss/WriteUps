# Upload Size
## Upload a file larger than 100 kB.

El reto comsiste en subir un archivo de mas de 100 kB, cosa que la web no permite.
Asi que habra que interceptar la peticion de la web y modificar el contenido de nuestro archivo.

* Crear un archivo cualquiera con texto incluido.
* Interceptar la peticion con burpsuite.
* agregar contendio a la descripcion de el archivo, en este caso muchas letras A (hay que tener en cuenta que deben ser muchas, contando que cada letra A usaria 4 bytes tienen que ser muchas cadenas para sobrepasar los 100 kB)

`Nota`
`En mi caso cree un archivo llamado data.txt`
`Pero ya que este formato no es aceptado por la web debi renombrarlo por data.txt.zip`
