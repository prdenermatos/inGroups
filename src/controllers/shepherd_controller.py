from flask import render_template, redirect
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/shepherd', methods = ['GET', 'POST'])
def views_sheep():
    # isPermit = ACL.avaliable()
    # if not isPermit:
    #     return redirect('/')

    
    return render_template("shepherd.html");

