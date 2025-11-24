from database import db
from models import Employee

def delete_payroll_crud(batch_name, staff_id ):
    try:
        delete_query = Employee.query.filter_by(batch_name=batch_name, staff_id=staff_id).first()

        db.session.delete(delete_query)
        db.session.commit()

        return delete_query
        
    except Exception as error:
        print(f"error:{error}")
        return error