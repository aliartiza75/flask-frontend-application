from app.ht_fe.routes import mod
from flask import Flask
app = Flask(__name__)

# registering application
app.register_blueprint(mod, uri_prefix='/ht_fe')
