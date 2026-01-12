# Security Ninjas Lab

## Información
**Security Ninjas** de **OpenDNS** es un *laboratorio de capacitación en seguridad de aplicaciones* (AppSec) creado como una herramienta práctica para aprender sobre **vulnerabilidades comunes en aplicaciones web**, basadas principalmente en el **OWASP Top 10**. ([Hack Players][1])

### ¿Cómo funciona el laboratorio?

El laboratorio se ejecuta como una **aplicación web vulnerable local** (o en red) que puedes desplegar usando **Docker**, lo que lo hace fácil de levantar y destruir sin riesgos:

1. Descargar la imagen Docker de Security Ninjas:

```bash
   docker run -d -p 8899:80 opendns/security-ninjas
````

2. Acceder desde el navegador a `http://localhost:8899` (u otra IP/puerto). ([Hack Players][1])

Este entorno es útil para **práctica de pentesting / hacking ético** o para aprender desde lo básico cómo funcionan vulnerabilidades como **command injection**, **XSS**, **CSRF**, entre otras.

---

## Resolución

### Reto 1 — Command Injection

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/1.png

La aplicación presenta un input que no valida ni sanitiza correctamente los datos ingresados, los cuales son concatenados directamente en una llamada al sistema, permitiendo inyectar operadores de shell (`|`, `;`, `&&`).

```bash
google.com | ip a
```

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/1-2.png

---

### Reto 2 — Broken Authentication

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/2.png

La cookie de sesión contiene información del usuario y no está protegida ni validada correctamente del lado del servidor.

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/2-3.png

Tras obtener una cookie válida (`user1`), se puede clonar y modificar para crear otra (`user2`).

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/2-4.png

Usando Burp Suite se intercepta la petición y se reemplaza la cookie para acceder a los recursos de otro usuario.

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/2-5.png

**Nota:** Es importante usar la petición a `user_details.php`, ya que otras rutas requieren credenciales válidas.

---

### Reto 3 — Cross-Site Scripting (XSS)

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/3.png

#### Reflected

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/3-1-1.png

```html
<script>window.location.href="/unlucky.php";</script>
```

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/3-1-2.png

#### Stored

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/3-2-1.png

```html
<script>window.location.href="/hacked_users.php";</script>
```

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/3-2-2.png

---

### Reto 4 — Insecure Direct Object References (IDOR)

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/4.png

El sistema redirige a archivos PDF cuyos nombres están codificados en hexadecimal.

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/4-1.png

```bash
# Decodificar
echo 6e6f6e5f636f6e666964656e7469616c | xxd -r -p
non_confidential

# Crear nuevo valor
echo -n "confidential" | xxd -p
636f6e666964656e7469616c
```

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/4-4.png

---

### Reto 5 — File Inclusion / Source Disclosure

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/5.png

El parámetro `fname` permite cargar archivos arbitrarios:

```
http://localhost/meme.php?fname=meme1.htm
```

Modificando:

```
/meme.php?fname=config.php
```

se accede a archivos internos.

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/5-1-2.png
https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/5-1-1.png

---

### Reto 6 — Lógica insegura

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/6.png

La aplicación valida los descuentos del lado del cliente, permitiendo descubrir un código especial analizando el HTML/JS.

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/6-1.png

---

### Reto 7

**Nota:** El reto parece estar defectuoso en esta versión del laboratorio.

---

### Reto 8 — CSRF

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/8.png

La aplicación no implementa tokens CSRF.

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/8-2.png

```html
<img src="http://172.17.0.3/update_email.php?new_email=user1@evil.com&user=user1&Update=Save">
```

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/8-6.png
https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/8-7.png

**Nota:** También puede ejecutarse directamente desde el navegador.

---

### Reto 9 — Bypass de autenticación

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/9.png
https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/9-2.png

```
fm.php?u=humphrey
```

https://github.com/0d1n-oss/WriteUps/blob/main/Security%20Ninjas/images/9-3.png

---

### Reto 10 — Open Redirect

La aplicación usa un parámetro de redirección tras completar el captcha, pero el reto está parcialmente limitado en esta versión.

---

## Conclusión

El laboratorio es muy recomendable para principiantes, fácil de desplegar y enfocado en el aprendizaje práctico.

### Problemas detectados

* Reto 3: comportamiento inconsistente tras múltiples pruebas.
* Reto 7: no está correctamente implementado.
* Reto 10: la solución propuesta no funciona correctamente.

---
