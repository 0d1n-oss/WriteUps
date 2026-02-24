# Cross-Site Scripting (XSS) DOM

#### Que es un XSS?
Un ataque XSS (Cross-Site Scripting) en ciberseguridad es una vulnerabilidad web que permite a un atacante inyectar scripts maliciosos (usualmente JavaScript) en sitios web legítimos, los cuales se ejecutan en el navegador de la víctima. Esto busca robar sesiones, cookies, información personal o redirigir usuarios a sitios maliciosos.

#### Que especifica el DOM?
El XSS basado en DOM (Document Object Model) es un tipo de ataque de seguridad web donde el código malicioso se ejecuta totalmente en el navegador de la víctima al manipular el entorno DOM, sin necesidad de interactuar con el servidor. Ocurre cuando un script JavaScript del lado del cliente toma datos no seguros (como window.location) y los escribe inseguramente en la página (innerHTML, document.write).

---

![7-1](./images/7-1.png)
El reto presenta una pagina con botones que facilitan el "cambiar" el lenguaje, lo importante de esto es poder manipular la url.

![7-2](./images/7-2.png)
Observando el parametro **default** para poder cambiar el idioma, cambiando el parametro y logrando ver como esto se reescribe en la pagina.
