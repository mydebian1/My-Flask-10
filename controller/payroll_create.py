from flask import Blueprint, Flask, request, jsonify, current_app
from crud.payroll_create import create_payroll_crud
from utils.utils import get_payroll_by_username
from sqlalchemy.exc import IntegrityError
from schemas.payroll import CreatePayrollRequest, PayrollResponse
from auth import require_auth

payroll_create_bp = Blueprint("payroll_create_bp", __name__, url_prefix="/payroll")


@payroll_create_bp.route('/create', methods = ["POST"])
@require_auth
def create_payroll():

    data = CreatePayrollRequest(request.json)
    current_app.logger.info(f"Data: {data}")

    if not data.is_valid():
        return jsonify({"error": "Missing Fields"}), 400
        
    exist_payroll = get_payroll_by_username(data.batch_name, data.staff_id)
    
    if exist_payroll:
        current_app.logger.error("Payroll Already Exists")
        return jsonify({
                "code": "PAYROLL_ALREADY_EXISTS",
                "message": f"This Batch Name {data.batch_name} and Staff ID {data.staff_id} is already exists, Please try another one"
        }), 403
        
    try:
        new_payroll = create_payroll_crud(
            batch_name = data.batch_name,
            staff_id = data.staff_id,
            basic_salary = data.basic_salary,
            hourly_rate = data.hourly_rate,
            monthly_hours = data.monthly_hours,
            worked_hours = data.worked_hours,
            late = data.late,
            leaves = data.leaves,
            early = data.early,
            bonus1 = data.bonus1,
            bonus2 = data.bonus2
        )
    
        return jsonify({
            "code": "Payroll_CREATED",
            "data": PayrollResponse(new_payroll).to_dict()
        }), 201
    
    except IntegrityError as error:
        current_app.logger.error(f"Integrity Error {error}")
        return jsonify({"code": "INTEGRITY_ERROR", "message": str(error)}), 409

    except Exception:
        current_app.logger.error("Exception Error")
        return jsonify({"code": "ERROR"}), 500





    





