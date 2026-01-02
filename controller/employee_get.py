from flask import Blueprint, Flask, request, jsonify, current_app
from crud.employee_get import get_employee_by_username, get_all_employee_crud, get_short_employee_crud
from schemas.employee import EmployeeResponse, EmployeeListResponse, EmployeeShortResponse
from auth import require_auth

get_bp = Blueprint("get_bp", __name__, url_prefix="/employee")


@get_bp.route("/byusername", methods = ["GET"])
@require_auth
def get_employee_username():

    data = request.json
    current_app.logger.info(f"Data: {data}")

    username = data.get("username")

    if not username:
        current_app.logger.error(f"Error {username}")

        return jsonify({
            "Code":"No_Username_Data",
            "message":"Please Enter Your Username"
        }), 403
        

    employee = get_employee_by_username(username=username)
    print(f"employee:{employee}")

    try:
        if employee:
            return EmployeeResponse(employee).to_dict()
        
        else:
            return jsonify({
                "code":"Username_Doesn't_Exist",
                "message": f"Please Try another Username, {username} Is Not Registered"
            }), 403
            
    except Exception as error:
        current_app.logger.error(f"Error {error}")
        return jsonify({
            "code":"Exceptional_Error_Occured",
            "message":f"Exceptional Error Occured For Getting Employee '{username}', Please Try Again"
        })
    

@get_bp.route("/all", methods = ["GET"])
@require_auth
def get_all_employees():

    print('Get All Employee Request Issue')

    try:
        get_employees =  get_all_employee_crud()

        if get_employees:
            return EmployeeListResponse.build(get_employees)
        
        else:
            return {
                "code": "No_Employees_Found",
                "message": "Please Add The Employee First Then Search Here"
            }, 403
            
    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return {
            "code": "Exception_Error_Occured",
            "message": f"Exceptional Error Occured For All Employees, Please Try Again"
        }
    
@get_bp.route("/short", methods = ["GET"])
@require_auth
def get_short_employee():

    try:
        employees = get_short_employee_crud()

        if employees:
            return EmployeeShortResponse.from_list(employees)
        
        else:
            return {
                "code": "No_Short_Employees_Found",
                "message": "Please Add The Employee Name First Then Search Here"
            }, 403
        
    except Exception as e:
        current_app.logger.error(f"Exception Error {e}")
        return {
            "code": "Exception_Error_Occured",
            "message": f"Exceptional Error Occured For Short Employees, Please Try Again"
        }



