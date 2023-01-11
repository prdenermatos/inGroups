from flask import render_template, redirect
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/schedule', methods = ['GET', 'POST'])
def views_schedule():
    # isPermit = ACL.avaliable()
    # if not isPermit:
    #     return redirect('/')

    
    return render_template("schedule.html")

@app.route('/schedule-add', methods = ['GET', 'POST'])
def schedule_add():
    return render_template('schedule-add.html')