from flask import Blueprint, request, jsonify
from crud.create import create_employee_crud
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

        return jsonify({
            "error": "Missing fields"
        }), 400
    
    exist_employee = get_employee_by_username(username)

    if exist_employee:
        return jsonify({
                "code": "Employee_Already_Exist",
                "message": f"This {username} is already exists, Please try another one"
            })
    
    new_employee = create_employee_crud(
        name=name,
        email=email,
        username=username,
        password=password,
        role=role
    )

    try:
        if new_employee:
            return jsonify({
                "code": "Employee_Created",
                "message": f"Employee {username} Is Created Successfully"
            })
        
    except Exception as error:
        print(f"Error: {error}")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{username}' creation, please try again"
        })

    


   