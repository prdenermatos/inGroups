from flask import render_template, redirect, request, flash, session
from src import db, app
from src.models.tables import User
from src.services.validation_register_user_services import ValidationRegisterUserServices as VRS
from src.services.cripto_password_service import CriptoPasswordService as CPS

data_mocado_test = []


@app.route('/registration-user', methods = ['GET', 'POST'])
def registration_user():
    return render_template("registration-user.html")

@app.route('/create-user', methods= ['POST'])
def create_user():

    nome = request.form['nome'],
    email = request.form['email'],
    senha = request.form['senha'],

    user = User(nome, email, senha)


    db.session.add(user)
    db.session.commit()


    return redirect('/login')



@app.route('/login')
def login_user():
    return render_template('login.html')

@app.route('/auth', methods= ['POST'])
def auth_user():
    data_user_to_auth = {
        'email': request.form['email'],
        'password': request.form['password'],
    }

    data_find_user = _create_filter_find_user(data_user_to_auth)

    db = ELR()
    try_data_user = db.find_one(index='user', body=data_find_user)


    if (try_data_user):
        user_token = try_data_user['hits']['hits'][0]['_source']['password']
        user_name  = try_data_user['hits']['hits'][0]['_source']['first_name']

        password = CPS(data_user_to_auth['password'])
        avaliableHash =  password.encrypt() == user_token  

        if (avaliableHash == False):
            flash("Usuário ou senha incorretos")
            return redirect('/login')
        else:
            session['user_logger'] = user_token
            return redirect('/plataform')
    
    else: 
        return redirect('/login')



def _create_filter_find_user(request_body: dict) -> dict:
    return  {
        "query": {
            "query_string": {
                "query": f"{request_body['email']}"
            }
        }
    }


@app.route('/logout')
def logout():
    session['user_logger'] = None
    return redirect('/') 
   

    
