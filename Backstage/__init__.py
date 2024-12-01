from flask import Flask, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.models import fsqla_v3 as fsqla
import flask_wtf


from . import config

class Base(DeclarativeBase):
  pass


db = SQLAlchemy(model_class=Base, query_class=Base)
fsqla.FsModels.set_db_info(db)
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    flask_wtf.CSRFProtect(app)

    from Backstage.models import User, Role
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)


    return app


app = create_app()
from .routes import *
