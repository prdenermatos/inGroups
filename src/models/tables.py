from flask_sqlalchemy import SQLAlchemy
from src import *

class user(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20))
    email = db.Column(db.String(30))
    senha = db.Column(db.String(30))

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


    def __repr__(self):
        return '<Usuario %r>' % self.nome  