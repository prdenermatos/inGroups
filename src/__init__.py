from flask import Flask
from flask_cors import CORS

app = Flask(__name__, template_folder="../templates",static_folder="../static")
CORS(app)

app.config.from_object('config')
# app.config['CORS_HEADERS'] = 'Content-Type'


from src.controllers.empresa_controller import *
from src.controllers.home_controller import *
from src.controllers.registration_user_controller import *
from src.controllers.plataform_controller import *
from src.controllers.reports_controller import *







