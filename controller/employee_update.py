from flask import Blueprint, Flask, request, jsonify, current_app
from crud.employee_update import update_employee_crud
from utils.utils import get_employee_by_username
from sqlalchemy.exc import IntegrityError
from schemas.employee import UpdateEmployeeRequest, EmployeeResponse

update_bp = Blueprint("update_bp", __name__, url_prefix="/employee")

# app = Flask(__name__)

@update_bp.route("/update", methods=["PUT"])
def update_employee():

    data = UpdateEmployeeRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400

    if not data.has_any_updates():
        return jsonify({
            "code": "DATA_MISSING", 
            "error": "Required fields for data update not provided"
            }), 400
    
    employee = get_employee_by_username(data.username)

    if not employee:
        current_app.logger.error(f"Error. {employee}")
        return jsonify({
            "code": "EMPLOYEE_NOT_FOUND", 
            "error": "Required fields for data update not provided"
        }), 404

    try:
        employee = update_employee_crud(username=data.username, name=data.name, password=data.password, role=data.role, email=data.email)

        return jsonify({
            "code": "Employee_Updated",
            "data": EmployeeResponse(employee).to_dict()
        }), 403
    

    except IntegrityError as error:
        current_app.logger.error(f"Integrity Error Occured: {error}")
        return jsonify({
            "CODE":"Integrity_ERROR_OCCURED",
            "message":f"Integrity error occured for '{data.username}' creation, please try again {error}"
        })
    
        
    except Exception:
        current_app.logger.error("Exceptional Error Occured")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{data.username}' creation, please try again"
        })
    

