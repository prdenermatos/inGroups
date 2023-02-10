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

    def __init__(self, id, create_date,
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
        self.id = id
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
    ...

class MissingMembers(db.Model):
    __tablename__ = 'missing_members'
    id = db.Column(db.Integer, primary_key=True)
    ...

class Visitor(db.Model):
    __tablename__ = 'visitor'
    id = db.Column(db.Integer, primary_key=True)
    ...

class Journey(db.Model):
    __tablename__ = 'journey'
    id = db.Column(db.Integer, primary_key=True)
    ...

class VisitorJourney(db.Model):
    __tablename__ = 'visitor_journey'
    id = db.Column(db.Integer, primary_key=True)
    ...

class SupervisionReports(db.Model):
    __tablename__ = 'supervision_reports'
    id = db.Column(db.Integer, primary_key=True)
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

    def __init__(self, id, create_date, group_name, leader_name, vice_leader_name, street_number,
                  district, city, sectorId, host_name, meeting_day, meeting_time,  enabled ):
        
        self.id = id
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
   

    def __init__(self, first_name, last_name, office,
                  mother_name, tel_mother, dad_name, 
                  tel_dad, date_birth, date_member, 
                  telephone, address, address_number, 
                  district, city, groupId, isBatism,
                  email, password
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



