from flask import Blueprint, Flask, request, jsonify
from crud.payroll_create import create_payroll_crud
from utils.utils import get_payroll_by_username
from sqlalchemy.exc import IntegrityError
from schemas.payroll import CreatePayrollRequest, PayrollResponse

payroll_create_bp = Blueprint("payroll_create_bp", __name__, url_prefix="/payroll")

app = Flask(__name__)

@payroll_create_bp.route('/create', methods = ["POST"])
def create_payroll():

    data = CreatePayrollRequest(request.json)
    app.logger.info(f"Data: {data}")

    if not data.is_valid():
        return jsonify({"error": "Missing Fields"}), 400
        
    exist_payroll = get_payroll_by_username(data.batch_name, data.staff_id)
    
    if exist_payroll:
        app.logger.error("Payroll already exists.")
        return jsonify({
                "code": "EMPLOYEE_ALREADY_EXISTS",
                "message": f"This {data.batch_name} and {data.staff_id} is already exists, Please try another one"
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
        return jsonify({"code": "INTEGRITY_ERROR", "message": str(error)}), 409

    except Exception:
        return jsonify({"code": "ERROR"}), 500





    





