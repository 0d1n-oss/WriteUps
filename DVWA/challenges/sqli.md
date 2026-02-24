# SQL Injection

#### Que es una injeccion sql?
Una inyección SQL manipula una consulta SQL estándar para explotar vulnerabilidades en la base de datos subyacente de la aplicación. Veamos algunos ejemplos de códigos para ver cómo funciona esto.

---

![6-1](./images/6-1.png)
La web muestra un input que permite ingresarc texto, pidiendo un ID de usuario, desde ahi se puede intuir que existe una base de datos que contiene usuarios, y usando un paylaod basico se puede dumpear la base de datos.

![6-2](./images/6-2.png)
Otra alternativa seria usar **sqlmap**, una herramienta que permita atacar bases de datos con bastantes funcionalidades.

``` bash
sqlmap -u "http://172.17.0.2:80/vulnerabilities/sqli/?id=1" -D dvwa -T users --dump --batch --level=4 --risk=3
```
