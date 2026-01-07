from flask import Blueprint, Flask, request, jsonify, current_app
from crud.payroll_delete import delete_payroll_crud
from utils.utils import get_payroll_by_username
from sqlalchemy.exc import IntegrityError
from schemas.payroll import DeletePayrollRequest
from auth import require_auth

payroll_delete_bp = Blueprint("payroll_delete_bp", __name__, url_prefix="/payroll")


@payroll_delete_bp.route("/delete", methods=["POST"])
@require_auth
def delete_payroll():

    data = DeletePayrollRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        current_app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400
    
    payroll = get_payroll_by_username(data.batch_name, data.staff_id)

    if not payroll:
        current_app.logger.error(f"Payroll Error. {payroll}")
        return jsonify({
            "code": "Payroll_Desn't_Exist", 
            "message": f"Payroll Doesn't Exist. Please Enter Your Valid Batch Name '{data.batch_name}' And Staff ID '{data.staff_id}' "
        }), 404

    
    try:
        delete_query = get_payroll_by_username(batch_name=data.batch_name, staff_id=data.staff_id)

        if delete_query:
            return jsonify({
                "CODE": "Payroll_DELETED",
                "message": f"Payroll '{data.batch_name}' and '{data.staff_id}' are deleted"
            }), 200
        
    except IntegrityError as error:
        current_app.logger.error(f"Integrity Error Occured: {error}")
        return jsonify({
            "CODE":"Integrity_ERROR_OCCURED",
            "message":f"Integrity error occured for '{data.batch_name}' and '{data.staff_id}' updation, please try again {error}"
        })
        
    except Exception:
        current_app.logger.error("Exception Error Occured")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{data.batch_name}' and '{data.staff_id}' updation, please try again"
        })
    