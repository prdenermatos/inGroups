from flask import render_template, redirect
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/', methods = ['GET', 'POST'])
def index():
    # isPermit = ACL.avaliable()
    # if not isPermit:
    #     return redirect('/')

    
    return render_template("index.html")


# ADC envio do form para email do ADM do sistema