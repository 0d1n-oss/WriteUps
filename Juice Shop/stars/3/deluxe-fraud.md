# Deluxe Fraud
## Obtain a Deluxe Membership without paying for it.

El reto consiste en conseguir una membresia sin pagar nada.
Para este reto se debe explorar el codigo de la pagina web y modificarlo.
En el area de el boton de `pay` (que usualmente este desabilitado) debemos borrar las lineas `mat-button-disabled` y `disabled=true`.
Consiguiendo que el boton sea funcional.

Usando burpsuite se puede interceptar la peticion al presionar este boton.
Modificando el parametro `paymentMode` para dejarlo vacio podemos hacer que el servidor nos haga miembro sin pagar.
