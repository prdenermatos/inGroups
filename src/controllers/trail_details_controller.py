from flask import render_template, redirect
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/trail_details', methods = ['GET', 'POST'])
def views_trail_details():
    # isPermit = ACL.avaliable()
    # if not isPermit:
    #     return redirect('/')

    
    return render_template("trail_details.html");

