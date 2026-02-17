from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object('Config')
    

    from .blueprints.main import main_bp
    from .blueprints.main import predict_bp
    from .blueprints.main import api_bp


    app.register_blueprint(main_bp, url_prefix="/")
    app.register_blueprint(predict_bp, url_prefix="/predict")
    app.register_blueprint(api_bp, url_prefix="/api")
    

    return app