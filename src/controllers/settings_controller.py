from flask import render_template
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/menu-settings', methods = ['GET', 'POST'])
def menu_settings():
    # isPermit = ACL.avaliable()
    # if not isPermit:
    #     return redirect('/')

    
    return render_template("menu-settings.html")


@app.route('/settings-church', methods = ['GET', 'POST'])
def settigns_church():
    return render_template("settings-church.html")


@app.route('/settings-groups', methods = ['GET', 'POST'])
def settings_groups(): 
    return render_template("settings-groups.html")


@app.route('/list-groups', methods = ['GET', 'POST'])
def list_groups():
    return render_template('list-groups.html')

@app.route('/settings-cults', methods = ['GET', 'POST'])
def settings_cults(): 
    return render_template('settings-cults.html')

@app.route('/list-cults', methods = ['GET', 'POST'])
def list_cults(): 
    return render_template('list-cults.html')