from flask import render_template, redirect
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/supervision', methods = ['GET', 'POST'])
def views_supervision():
    # isPermit = ACL.avaliable()
    # if not isPermit:
    #     return redirect('/')

    
    return render_template("supervision.html")

@app.route('/supervisions-add', methods = ['GET', 'POST'])
def add_supervision_report(): 
    print('add_supervision_report')
    return render_template('supervisions-add.html')

@app.route('/supervision-report', methods = ['GET', 'POST'])
def report_supervion():
    return render_template('supervision-report.html')