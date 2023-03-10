from src import *

class Church(db.Model):
    __tablename__ = 'church'

    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.String(100))
    church_name = db.Column(db.String(100))
    cnpj = db.Column(db.String(100))
    president_name = db.Column(db.String(100))
    street_number = db.Column(db.String(100))
    district =db.Column(db.String(100))
    city = db.Column(db.String(100))
    vice_president_name = db.Column(db.String(100))
    first_secretary = db.Column(db.String(100))
    second_secretary = db.Column(db.String(100))
    first_treasurer = db.Column(db.String(100))
    second_treasurer =db.Column(db.String(100))

    def __init__(self, create_date,
                  church_name, cnpj,
                    president_name,
                    street_number,
                    district, city,
                    vice_president_name, 
                    first_secretary, 
                    second_secretary, 
                    first_treasurer, 
                    second_treasurer
                    ):
      
        self.create_date = create_date
        self.church_name = church_name
        self.cnpj = cnpj
        self.president_name = president_name
        self.street_number = street_number
        self.district = district
        self.city = city
        self.vice_president_name = vice_president_name
        self.first_secretary = first_secretary
        self.second_secretary = second_secretary
        self.first_treasurer = first_treasurer
        self.second_treasurer = second_treasurer
    
    def __repr__(self):
        return '<Church %r>' % self.church_name  

class Cults(db.Model):
    __tablename__ = 'cults'

    id = db.Column(db.Integer, primary_key=True)
    create_date = db.Column(db.String(100))
    cult_name = db.Column(db.String(100))
    leader_name = db.Column(db.String(100))
    frequency = db.Column(db.Enum('semanal', 'quinzenal', 'mensal', 'bimestral'))
    meeting_day_time = db.Column(db.String(100))
    meeting_time_start = db.Column(db.String(100))
    meeting_time_end = db.Column(db.String(100))
    enabled =  db.Column(db.Integer)

    def __init__(self, id, create_date, cult_name, leader_name, frequency,
                  meeting_day_time, meeting_time_start, meeting_time_end, 
                  enabled):
        
        self.id = id 
        self.create_date = create_date 
        self.cult_name = cult_name 
        self.leader_name = leader_name 
        self.frequency = frequency 
        self.meeting_day_time = meeting_day_time 
        self.meeting_time_start = meeting_time_start 
        self.meeting_time_end = meeting_time_end
        self.enabled = enabled
    
        def __repr__(self):
            return '<Cults %r>' % self.cult_name
        


class Schedule(db.Model):
    __tablename__ = 'schedule'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100))
    user_leader = db.Column(db.String(100))
    event_type =  db.Column(db.Enum('Culto', 'Conferência', 'Treinamento', 'Outros'))
    initial_date = db.Column(db.String(100))
    finaly_date =db.Column(db.String(100))
    description = db.Column(db.String(100))
    event_name = db.Column(db.String(100))


    def __init__(self, id, event_name, user_leader, event_type, initial_date, finaly_date, description, folder_name):
        self.id = id 
        self.event_name = event_name
        self.user_leader = user_leader 
        self.event_type = event_type 
        self.initial_date = initial_date 
        self.finaly_date = finaly_date 
        self.description = description
        self.folder_name = folder_name
        
    
    def __repr__(self):
        return '<Schedule %r>' % self.event_name


class Visitor(db.Model):
    __tablename__ = 'visitor'
    id = db.Column(db.Integer, primary_key=True)
    visitor_name = db.Column(db.String(100))
    visitor_date =db.Column(db.String(100))
    contact_telephone = db.Column(db.String(100))
    street_number = db.Column(db.String(100))
    district = db.Column(db.String(100))
    host_visitor = db.Column(db.String(100))
    escort_name = db.Column(db.String(100))
    visitor_cult =  db.Column(db.String(100))
    is_frequency_group = db.Column(db.String(100))
    is_member_church = db.Column(db.String(100))
    enabled = db.Column(db.Integer)

    def __init__(self, id, visitor_name, visitor_date, contact_telephone, 
                 street_number, district, host_visitor, escort_name, visitor_cult, 
                 is_frequency_group, is_member_church, enabled):
        self.id = id 
        self.visitor_name = visitor_name
        self.visitor_date = visitor_date
        self.contact_telephone = contact_telephone
        self.street_number = street_number 
        self.district = district 
        self.host_visitor = host_visitor
        self.escort_name = escort_name 
        self.visitor_cult = visitor_cult 
        self.is_frequency_group = is_frequency_group
        self.is_member_church = is_member_church
        self.enabled = enabled

    def __repr__(self):
        return '<Visitor %r>' % self.visitor_name


