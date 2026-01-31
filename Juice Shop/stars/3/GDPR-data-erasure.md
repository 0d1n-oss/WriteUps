# GDPR Data Erasure
## Log in with Chris' erased user account.

El reto consiste en logearse siendo el usuario chris.
Este correo parece ser diferente, asi que habra que recurrir a otros medios para encontrarlo.
Se uso una de las vulnerabilidades sql para listar los usuarios, encontrando el correo de el usuario chris.
Ya con el correo se uso una injeccion sql para hacer el bypass, la clave no importa mucho en este caso.

```
email: chris.pike@juice-sh.op' -- -
password: 11111
```
