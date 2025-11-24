from database import db
from controller.payroll_create import get_payroll_by_username
from models import Employee

def get_payroll_username_crud(batch_name, staff_id):
    try: 
        get_payroll = get_payroll_by_username(batch_name, staff_id)
        print(get_payroll)
        return get_payroll
    
    except Exception as error:
        print(f"error: {error}")
        return error


def get_all_payroll_crud():
    try:  
        get_payroll = Employee.query.all()
        db.session.commit()
        return get_payroll
    
    except Exception as error:
        print(f"error: {error}")
        return error