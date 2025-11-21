from flask import Blueprint, request, jsonify
from database import db
from models import Employee

create_bp = Blueprint("create_bp", __name__, url_prefix="/employee")

def get_employee_by_username(username):
    employee = Employee.query.filter_by(username=username).first()
    return employee

@create_bp.route("/create", methods=["POST"])
def create_employee():
    data = request.json

    name = data.get("name")
    email = data.get("email")
    username = data.get("username")
    password = data.get("password")
    role = data.get("role", "guest")

    if not all([name, email, username, password, role]):
        return jsonify({"error": "Missing fields"}), 400
    
    get_employee = get_employee_by_username(username)

    if get_employee:
        return jsonify({"error": "Employee already exist"}), 404
    

    return jsonify({"message": "Employee created successfully"}), 200