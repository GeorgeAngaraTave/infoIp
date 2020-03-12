from flask import Flask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = 'esto-es-una-clave-muy-secreta'