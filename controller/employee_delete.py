from flask import Blueprint, Flask, request, jsonify
from utils.utils import get_employee_by_username
from crud.employee_delete import delete_employee_crud
from sqlalchemy.exc import IntegrityError
from schemas.employee import DeleteEmployeeRequest

delete_bp = Blueprint("delete_bp", __name__, url_prefix="/employee")

app = Flask (__name__)

@delete_bp.route("/delete", methods=["POST"])
def delete_employee():
    data = DeleteEmployeeRequest(request.json)
    app.logger.info(f"Data: {data}")

    if not data.is_valid():
        return jsonify({"error": "Username required"}), 400
    
    username = get_employee_by_username(data.username)

    if not username:
        app.logger.info("Employee doesnt exist.")
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
        app.logger.error(f"Error: {error}")
        return jsonify({
            "code": "IntegrityError",
            "message": f"IntegrityError Error occured for Employee {data.username} deletion {error}"
    })

    except Exception:
        return jsonify({
            "code": "EXCEPTION",
            "message": f"Exception Error occured for Employee {data.username} deletion!"
        })