from models import Employee
from models import Payroll

def get_employee_by_username(username):
    employee = Employee.query.filter_by(username=username).first()
    return employee

def get_payroll_by_username(batch_name, staff_id):
    payroll = Payroll.query.filter_by(batch_name=batch_name, staff_id=staff_id).first()
    return payroll