from database import db
from controller.employee_create import get_employee_by_username
from models import Employee
from sqlalchemy.exc import IntegrityError

def get_employee_username_crud(username):
    try: 
        get_employee = get_employee_by_username(username)
        print(get_employee)
        return get_employee
    
    except IntegrityError as error:
        print(f"error: {error}")
        return error
    
    except Exception as error:
        print(f"error: {error}")
        return error


def get_all_employee_crud():
    try: 
        get_employee = Employee.query.all()
        db.session.commit()
        return get_employee
    
    except IntegrityError as error:
        print(f"error: {error}")
        return error
    
    except Exception as error:
        print(f"error: {error}")
        return error
    
def get_short_employee_crud():
    try:
        employees = Employee.query.with_entities(Employee.id, Employee.name).all()
        db.session.commit()
        return employees
    
    except IntegrityError as error:
        print(f"error: {error}")
        raise error
    
    except Exception as error:
        raise error