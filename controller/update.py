from flask import Blueprint, request, jsonify
from crud.update import update_employee_crud

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
        return jsonify({
            "error": "Username is required"
        }), 400

    employee = update_employee_crud(username=username, name=name, email=email, password=password, role=role)

    if not employee:
        return jsonify({
            "code": "USER_NOT_EXIST",
            "message": f"This {username} Doesn't Exist" 
        }), 403

    if employee:
        return jsonify({
            "code": "Employee_Updated",
            "message": f"Employee {username} updated successfully"
        })
    
    else:
        return jsonify({
            "code": "ERROR",
            "message": f"Employee {username} Is Not Created Due To Some Error!"
        }), 404
    

