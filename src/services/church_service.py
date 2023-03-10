from src import db
from src.models.tables import Church
from sqlalchemy import update

class CreateChurch:
    def __init__ (self, dtoToSave: dict):
        self.data_church = dtoToSave
    def save(self):
        church: Church = Church(
            self.data_church['date_create'],
             self.data_church['church_name'],
             self.data_church['cnpj'],
             self.data_church['president_name'],
             self.data_church['street_number'],
             self.data_church['disctrict'],
             self.data_church['city'],
             self.data_church['vice_president_name'],
             self.data_church['first_secretary_name'],
             self.data_church['second_secretary_name'],
             self.data_church['first_treasurer_name'], 
             self.data_church['second_treasurer_name']
            )

        db.session.add(church)
        db.session.commit()

class EditChurch:
    def __init__(self) -> None:
        pass
    def find_data(self):
        return Church.query.first()
    def update_data(self, data_update: dict, id_church: int):     
        stmt = update(Church).where(Church.id == id_church).values(
            create_date = data_update['date_create'], 
            church_name= data_update['church_name'],
            cnpj = data_update['cnpj'],
            president_name = data_update['president_name'],
            street_number = data_update['street_number'],
            district = data_update['disctrict'],
            city = data_update['city'],
            vice_president_name = data_update['vice_president_name'],
            first_secretary = data_update['first_secretary_name'],
            second_secretary = data_update['second_secretary_name'],
            first_treasurer = data_update['first_treasurer_name'],
            second_treasurer = data_update['second_treasurer_name']
            )
        
        db.session.execute(stmt)
        db.session.commit()


        

      
    