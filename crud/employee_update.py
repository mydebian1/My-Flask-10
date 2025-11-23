from database import db
from controller.employee_create import get_employee_by_username

def update_employee_crud(name, username, email, password, role):
    employee = get_employee_by_username(username)

    if not employee:
        return employee == False

    try:
        if name:
            employee.name = name

        if email:
            employee.email = email

        if password:
            employee.password = password

        if role:
            employee.role = role

        db.session.commit()

        return employee


    except Exception as e:
        print(f"error: {e}")
        return e