from flask import Blueprint, Flask, request, jsonify
from crud.payroll_update import update_payroll_crud
from utils.utils import get_payroll_by_username
from sqlalchemy.exc import IntegrityError
from schemas.payroll import UpdatePayrollRequest, PayrollResponse

payroll_update_bp = Blueprint("payroll_update_bp", __name__, url_prefix="/payroll")

app = Flask(__name__)

@payroll_update_bp.route("/update", methods=["PUT"])
def update_payroll():

    data = UpdatePayrollRequest(request.json)
    valid, message = data.is_valid()

    if not valid:
        app.logger.error(f"Schema error. {message}")
        return jsonify({"error": f"Schema error. {message}"}), 400
    
    if not data.has_any_updates():
        return jsonify({
            "code": "DATA_MISSING", 
            "error": "Required fields for data update not provided"
            }), 400
    
    payroll = get_payroll_by_username(data.batch_name, data.staff_id)

    if not payroll:
        return jsonify({
            "code": "EMPLOYEE_NOT_FOUND", 
            "error": "Required fields for data update not provided"
        }), 404

    try:
        updated_payroll = update_payroll_crud(batch_name=data.batch_name, staff_id=data.staff_id, basic_salary=data.basic_salary, hourly_rate=data.hourly_rate, monthly_hours=data.monthly_hours, worked_hours=data.worked_hours, late=data.late, leaves=data.leaves, early=data.early, bonus1=data.bonus1, bonus2=data.bonus2)

        return jsonify({
            "code": "Payroll_Updated",
            "data": PayrollResponse(updated_payroll).to_dict()
        }), 403
           
    except IntegrityError as error:
        app.logger.error(f"Integrity Error Occured: {error}")
        return jsonify({
            "CODE":"Integrity_ERROR_OCCURED",
            "message":f"Integrity error occured for '{data.batch_name}' and '{data.staff_id}' updation, please try again {error}"
        })
        
    except Exception:
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{data.batch_name}' and '{data.staff_id}' updation, please try again"
        })
    
    


