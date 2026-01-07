from flask import Blueprint, Flask, request, jsonify, current_app
from crud.payroll_get import get_payroll_by_username, get_all_payroll_crud
from schemas.payroll import PayrollResponse, PayrollListResponse
from auth import require_auth

payroll_get_bp = Blueprint("payroll_get_bp", __name__, url_prefix="/payroll")


@payroll_get_bp.route("/byusername", methods = ["GET"])
@require_auth
def get_payroll_username():

    data = request.json
    current_app.logger.info(f"Data: {data}")

    batch_name = data.get("batch_name")
    staff_id = data.get("staff_id")

    if not batch_name or not staff_id:
        current_app.logger.error(f"Error {batch_name} And {staff_id}")
        return jsonify({
            "code": "Data_Missing",
            "Message": f"No {batch_name} And {staff_id} Are Provided"
        }), 403
    
    payroll = get_payroll_by_username(batch_name=batch_name, staff_id=staff_id)
    print(f"Payroll:{payroll}")

    try:
        if payroll:
            return PayrollResponse(payroll).to_dict()
        
        else: 
            return {
                "code": "Payroll_Dosent_Exists",
                "message": f" Please Try Another Payroll But This {batch_name} And {staff_id} Is Not Found!"
            }, 403
        
    except Exception as error:
        current_app.logger.error(f"Exception Error {error}")
        return jsonify({
            "code":"Exceptional_Error_Occured",
            "message":f"Exceptional Error Occured For Getting Payroll '{batch_name}' And '{staff_id}', Please Try Again"
        })
    

@payroll_get_bp.route("/all", methods = ["GET"])
@require_auth
def get_all_payroll_controller():

    current_app.logger.error('Get All Payroll Request Issue')

    try:
        get_all_payroll =  get_all_payroll_crud()

        if get_all_payroll:
            return PayrollListResponse.build(get_all_payroll)
        
        else:
            return {
                "code": "NO_PAYROLL_FOUND",
                "message": "No Payroll Exist. Please Add Payroll Earlier"
            }, 403
            
    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return {
            "code": "EXCEPTION",
            "message": f"Exception Error Occured For Payroll Deletion!"
        }
