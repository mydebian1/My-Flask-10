from flask import Blueprint, Flask, request, jsonify
from crud.employee_get import get_employee_by_username, get_all_employee_crud
from models import Employee
from schemas.employee import EmployeeResponse, EmployeeListResponse

get_bp = Blueprint("get_bp", __name__, url_prefix="/employee")

app = Flask (__name__)

@get_bp.route("/byusername", methods = ["GET"])
def get_employee_username():

    data = request.json
    app.logger.info(f"Data: {data}")

    username = data.get("username")

    if not username:
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
        print(f"error:{error}")
        return jsonify({
            "code":"Exceptional_Error_Occured",
            "message":f"Exceptional Error Occured For Getting Employee '{username}', Please Try Again"
        })
    

@get_bp.route("/all", methods = ["GET"])
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
        print(f"Error: {e}")
        return {
            "code": "Exception_Error_Occured",
            "message": f"Exceptional Error Occured For All Employees, Please Try Again"
        }