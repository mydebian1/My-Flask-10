from database import db
from controller.payroll_create import get_payroll_by_username
from sqlalchemy.exc import IntegrityError


def update_payroll_crud(batch_name, staff_id, basic_salary, hourly_rate, monthly_hours, worked_hours, late, leaves, early, bonus1, bonus2):
    payroll = get_payroll_by_username(batch_name, staff_id)

    if not payroll:
        return payroll == False
    
    try:
        if batch_name:
            payroll.batch_name = batch_name

        if staff_id:
            payroll.staff_id = staff_id

        if basic_salary:
            payroll.basic_salary = basic_salary

        if hourly_rate: 
            payroll.hourly_rate = hourly_rate

        if monthly_hours:
            payroll.monthly_hours = monthly_hours

        if worked_hours:
            payroll.worked_hours = worked_hours
        
        if late:
            payroll.late = late

        if leaves:
            payroll.leaves = leaves

        if early:
            payroll.early = early

        if bonus1:
            payroll.bonus1 = bonus1
        
        if bonus2:
            payroll.bonus2 = bonus2

        db.session.commit()

        return payroll
    
    except IntegrityError:
        raise
    
    except Exception:
        raise




