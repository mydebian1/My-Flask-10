from flask import Blueprint, Flask, request, jsonify
from crud.payroll_create import create_payroll_crud
from utils.utils import get_payroll_by_username
from sqlalchemy.exc import IntegrityError
from schemas.payroll import CreatePayrollRequest, PayrollResponse, PayrollListResponse

payroll_create_bp = Blueprint("payroll_create_bp", __name__, url_prefix="/payroll")

app = Flask(__name__)

@payroll_create_bp.route('/create', methods = ["POST"])
def create_payroll():

    data = CreatePayrollRequest(request.json)
    app.logger.info(f"Data: {data}")

    if not data.is_valid():
        return jsonify({"error": "Missing Fields"}), 400

    # try:
    #     batch_name = data.get('batch_name', None)
    #     staff_id = data.get('staff_id', 0)
    #     basic_salary = data.get('basic_salary', 0)
    #     hourly_rate = data.get('hourly_rate', 0)
    #     monthly_hours = data.get('monthly_hours', 0)
    #     worked_hours = data.get('worked_hours', 0)
    #     late = data.get('late', 0)
    #     leaves = data.get('leaves', 0)
    #     early = data.get('early', 0)
    #     bonus1 = data.get('bonus1', 0)
    #     bonus2 = data.get('bonus2', 0)

    #     if not all([batch_name, staff_id, basic_salary, hourly_rate, monthly_hours, worked_hours, late, leaves, early, bonus1, bonus2]):
    #         return jsonify({
    #             "error": "Missing Fields"
    #         }), 400
        
    #     exist_payroll = get_payroll_by_username(batch_name, staff_id)

    #     if exist_payroll:
    #         return jsonify({
    #             "code": "Payroll_Already_Exist",
    #             "message": f"This {batch_name} and {staff_id} is already exists, Please try another one"
    #         })
        
    try:
        new_payroll = create_payroll_crud (
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
            "code": "Payroll_Created",
            "message": f"Payroll {data.batch_name} and {data.staff_id} Is Created Successfully"
        })

    except IntegrityError as error:
        print(f"Error: {error}")
        return jsonify({
            "CODE":"IntegrityError_ERROR_OCCURED",
            "message":f"Integrity error occured for '{data.batch_name}' and ''{data.staff_id} creation, please try again {error}"
        })

    except Exception as error:
        print(f"Error: {error}")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{data.batch_name}' and ''{data.staff_id} creation, please try again"
        })





    





