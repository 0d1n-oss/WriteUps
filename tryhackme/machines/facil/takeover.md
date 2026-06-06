# Reto: TakeOver
- Dificultad: Facil
- Tipo: Desafio
- Tecnologia: Navegador web

![](../../assets/images/takeover/banner.png)

---

El desafio consiste en una especie de auditoria, una empresa necesita que les mostremos el "punto vulnerable".

Accediendo a la pagina principal se puede ver una web simple.

![](../../assets/images/takeover/1.png)

Usando fuzzing se lograron descubrir algunos dominios (dejando en claro la ip de el sevridor).

![](../../assets/images/takeover/3.png)

El subdominio **support** alberga una web simple.
Lo interesante de este subdominio es el certificado. La web usa https, pero el certificado no es optimo.

![](../../assets/images/takeover/4.png)

![](../../assets/images/takeover/5.png)

Viendo el certificado se pudo encontrar un nuevo dominio.
Al intentar acceder a este se pudo ver una pagina de error, la cual contiene la flag.

![](../../assets/images/takeover/6.png)
