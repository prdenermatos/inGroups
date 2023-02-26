from flask import render_template, redirect
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/plataform', methods = ['GET', 'POST'])
def plataform_access():
    isPermit = ACL.avaliable()
    if not isPermit:
        return redirect('/')
    return render_template("plataform.html")

