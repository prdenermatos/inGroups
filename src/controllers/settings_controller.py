from flask import render_template, redirect, request, flash
from src import app
from src.services.validation_register_user_services import AccessControl as ACL
from src.services.church_service import CreateChurch, EditChurch
from src.models.tables import Church


@app.route('/menu-settings', methods = ['GET', 'POST'])
def menu_settings():
    isPermit = ACL.avaliable()
    if not isPermit:
        return redirect('/')
    return render_template("menu-settings.html")


@app.route('/settings-church', methods = ['GET', 'POST'])
def settigns_church():
    isPermitonLogger = ACL.avaliable()
   
    if not isPermitonLogger:
        return redirect('/')

    data_church: Church = EditChurch().find_data()
    if data_church == None:
        data_church = {'id': 0} 

    return render_template("settings-church.html", data = data_church)


@app.route('/add-church', methods=['POST'])
def create_settings_church():
    id_church =  request.form['id']
    data_church = {
        'date_create': request.form['date'], 
        'church_name': request.form['church_name'],
        'cnpj': request.form['cnpj'], 
        'president_name': request.form['president_name'],
        'street_number': request.form['street_number'],
        'disctrict': request.form['disctrict'],
        'city': request.form['city'],
        'vice_president_name': request.form['vice_president_name'], 
        'first_secretary_name': request.form['first_secretary_name'],
        'second_secretary_name': request.form['second_secretary_name'],
        'first_treasurer_name': request.form['first_treasurer_name'], 
        'second_treasurer_name': request.form['second_treasurer_name'] 
        }

    if  int(id_church) == 0:
        print('entrou na criação')
        CreateChurch(data_church).save()
        flash('Cadastro realizado com sucesso')

    else:
        print('entrou na edição')
        
        EditChurch().update_data(data_church, id_church)
        flash('Cadastro atualizado com sucesso')
        

    return redirect('/menu-settings')



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


@app.route('/settings-trails', methods = ['GET', 'POST'])
def settings_trails(): 
    return render_template('settings-trails.html')

@app.route('/list-trails', methods = ['GET', 'POST'])
def list_trails(): 
    return render_template('list-trails.html')