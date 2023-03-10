from flask import render_template, redirect, request, flash
from src import app
from src.services.validation_register_user_services import AccessControl as ACL
from src.services.church_service import CreateChurch, EditChurch
from src.services.group_service import CreateGroup, GroupType, UpdateGroup
from src.models.tables import User, Sector, Church, Group
from src.common.locations import Locations


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
    date = str(data_church.create_date)
    cities = [Locations.city['name']]
    districts = Locations.city['districts']
    if data_church == None:
        data_church = {'id': 0} 

    return render_template("settings-church.html", data = data_church, date= date, cities=cities, districts=districts )


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
    isPermit = ACL.avaliable()
    if not isPermit:
        return redirect('/')

    data = {'id': 0}
    cities = [Locations.city['name']]
    districts = Locations.city['districts']
    data_users = User.query.all()
    sectors = Sector.query.all()

    print('-->', data_users)
    print('sec--->', sectors)
    if data_users and len(data_users) == 0: 
        data_users = [{'id': 0}] 
    if sectors and len(sectors) == 0:
        sectors = { 'id': 0}
    

    return render_template("settings-groups.html", cities=cities, districts = districts, data_users=data_users, data=data)


# add crud
@app.route('/add-group', methods=['GET', 'POST', 'UPDATE'])
def add_group():
    group_id = int(request.form['id'])
    print('veio id?', group_id)

    group = Group(
        request.form['create_date'],
        request.form['group_name'],
        request.form['leader_name'],
        request.form['vice_leader_name'],
        request.form['street_number'],
        request.form['district'],
        request.form['city'],
        request.form['sectorId'],
        request.form['host_name'],
        request.form['meeting_day'],
        request.form['meeting_time'],
        request.form['enabled'],
    )

    if group_id == 0 :
        CreateGroup(group).save()
        flash('Cadastro criado com sucesso')
        return render_template('list-groups.html')

    else:
        UpdateGroup(group, group_id).update()
        flash('Cadastro atualizado com sucesso')
        return render_template('list-groups.html')
        
   




@app.route('/list-groups', methods = ['GET', 'POST'])
def list_groups():
    # lista todas as células
    return render_template('list-groups.html')


@app.route('/update-group', methods=['POST'])
def update_group():
    #pegar o id da iteração com input hiden ou na url
    ...

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