# Maquina: Database
- Dificultad: Medio
- OS: Linux
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/banner.png)

## Reconocimiento
La face de reconocimiento se realizo con con nmap, encontrando varios puertos abiertos con sus respectivos servicios.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/1.png)

Accediendo a la web se puede ver un panel de login, las primeras opciones fueron fuzzing y fuerza bruta, pero al final se tomo la desicion de usar una inyeccion sql.
Usando una inyeccion sql clasica se pudo hacer un bypass al panel, viendo que la pagina da la bienvenida al usuario dylan.

``` bash
username = 'or 1=1 -- -
password = test
```

![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/2.png)
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/2-2.png)

Teniendo ya constancia de que la web es vulnerable a sql injection se procedio a usar la herramienta sqlmap.
Con esta se fue capaz de extraer informacion de la base de datos

``` bash
#listar bases de datos
sqlmap -u http://172.17.0.2/index.php --dbs --form --batch

#listar tablas de base de datos register
sqlmap -u http://172.17.0.2/index.php --form -D register --tables --batch

#dumpear la tabla users de la base de datos register
sqlmap -u http://172.17.0.2/index.php --form -D register -T users --dump --batch
```

Luego de dumpear la informacion de la base de datos se encontraron credenciales importantes de el usuario dylan.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/3.png)

Ya con las credenciales de el usuario dylan se realizo una intrucion por el servicio smb, logrando encontrar un archivo dentro de este.
este archivo contiene una especie de hash, el cual al parecer esta en MD5.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/4.png)

Se uso la herramienta john the ripper para encontrar la clave de el usuario, la cual es 'lovely' en este caso.
Teniendo con esto una clave para acceder por ssh.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/5.png)

Escaneando mas la maquina se encontraron mas cosas interesantes por el servicio smb.
Con la herramienta enum4linux se logro obtener informacion sobre varios usuarios de el sistema.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/6.png)

Antes de acceder por ssh se creo una mini lista con tres nombres, justo los que se descubrieron en el escaneo hacia el servicio smb.
Logrando acceder con el usuario augustus.
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/7.png)

## Explotacion.
Dentro de la maquina somos el usuario augustus, desde este se pudo ver que hay otros dos usuarios.
Se encontro un binario (/usr/bin/java) con permisos de el usuario dylan, se intento proceder con la escalada de privilegios desde esta via, pero no dio frutos.
Se logro descubrir que el usuario dylan uso su misma clave tanto en el servicio smb como en el servicio ssh (todo un genio).
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/8.png)

Despues de investigar algunos binarios se encontraron algunos ejemplares con permisos de root, explotando el binario /usr/bin/env se logro obtener una shell de el usuario root.
pudiendo saltarnos los demas usuarios y obteniendo el acceso absoluto desde el usuario august
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/9.png)

## Conclusion
Esta maquina resulto interesante, algo basica, pero curiosa.
La fase de explotacion me dio complicaciones, aunque logre resolver la escalada de privilegios usando otro binario con permisos.

# Pickle rick!!!
![](https://github.com/0d1n-oss/WriteUps/blob/main/dockerlabs/assets/images/database/pickle.png)
