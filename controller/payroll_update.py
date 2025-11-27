from flask import Blueprint, Flask, request, jsonify
from crud.payroll_update import update_payroll_crud
from sqlalchemy.exc import IntegrityError

payroll_update_bp = Blueprint("payroll_update_bp", __name__, url_prefix="/payroll")

app = Flask(__name__)

@payroll_update_bp.route("/update", methods=["PUT"])
def update_payroll():
    data = request.json
    app.logger.info(f"Data: {data}")

    try:
        current_batch_name = data.get("current_batch_name")
        current_staff_id = data.get("current_staff_id")
        batch_name = data.get("batch_name")
        staff_id = data.get("staff_id")
        basic_salary = data.get("basic_salary")
        hourly_rate = data.get("hourly_rate")
        monthly_hours = data.get("monthly_hours")
        worked_hours = data.get("worked_hours")
        late = data.get("late")
        leaves = data.get("leaves")
        early = data.get("early")
        bonus1 = data.get("bonus1")
        bonus2 = data.get("bonus2")

        if not batch_name or not staff_id:
            return jsonify ({
                "code": "No_Data_Found",
                "message": "Batch Name And Staff ID Are Required"
            })
        
        try:
            payroll = update_payroll_crud(current_batch_name=current_batch_name, current_staff_id=current_staff_id, batch_name=batch_name, staff_id=staff_id, basic_salary=basic_salary, hourly_rate=hourly_rate, monthly_hours=monthly_hours, worked_hours=worked_hours, late=late, leaves=leaves, early=early, bonus1=bonus1, bonus2=bonus2)

            if not payroll:
                return jsonify ({
                    "code": "Payroll_Not_Exist",
                    "message": f"Please Provide The Correct {current_batch_name} and {current_staff_id}"
                })
            
        except IntegrityError as error:
            app.logger.error(f"Integrity Error Occured: {error}")
            return jsonify({
                "CODE":"Integrity_ERROR_OCCURED",
                "message":f"Integrity error occured for '{current_batch_name}' And '{current_staff_id}' creation, please try again {error}"
        })

        if payroll:
            return jsonify ({
                "code": "Payroll_Updated",
                "message": f"Payroll {current_batch_name} And {current_staff_id} Is Updated!"
            })
    
    except Exception as error:
        app.logger.error(f"Exceptional Error Occured: {error}")
        return jsonify({
            "CODE":"EXCEPTIONAL_ERROR_OCCURED",
            "message":f"Exceptional error occured for '{current_batch_name}' And '{current_staff_id}' creation, please try again"
        })
    
    


