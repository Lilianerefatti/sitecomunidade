import sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'deda5200337483fd9ba3bcfae9008533'
if os.getenv("DATABASE_URL"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
else:
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
    # Caminho absoluto para o banco
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, '..', 'instance', 'comunidade.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

# Inicializa extensões
database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'

from comunidade import models
engine =sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table("usuario"):
# Cria as tabelas se ainda não existirem
    with app.app_context():
        database.DROP_ALL()
        database.create_all()
        print("Base de dados criado")
else:
    print("Base de dados criado já existente")

from comunidade import routes


