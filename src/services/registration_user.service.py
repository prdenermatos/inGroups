from src import db
from src.models.tables import User

class RegistrationUserService:
    def __init__ (self, dtoToSave: list):
        self.data_user_registration = dtoToSave

    def save(self):

        user = User(self.data_user_registration)

        db.session.add(user)
        db.session.commit()

      
    

