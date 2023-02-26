from flask import render_template, redirect, request, flash, session
from src import db, app
from src.models.tables import User
from src.services.validation_register_user_services import ValidationRegisterUserServices as VRS
from src.services.cripto_password_service import CriptoPasswordService as CPS
from fileinput import filename
from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    imagem = FileField('Imagem')


def upload():
    form = UploadForm()
    if form.validate_on_submit():
        imagem = form.imagem.data
        filename = secure_filename(imagem.filename)
        imagem.save('uploads/' + filename)
        return 'Upload realizado com sucesso!'



@app.route('/registration-user', methods = ['GET', 'POST'])
def registration_user():
    '''
    implement finds to create forms
    '''
    form = UploadForm()
    


    return render_template("registration-user.html", form=form)

@app.route('/create-user', methods= ['POST'])
def create_user():
    
    first_name = request.form['first_name'],
    last_name = request.form['last_name'],
    office = request.form['office'],
    mother_name = request.form['mother_name'], 
    tel_mother = request.form['tel_mother'], 
    dad_name = request.form['dad_name'], 
    tel_dad = request.form['tel_dad'], 
    date_birth = request.form['date_birth'], 
    date_member = request.form['date_member'], 
    telephone = request.form['telephone'], 
    address = request.form['address'], 
    address_number = request.form['address_number'], 
    district = request.form['district'], 
    city = request.form['city'], 
    #groupId = request.form['group'], trazer o id da celula 
    groupId = 1, 
    isBatism = request.form['isBatism'], 
    email = request.form['email'], 
    password = request.form['password'], 
    password_confirme = request.form['password_confirme'], 

    # validar confirmação de senha
    validations = VRS(password, password_confirme )
    is_Valid = validations.validate_confirmation_password()
    if  is_Valid is False:
        flash('A confirmação da senha não teve sucesso!')
        return redirect('/') 

    # encriptografar senha e reatribuir no password antes de salvar

    passwordData = CPS(password)
    password = passwordData.encrypt()
    

    form = UploadForm()
    if form.validate_on_submit():
        imagem = form.imagem.data
        filename = secure_filename(imagem.filename)
        imagem.save('static/uploads/' + filename)
        hash_foto = filename

    user = User(first_name, last_name, office, mother_name, 
              tel_mother, dad_name, tel_dad, date_birth , 
                date_member, telephone, address, address_number,
                district, city, groupId, isBatism, email, password, hash_foto)

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

    # find no banco 
    user: User = db.session.query(User).filter(User.email == data_user_to_auth['email']).first()
    user_name = user.first_name
    password = CPS(data_user_to_auth['password'])
    avaliableHash =  password.encrypt() == user.password

    if (avaliableHash == False):
        flash("Usuário ou senha incorretos")
        return redirect('/login')
    else:
        session['user_logger'] = user_name
        return redirect('/plataform')
    



@app.route('/logout')
def logout():
    session['user_logger'] = None
    return redirect('/') 
   

    
