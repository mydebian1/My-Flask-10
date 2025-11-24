from flask import Blueprint, request, jsonify
from controller.payroll_create import get_payroll_by_username
from crud.payroll_delete import delete_payroll_crud

payroll_delete_bp = Blueprint("payroll_delete_bp", __name__, url_prefix="/payroll")

@payroll_delete_bp.route("/delete", methods=["POST"])
def delete_payroll():
    data = request.json

    staff_id = data.get("staff_id")
    batch_name = data.get("batch_name")

    if not staff_id or not batch_name: 
        return jsonify({
            "code": "Data_Missing",
            "message": f"Your {batch_name} And {staff_id} Are Required"
        })
    
    exist_payroll = get_payroll_by_username(batch_name, staff_id)

    if not exist_payroll:
        return jsonify({
                "code": "Payroll_NOT_EXIST",
                "message": f"This {batch_name} and {staff_id} is not exists, please try another one"
            })

    try:
        delete = delete_payroll_crud(batch_name=batch_name, staff_id=staff_id)

        if delete:
            return jsonify({
                "code": "Payroll_Deleted",
                "message": f"Payroll {batch_name} And {staff_id} Are Deleted Successfully"
            })
        
    except Exception as error:
        print(f"error: {error}")
        return jsonify({
            "code": "EXCEPTION",
            "message": f"Exception Error occured for Employee {batch_name} And {staff_id} deletion!"
        })

