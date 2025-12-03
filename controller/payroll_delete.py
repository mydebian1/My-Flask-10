from flask import Blueprint, Flask, request, jsonify
from crud.payroll_delete import delete_payroll_crud
from utils.utils import get_payroll_by_username
from sqlalchemy.exc import IntegrityError
from schemas.payroll import DeletePayrollRequest

payroll_delete_bp = Blueprint("payroll_delete_bp", __name__, url_prefix="/payroll")

app = Flask (__name__)

@payroll_delete_bp.route("/delete", methods=["POST"])
def delete_payroll():

    data = DeletePayrollRequest(request.json)
    app.logger.info(f"Data: {data}")

    if not data.is_valid():
        return jsonify({"error": "Batch Name and Staff ID Are Required"}), 400
    
    
    payroll = get_payroll_by_username(data.batch_name, data.staff_id)

    if not payroll:
        return jsonify({
            "code": "Payroll_Desn't_Exist", 
            "message": f"Payroll Doesn't Exist. Please Enter Your Valid Batch Name '{data.batch_name}' And Staff ID '{data.staff_id}' "
        }), 404
    
    
    try:
        delete_query = delete_payroll_crud(batch_name=data.batch_name, staff_id=data.staff_id)

        if delete_query:
            return jsonify({
                "CODE": "Payroll_DELETED",
                "message": f"Payroll '{data.batch_name}' and '{data.staff_id}' are deleted"
            }), 200
        
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


















    try:
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

        except IntegrityError as error:
            print(f"error: {error}")
            return jsonify({
                "code": "Integrity_Error",
                "message": f"Integrity Error occured for Payroll {batch_name} And {staff_id} deletion {error}"
            })
        
        if delete:
            return jsonify({
                "code": "Payroll_Deleted",
                "message": f"Payroll {batch_name} And {staff_id} Are Deleted Successfully"
            })
        
    except Exception as error:
        print(f"error: {error}")
        return jsonify({
            "code": "EXCEPTION",
            "message": f"Exception Error occured for Payroll {batch_name} And {staff_id} deletion!"
        })

