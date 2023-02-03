from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder="../templates",static_folder="../static")

app.config.from_object('config')
db = SQLAlchemy(app)

# with app.app_context():
#     db.create_all()


from src.controllers.index_controller import *
from src.controllers.registration_user_controller import *
from src.controllers.plataform_controller import *
from src.controllers.reports_controller import *
from src.controllers.reports_add_controller import *
from src.controllers.shepherd_controller import *
from src.controllers.trail_details_controller import *
from src.controllers.supervision_controller import *
from src.controllers.schedule_controller import * 
from src.controllers.visitors_controller import *
from src.controllers.settings_controller import *








