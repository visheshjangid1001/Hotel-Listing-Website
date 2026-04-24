from flask import Flask, g, session

from app.auth import auth_bp
from app.config import Config
from app.extensions import db
from app.main import main_bp
from app.models import User


def create_app(config_class=Config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    @app.before_request
    def load_current_user():
        user_id = session.get("user_id")
        g.user = User.query.get(user_id) if user_id else None

    @app.context_processor
    def inject_user():
        return {"current_user": g.get("user")}

    return app
