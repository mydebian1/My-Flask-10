from flask import Blueprint, request, jsonify
from crud.payroll_create import create_payroll_crud
from utils.utils import get_payroll_by_username

payroll_create_bp = Blueprint("payroll_create_bp", __name__, url_prefix="/payroll")

@payroll_create_bp.route('/create', methods = ["POST"])
def create_payroll():

    data = request.json
    print(data)

    batch_name = data.get('batch_name', None)
    staff_id = data.get('staff_id', 0)
    basic_salary = data.get('basic_salary', 0)
    hourly_rate = data.get('hourly_rate', 0)
    monthly_hours = data.get('monthly_hours', 0)
    worked_hours = data.get('worked_hours', 0)
    late = data.get('late', 0)
    leaves = data.get('leaves', 0)
    early = data.get('early', 0)
    bonus1 = data.get('bonus1', 0)
    bonus2 = data.get('bonus2', 0)

    if not all([batch_name, staff_id, basic_salary, hourly_rate, monthly_hours, worked_hours, late, leaves, early, bonus1, bonus2]):
        return jsonify({
            "error": "Missing Fields"
        }), 400
    
    exist_payroll = get_payroll_by_username(batch_name, staff_id)

    if exist_payroll:
        return jsonify({
            "code": "Payroll_Already_Exist",
            "message": f"This {batch_name} and {staff_id} is already exists, Please try another one"
        })
    
    new_payroll = create_payroll_crud (
        batch_name = batch_name,
        staff_id = staff_id,
        basic_salary = basic_salary,
        hourly_rate = hourly_rate,
        monthly_hours = monthly_hours,
        worked_hours = worked_hours,
        late = late,
        leaves = leaves,
        early = early,
        bonus1 = bonus1,
        bonus2 = bonus2
    )

    try:
        if new_payroll:
            return jsonify({
                "code": "Payroll_Created",
                "message": f"Payroll {batch_name} and {staff_id} Is Created Successfully"
            })
        
    except Exception as error:
        print(f"Error: {error}")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{batch_name}' and ''{staff_id} creation, please try again"
        })





    





