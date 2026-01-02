from flask import Blueprint, Flask, request, jsonify, current_app
from utils.utils import get_employee_by_username
from crud.employee_delete import delete_employee_crud
from sqlalchemy.exc import IntegrityError
from schemas.employee import DeleteEmployeeRequest
from auth import require_auth

delete_bp = Blueprint("delete_bp", __name__, url_prefix="/employee")


@delete_bp.route("/delete", methods=["POST"])
@require_auth
def delete_employee():

    data = DeleteEmployeeRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400
    
    username = get_employee_by_username(data.username)

    if not username:
        current_app.logger.info("Employee Doesnt Exist")
        return jsonify({
            "CODE": "EMPLOYEE_DOESNT_EXIST",
            "message": "Employee doesnt exist, please enter a valid username"
        })

    try:
        delete = delete_employee_crud(username=data.username)

        if delete:
            return jsonify({
                "CODE": "EMPLOYEE_DELETED",
                "message": f"Employee '{data.username}' is deleted"
            }), 200
        
    except IntegrityError as error:
        current_app.logger.error(f"Error: {error}")
        return jsonify({
            "code": "IntegrityError",
            "message": f"IntegrityError Error occured for Employee {data.username} deletion {error}"
    })

    except Exception:
        current_app.logger.error("Exception Error")
        return jsonify({
            "code": "EXCEPTION",
            "message": f"Exception Error occured for Employee {data.username} deletion!"
        })