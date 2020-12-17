# Instrucciones

se requiere Python 3, se testeo en python 3.8.2.

```bash
git clone https://github.com/ElPapi42/sendgrid-script
cd sendgrid-script
pip3 install -r requirements.txt
```
* Registrar un Sender en la aplicacion web de SendGrid, este sera usado para enviar los emails.
* Obtener una Key para la API de SendGrid (Settings > API Keys > Create API Key > Dar un nombre y darle full access al token, o darle permiso para enviar emails.)
```bash
export SENDGRID_API_KEY=<your-key>
python3 send_email.py sender@example.com emails.csv "Subject of email" template.html
```

El primer argumento del script es el email del sender (previamente autorizado en sendgrid), luego un csv con una columna llamada 'email' que contiene todos los emails a los que se quiere enviar el correo. Sigue el subject del email, y por ultimo el html que se quiere enviar.

En este repo se incluyen el csv y el html de ejemplo, para personalizarlo.

No se envian emails a hotmail, parece que hay que registrar un dominio en sendgrid, pero no se mucho mas, no medio tiempo de investigar.