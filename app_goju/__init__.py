from flask import Flask
from config import Config




def re_app(class_config=Config):
    app = Flask(__name__)
    app.config.from_object(class_config)
    from app_goju.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app_goju.gojudaquan import bp as goju_bp
    app.register_blueprint(goju_bp)
    return app