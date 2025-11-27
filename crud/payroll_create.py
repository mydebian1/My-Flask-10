from database import db
from models import Payroll
from sqlalchemy.exc import IntegrityError


def create_payroll_crud(batch_name, staff_id, basic_salary, hourly_rate, monthly_hours, worked_hours, late, leaves, early, bonus1, bonus2):
    try:
        create_payroll = Payroll(
            batch_name = batch_name,
            staff_id = staff_id,
            basic_salary = basic_salary,
            hourly_rate = hourly_rate,
            monthly_hours = monthly_hours,
            worked_hours = worked_hours,
            late = late,
            leaves = leaves,
            early = early,
            bonus1 = bonus1,
            bonus2 = bonus2
        )

        db.session.add(create_payroll)
        db.session.commit()

        return create_payroll
    
    except IntegrityError:
        raise
        
    except Exception:
        raise
