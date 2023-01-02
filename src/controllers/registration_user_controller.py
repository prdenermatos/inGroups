from flask import render_template, redirect, request, flash, session
from src import app
from src.services.validation_register_user_services import ValidationRegisterUserServices as VRS
from src.services.cripto_password_service import CriptoPasswordService as CPS
from src.db.elasticsearch import connect_db
from src.repository.elasticsearch_repository import ElasticsearchRepository as ELR


data_mocado_test = []


@app.route('/registration-user', methods = ['GET', 'POST'])
def registration_user():
    return render_template("registration-user.html");

@app.route('/create-user', methods= ['POST'])
def create_user():
    data_user_create = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'telephone': request.form['telephone'],
        'address': request.form['address'],
        'city': request.form['city'],
        'email': request.form['email'],
        'password': request.form['password'],
        'password_confirme': request.form['password_confirme'],
    }

    validate_form_submit = VRS(
        data_user_create['first_name'],
        data_user_create['email'],
        data_user_create['telephone'],
        data_user_create['password'], 
        data_user_create['password_confirme'])
    

    
    valid_fields_requerid_logs = validate_form_submit.validate_fields_registration()


    if (len(valid_fields_requerid_logs) > 0):
        for log in valid_fields_requerid_logs: 
            flash(f'{log}')
        return redirect('/registration-user')

    valid_password = validate_form_submit.validate_confirmation_password()

    if (valid_password == False):
        flash("Senha não confirmada")
        return redirect('/registration-user')
    
    to_cripto_password = CPS(data_user_create['password']).encrypt()
    passwor_cripto = {
        'password':  to_cripto_password,
        'password_confirme': '',
    }
    data_user_create.update(passwor_cripto)
    userId = (f'{data_user_create["first_name"]}_{data_user_create["email"]}').upper()

    db = ELR()
    dataRetrived = db.find_document_by_id(index='user', id=userId)
    if (dataRetrived):
        flash("Usurário já cadastrado.")    
        return redirect('/registration-user')
    else:
        db.insert_document(index='user', id=userId, document=data_user_create )
  
    flash("Cadastrado com Sucesso!")    
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
   

    
