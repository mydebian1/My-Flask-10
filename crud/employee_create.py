from database import db
from models import Employee
from sqlalchemy.exc import IntegrityError


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

    except IntegrityError:
        raise

    except Exception:
        raise