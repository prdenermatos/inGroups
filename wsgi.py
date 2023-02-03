from src import *
from flask_sqlalchemy import SQLAlchemy



if __name__ == "__main__":
    app.run(debug=True)
    db.create_all()