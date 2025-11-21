from flask import Blueprint, request, jsonify
from controller.create import get_employee_by_username
from crud.delete import delete_employee_crud

delete_bp = Blueprint("delete_bp", __name__, url_prefix="/employee")

@delete_bp.route("/delete", methods=["POST"])
def delete_employee():
    data = request.json
    username = data.get("username")

    if not username: 
        return jsonify({
            "code": "Data_Missing",
            "message": "Username Required"
        })
    
    exist_employee = get_employee_by_username(username)

    if not exist_employee:
        return jsonify({
                "code": "EMPLOYEE_NOT_EXIST",
                "message": f"This {username} is not exists, Please try another one"
            })

    try:
        delete = delete_employee_crud(username=username)

        if delete:
            return jsonify({
                "code": "Employee_Deleted",
                "message": f"Employee {username} Is Deleted Successfully"
            })
        
    except Exception as error:
        print(f"error: {error}")
        return jsonify({
            "code": "EXCEPTION",
            "message": f"Exception Error occured for Employee {username} deletion!"
        })