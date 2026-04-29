from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return """
    <html>
        <head>
            <title>Mi App en Flask</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>🚀 Mi App está funcionando</h1>
            <p>Desplegada en Elastic Beanstalk</p>
            <p>Versión 3</p>
            <a href="/health">Ver estado</a>
        </body>
    </html>
    """

@application.route("/health")
def health():
    return {
        "status": "ok",
        "mensaje": "La aplicación está corriendo correctamente"
    }