# Expose Metrics
## Find the endpoint that serves usage data to be scraped by a popular monitoring system.

La descripcion habla sobre un popular sistema de monitoreo, y una url que referencia a prometheus.
Investigando sobre este se encontraron rutas usadas en este servicio, creando un mini diccionario con esta informacion.

* Creacion de diccionario
```txt
data
data-agent
metrics
query
prefix
```

* Se uso gobuster para hacer fuzzing con estas rutas, encontrando la ruta metrics/ y completando asi el desafio.

`nota`
`Gobuster da un error con un codigo de respuesta, hay que excluir el codigo para poder proceder con el escaneo, y que asi gobuster ignore este codigo`

