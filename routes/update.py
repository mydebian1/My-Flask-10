from flask import Blueprint, request, jsonify
from database import db
from routes.create import get_employee_by_username

update_bp = Blueprint("update_bp", __name__, url_prefix="/employee")

@update_bp.route("/update", methods=["PUT"])
def update_employee():
    data = request.json
    username = data.get("username")
    name = data.get("name")
    email = data.get("email")
    role = data.get("role")
    password = data.get("password")

    if not username:
        return jsonify({"error": "Username is required"}), 400

    employee = get_employee_by_username(username)

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    # Update any fields provided
    if name:
        employee.name = name
    
    if email:
        employee.email = email
    
    if role:
        employee.role = role
    
    if password:
        employee.password = password

    db.session.commit()

    return jsonify({"message": "Employee updated successfully"}), 200