class JourneyStepper(db.Model): # (add crud in front)
    __tablename__ = 'journey'
    id = db.Column(db.Integer, primary_key=True)
    stepper_name = db.Column(db.String(100))
    enabled = db.Column(db.Integer)

    def __init__(self, id, stepper_name, enabled) -> None:
        self.id = id 
        self.stepper_name = stepper_name 
        self.enabled = enabled 
    
    def __repr__(self) -> str:
        return '<JourneyStepper %r>' % self.stepper_name

    

class VisitorJourney(db.Model): #many_to_many 
    __tablename__ = 'visitor_journey'

    visitorId =  db.Column(db.ForeignKey(Visitor.id), primary_key = True)
    journeyStepperId =  db.Column(db.ForeignKey(JourneyStepper.id), primary_key = True)

    def __init__(self, visitorId, journeyStepperId):
        self.visitorId = visitorId 
        self.journeyStepperId = journeyStepperId


    def __repr__(self):
        return '<VisitorJourney %r>' % self.visitorId  
    
    ...


class Network(db.Model):
    __tablename__ = 'network'
    id = db.Column(db.Integer, primary_key=True)
    network_name = db.Column(db.String(100))
    leader_name = db.Column(db.String(100))


    def __init__(self, id, network_name, leader_name):
        self.id = id
        self.network_name = network_name
        self.leader_name = leader_name
    
    def __repr__(self):
        return '<Network %r>' % self.network_name  


class Sector(db.Model):
    __tablename__ = 'sector'
    id = db.Column(db.Integer, primary_key=True)
    sector_name = db.Column(db.String(100))
    leader_name = db.Column(db.String(100))
    networkId = db.Column(db.ForeignKey(Network.id))

    def __init__(self, id, sector_name, leader_name, networkId):
        self.id = id
        self.sector_name = sector_name
        self.leader_name = leader_name
        self.networkId = networkId
    
    def __repr__(self):
        return '<Sector %r>' % self.sector_name 

class Group(db.Model):
    __tablename__ = 'group'

    id = db.Column(db.Integer, primary_key=True )
    create_date = db.Column(db.String(100))
    group_name =  db.Column(db.String(100))
    leader_name = db.Column(db.String(100))
    vice_leader_name = db.Column(db.String(100))
    street_number = db.Column(db.String(100))
    district = db.Column(db.String(100))
    city = db.Column(db.String(100))
    sectorId = db.Column(db.ForeignKey(Sector.id)) 
    host_name = db.Column(db.String(100))
    meeting_day = db.Column(db.String(100))
    meeting_time = db.Column(db.String(100))
    enabled = db.Column(db.Integer)

    def __init__(self, create_date, group_name, leader_name, vice_leader_name, street_number,
                  district, city, sectorId, host_name, meeting_day, meeting_time,  enabled ):
        
        self.create_date = create_date
        self.group_name = group_name
        self.leader_name = leader_name
        self.vice_leader_name = vice_leader_name
        self.street_number = street_number 
        self.district = district
        self.city = city 
        self.sectorId = sectorId
        self.host_name = host_name
        self.meeting_day = meeting_day
        self.meeting_time = meeting_time
        self.enabled = enabled
    
    def __repr__(self):
        return '<Group %r>' % self.group_name

class Reports(db.Model):
    __tablename__ = 'reports'
    id = db.Column(db.Integer, primary_key=True) 
    groupId = db.Column(db.ForeignKey(Group.id))
    meeting_date = db.Column(db.String(100))
    total_members = db.Column(db.Integer)
    total_visitors = db.Column(db.Integer)
    total_mdas = db.Column(db.Integer)
    total_children = db.Column(db.Integer)
    total_frequency_cult_celebration = db.Column(db.Integer)
    total_frequency_cult_renove = db.Column(db.Integer)
    total_offers = db.Column(db.Integer)


class MissingMembers(db.Model):
    __tablename__ = 'missing_members'
    
    userId =  db.Column(db.Integer)
    reportId =  db.Column(db.ForeignKey(Reports.id), primary_key = True)
    groupId = db.Column(db.ForeignKey(Group.id), primary_key = True)
    missing_date = db.Column(db.DateTime, server_default=db.func.now())


    def __init__(self, userId, reportId, groupId, missing_date ):
        self.userId = userId 
        self.reportId = reportId
        self.groupId = groupId
        self.missing_date = missing_date


    def __repr__(self):
        return '<UserTrail %r>' % self.userId  


class Ministry(db.Model):
    __tablename__ = 'ministry'

    id = db.Column(db.Integer, primary_key=True )
    ministry_name = db.Column(db.String(100))
    leader_name = db.Column(db.String(100))
    enabled = db.Column(db.Integer)


    def __init__(self, id, ministry_name, leader_name, enabled):
        self.id = id 
        self.ministry_name = ministry_name 
        self.leader_name = leader_name 
        self.enabled = enabled 

    def __repr__(self):
        return '<Ministry %r>' % self.ministry_name


