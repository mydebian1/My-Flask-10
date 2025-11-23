from flask import Flask
from database import init_db
from flask_cors import CORS

from controller.employee_create import create_bp
from controller.employee_update import update_bp
from controller.employee_delete import delete_bp
from controller.employee_get import get_bp

from controller.payroll_create import payroll_create_bp

app = Flask (__name__)
CORS(app)

# Point SQLAlchemy to your SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/shahkhan/Documents/Python/creativekhan/My-Flask-10/database/myimab.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize DB
init_db(app)

# Register Employee blueprints
app.register_blueprint(create_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(get_bp)

#Register Payroll Blueprints
app.register_blueprint(payroll_create_bp)

@app.route("/")
def index():
    return "Wellcome To Flask"

if __name__ == "__main__":
    app.run(debug=True)