from flask import Flask
from database import init_db
from flask_cors import CORS

from controller.create import create_bp
from controller.update import update_bp
from controller.delete import delete_bp
from controller.get import get_bp

app = Flask (__name__)
CORS(app)

# Point SQLAlchemy to your SQLite database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////home/iotexpert/Documents/web-dev/python/my-flask-10/database/myimab.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize DB
init_db(app)

# Register blueprints
app.register_blueprint(create_bp)
app.register_blueprint(update_bp)
app.register_blueprint(delete_bp)
app.register_blueprint(get_bp)

@app.route("/")
def index():
    return "Wellcome To Flask"

if __name__ == "__main__":
    app.run(debug=True)