from flask import Blueprint, Flask, request, jsonify
from crud.employee_update import update_employee_crud
from sqlalchemy.exc import IntegrityError


update_bp = Blueprint("update_bp", __name__, url_prefix="/employee")

app = Flask(__name__)

@update_bp.route("/update", methods=["PUT"])
def update_employee():
    data = request.json
    app.logger.info(f"Data: {data}")

    try:
        username = data.get("username")
        name = data.get("name")
        email = data.get("email")
        role = data.get("role")
        password = data.get("password")

        if not username:
            return jsonify({
                "error": "Username is required"
            }), 400

        try:
            employee = update_employee_crud(username=username, name=name, email=email, password=password, role=role)
            
            if not employee:
                return jsonify({
                    "code": "USER_NOT_EXIST",
                    "message": f"This {username} Doesn't Exist" 
                }), 403

        except IntegrityError as error:
            app.logger.error(f"Integrity Error Occured: {error}")
            return jsonify({
                "CODE":"Integrity_ERROR_OCCURED",
                "message":f"Integrity error occured for '{username}' creation, please try again {error}"
            })
        

        if employee:
            return jsonify({
                "code": "Employee_Updated",
                "message": f"Employee {username} updated successfully"
            })
        
    except Exception as error:
        app.logger.error(f"Exceptional Error Occured: {error}")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{username}' creation, please try again"
        })
    

