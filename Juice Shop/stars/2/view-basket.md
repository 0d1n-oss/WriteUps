# View Basket
## View another user's shopping basket.

Este reto consiste en ver la certa de compra de otro usuario.
Logrando que el servidor interprete que somos alguien mas y proporcione esos datos.

* Se creo un nuevo usuario en la tienda.
* Usando este usuario se agrego un producto a la cesta.
* Interceptando la peticion con burpsuite se logro modificar el id de la peticion (GET /rest/basket/9), logrando que el servidor devuelva la informacion de una cesta que no es nuestra.

