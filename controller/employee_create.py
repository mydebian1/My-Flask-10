from flask import Flask, Blueprint, request, jsonify, current_app
from crud.employee_create import create_employee_crud
from utils.utils import get_employee_by_username
from sqlalchemy.exc import IntegrityError
from schemas.employee import CreateEmployeeRequest, EmployeeResponse
from auth import require_auth
# import logging

create_bp = Blueprint("create_bp", __name__, url_prefix="/employee")

# app = Flask (__name__)
# app.logger.setLevel(logging.INFO)

@create_bp.route("/create", methods=["POST"])
@require_auth
def create_employee():

    data = CreateEmployeeRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400

    
    employee_by_username = get_employee_by_username(data.username)

    if employee_by_username:
        current_app.logger.error("Employee Already Exists")
        return jsonify({
                "code": "EMPLOYEE_ALREADY_EXISTS",
                "message": f"This username {data.username} already exists, try a new one"
        }), 403

    try:
        new_employee = create_employee_crud(
            name = data.name,
            email = data.email,
            username = data.username,
            password = data.password,
            role = data.role
        )

        return jsonify({
            "code": "EMPLOYEE_CREATED",
            "data": EmployeeResponse(new_employee).to_dict()
        }), 201

    except IntegrityError as e:
        current_app.logger.error(f"Integrity Error {e}")
        return jsonify({"code": "INTEGRITY_ERROR", "message": str(e)}), 409

    except Exception:
        current_app.logger.error("Exception Error")
        return jsonify({"code": "ERROR"}), 500