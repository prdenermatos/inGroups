from flask import render_template
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/menu-settings', methods = ['GET', 'POST'])
def menu_settings():
    # isPermit = ACL.avaliable()
    # if not isPermit:
    #     return redirect('/')

    
    return render_template("menu-settings.html")