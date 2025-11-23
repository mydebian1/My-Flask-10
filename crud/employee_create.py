from database import db
from models import Employee

def create_employee_crud(name, email, username, password, role):
    try:
        create_employee = Employee(
            name=name,
            email=email,
            username=username,
            password=password,
            role=role
        )

        db.session.add(create_employee)
        db.session.commit()

        return create_employee
        
    except Exception as error:
        print(f"error:{error}")
        return error