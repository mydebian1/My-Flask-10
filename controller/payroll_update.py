from flask import Blueprint, request, jsonify
from crud.payroll_update import update_payroll_crud

payroll_update_bp = Blueprint("payroll_update_bp", __name__, url_prefix="/payroll")

@payroll_update_bp.route("/update", methods=["PUT"])
def update_payroll():
    data = request.json

    current_batch_name = data.get('current_batch_name')
    current_staff_id = data.get('current_staff_id')
    batch_name = data.get('batch_name')
    staff_id = data.get('staff_id')
    basic_salary = data.get('basic_salary')
    hourly_rate = data.get('hourly_rate')
    monthly_hours = data.get('monthly_hours')
    worked_hours = data.get('worked_hours')
    late = data.get('late')
    leaves = data.get('leaves')
    early = data.get('early')
    bonus1 = data.get('bonus1')
    bonus2 = data.get('bonus2')

    if not batch_name or not staff_id:
        return jsonify ({
            "code": "No_Data_Found",
            "message": "Batch Name And Staff ID Are Required"
        })
    
    payroll = update_payroll_crud(current_batch_name=current_batch_name, current_staff_id=current_staff_id, batch_name=batch_name, staff_id=staff_id, basic_salary=basic_salary, hourly_rate=hourly_rate, monthly_hours=monthly_hours, worked_hours=worked_hours, late=late, leaves=leaves, early=early, bonus1=bonus1, bonus2=bonus2)

    if not payroll:
        return jsonify ({
            "code": "Payroll_Not_Exist",
            "message": f"Please Provide The Correct {current_batch_name} and {current_staff_id}"
        })
    
    if payroll:
        return jsonify ({
            "code": "Payroll_Updated",
            "message": f"Payroll {current_batch_name} And {current_staff_id} Is Updated!"
        })
    
    else:
        return jsonify({
            "code": "ERROR",
            "message": f"Payroll {current_batch_name} And {current_staff_id} Is Not Created Due To Some Error!"
        }), 404
    
    


