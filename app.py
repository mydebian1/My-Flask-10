from flask import Flask
from database import init_db
from flask_cors import CORS
from config import Config

from controller.employee_create import create_bp
from controller.employee_update import update_bp
from controller.employee_delete import delete_bp
from controller.employee_get import get_bp

from controller.payroll_create import payroll_create_bp
from controller.payroll_update import payroll_update_bp
from controller.payroll_delete import payroll_delete_bp
from controller.payroll_get import payroll_get_bp

# Point SQLAlchemy to your SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:iqbal123123@localhost:5432/'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def create_app():
    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # CORS
    CORS(app)

    # Logging
    app.logger.setLevel(app.config["LOG_LEVEL"])
    app.logger.info("test")

    # Initialize DB
    init_db(app)

    # Register EmplFLASK_ENVoyee blueprints
    app.register_blueprint(create_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(delete_bp)
    app.register_blueprint(get_bp)

    #Register Payroll Blueprints
    app.register_blueprint(payroll_create_bp)
    app.register_blueprint(payroll_update_bp)
    app.register_blueprint(payroll_delete_bp)
    app.register_blueprint(payroll_get_bp)


    @app.route("/")
    def index():
        return "Wellcome To Flask"
    
    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=Config.DEBUG)