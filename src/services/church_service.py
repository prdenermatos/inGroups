from src import db
from src.models.tables import Church

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
        

      
    