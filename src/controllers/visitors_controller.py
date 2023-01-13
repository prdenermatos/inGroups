from flask import render_template
from src import app
from src.services.validation_register_user_services import AccessControl as ACL

@app.route('/visitors_journey', methods = ['GET', 'POST'])
def views_visitors_journey():
    # isPermit = ACL.avaliable()
    # if not isPermit:
    #     return redirect('/')

    
    return render_template("visitors-journey.html")

@app.route('/visitor-add', methods =['GET', 'POST'])
def add_visitors():
    return render_template("visitor-add.html")