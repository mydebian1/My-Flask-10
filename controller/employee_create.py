from flask import Flask, Blueprint, request, jsonify
from crud.employee_create import create_employee_crud
from utils.utils import get_employee_by_username
from sqlalchemy.exc import IntegrityError

create_bp = Blueprint("create_bp", __name__, url_prefix="/employee")

app = Flask (__name__)

@create_bp.route("/create", methods=["POST"])
def create_employee():
    data = request.json
    app.logger.info(f"data: {data}")


    try:
        name = data.get("name")
        email = data.get("email")
        username = data.get("username")
        password = data.get("password")
        role = data.get("role", "guest")

        if not all([name, email, username, password, role]):
            app.logger.error(f"Field Missing: {name} or {email} or {username} or {password} or {role}")
            return jsonify({
                "error": "Missing fields"
            }), 400
        
        exist_employee = get_employee_by_username(username)

        if exist_employee:
            app.logger.error(f"Already Exist: {exist_employee}")
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
                app.logger.info(f"Employee Created: {new_employee}")
                return jsonify({
                    "code": "Employee_Created",
                    "message": f"Employee {username} Is Created Successfully"
                })
            
        except IntegrityError as error:
            app.logger.error(f"Integrity Error Occured: {error}")
            return jsonify({
                "CODE":"INTEGRITY_ERROR",
                "message":f"Integrity error occured for '{username}' creation, please try again. {error}"
            })
        
    except Exception as error:
        app.logger.error(f"Exceptional Error Occured: {error}")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{username}' creation, please try again"
        })

    


   