class Office(db.Model):
    __tablename__ = 'office'

    id = db.Column(db.Integer, primary_key=True )
    office_name = db.Column(db.String(100))
    leader_name = db.Column(db.String(100))
    enabled = db.Column(db.Integer)


    def __init__(self, id, office_name, leader_name, enabled):
        self.id = id 
        self.office_name = office_name 
        self.leader_name = leader_name 
        self.enabled = enabled 

    def __repr__(self):
        return '<Office %r>' % self.office_name

class Trail(db.Model):
    __tablename__ = 'trail'

    id = db.Column(db.Integer, primary_key=True)
    trail_name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    enabled = db.Column(db.Integer)

    def __init__(self, id, trail_name, enabled):
        self.id = id
        self.trail_name = trail_name 
        self.enabled = enabled
    
    def __repr__(self):
        return '<Trail %r>' % self.trail_name

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    office = db.Column(db.String(100))
    mother_name = db.Column(db.String(100))
    tel_mother = db.Column(db.String(100)) 
    dad_name =db.Column(db.String(100))
    tel_dad = db.Column(db.String(100))
    date_birth = db.Column(db.String(100))
    date_member = db.Column(db.String(100)) 
    telephone = db.Column(db.String(100)) 
    address = db.Column(db.String(100)) 
    address_number = db.Column(db.String(100)) 
    district = db.Column(db.String(100))
    city = db.Column(db.String(100))
    groupId = db.Column(db.ForeignKey(Group.id))  
    isBatism = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    hash_foto =  db.Column(db.String(100))
   

    def __init__(self, first_name, last_name, office,
                  mother_name, tel_mother, dad_name, 
                  tel_dad, date_birth, date_member, 
                  telephone, address, address_number, 
                  district, city, groupId, isBatism,
                  email, password, hash_foto
                    ):
         
        self.first_name = first_name
        self.last_name = last_name
        self.office = office
        self.mother_name = mother_name
        self.tel_mother =tel_mother
        self.dad_name = dad_name
        self.tel_dad = tel_dad
        self.date_birth = date_birth
        self.date_member = date_member
        self.telephone = telephone
        self.address = address
        self.address_number = address_number
        self.district = district
        self.city = city
        self.groupId = groupId
        self.isBatism = isBatism
        self.email = email
        self.password = password
        self.hash_foto = hash_foto 

    def __repr__(self):
        return '<Usuario %r>' % self.first_name  
    
class UserTrail(db.Model):
    __tablename__ = 'user_trail'

    userId =  db.Column(db.ForeignKey(User.id), primary_key = True)
    trailId =  db.Column(db.ForeignKey(Trail.id), primary_key = True)

    def __init__(self, userId, trailId):
        self.userId = userId 
        self.trailId = trailId


    def __repr__(self):
        return '<UserTrail %r>' % self.userId  


class SupervisionReports(db.Model):
    __tablename__ = 'supervision_reports'
    id = db.Column(db.Integer, primary_key=True)
    supervion_by_userId = db.Column(db.ForeignKey(User.id)) 
    groupId = db.Column(db.ForeignKey(Group.id)) 
    supervison_date = db.Column(db.String(100))
    description_strengths_points = db.Column(db.String(225))
    description_negative_points = db.Column(db.String(225))
    evangelism_points = db.Column(db.Integer)
    integration_points = db.Column(db.Integer)
    communion_points = db.Column(db.Integer)
    discipleship_points = db.Column(db.Integer)
    training_points =db.Column(db.Integer)
    multiplication_points = db.Column(db.Integer)
    is_potentiality = db.Column(db.Integer)
    is_organized_environment = db.Column(db.Integer)
    is_cleaning_after_meeting = db.Column(db.Integer)
    is_notices_made = db.Column(db.Integer)
    is_excellent_reception = db.Column(db.Integer)

    def __init__(self, id, supervion_by_userId, groupId, supervison_date, description_strengths_points,
                 description_negative_points, evangelism_points, communion_points, discipleship_points, 
                  training_points, multiplication_points, is_potentiality, is_organized_environment, 
                is_cleaning_after_meeting,  is_notices_made, is_excellent_reception  ):
        self.id = id 
        self.supervion_by_userId = supervion_by_userId
        self.groupId = groupId 
        self.supervison_date = supervison_date
        self.description_strengths_points = description_strengths_points 
        self.description_negative_points = description_negative_points 
        self.evangelism_points = evangelism_points 
        self.communion_points = communion_points 
        self.discipleship_points = discipleship_points 
        self.training_points = training_points 
        self.multiplication_points = multiplication_points 
        self.is_potentiality = is_potentiality
        self.is_organized_environment = is_organized_environment
        self.is_cleaning_after_meeting = is_cleaning_after_meeting 
        self.is_notices_made = is_notices_made 
        self.is_excellent_reception = is_excellent_reception
    
    def __repr__(self):
        return '<SupervisionReports %r>' % self.id





