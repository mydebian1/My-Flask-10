from database import db
from models import Employee

def delete_employee_crud(username):
    try:
        delete_query = Employee.query.filter_by(username=username).first()

        db.session.delete(delete_query)
        db.session.commit()

        return delete_query
        
    except Exception as error:
        print(f"error:{error}")
        return error