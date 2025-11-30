class CreatePayrollRequest:
    def __init__(self, data):
        self.batch_name = data.get("batch_name")
        self.staff_id = data.get("staff_id")
        self.basic_salary = data.get("basic_salary")
        self.hourly_rate = data.get("hourly_rate")
        self.monthly_hours = data.get("monthly_hours")
        self.worked_hours = data.get("worked_hours")
        self.late = data.get("late")
        self.leaves = data.get("leaves")
        self.early = data.get("early")
        self.bonus1 = data.get("bonus1")
        self.bonus2 = data.get("bonus2")

    def is_valid(self):
        return all([self.batch_name, self.staff_id, self.basic_salary, self.hourly_rate, self.monthly_hours, self.worked_hours, self.late, self.leaves, self.early, self.bonus1, self.bonus2])

class UpdatePayrollRequest:
    def __init__(self, data):
        self.batch_name = data.get("batch_name")
        self.staff_id = data.get("staff_id")
        self.basic_salary = data.get("basic_salary")
        self.hourly_rate = data.get("hourly_rate")
        self.monthly_hours = data.get("monthly_hours")
        self.worked_hours = data.get("worked_hours")
        self.late = data.get("late")
        self.leaves = data.get("leaves")
        self.early = data.get("early")
        self.bonus1 = data.get("bonus1")
        self.bonus2 = data.get("bonus2")
        

    def has_username(self):
        return self.username is not None

    def has_any_updates(self):
        return any([self.batch_name, self.staff_id, self.basic_salary, self.hourly_rate, self.monthly_hours, self.worked_hours, self.late, self.leaves, self.early, self.bonus1, self.bonus2])


class DeletePayrollRequest:
    def __init__(self, data):
        self.batch_name = data.get("batch_name")
        self.staff_id = data.get("staff_id")

    def is_valid(self):
        return all([self.batch_name, self.staff_id])


class PayrollResponse:
    def __init__(self, employee):
        self.id = employee.id
        self.name = employee.name
        self.email = employee.email
        self.username = employee.username
        self.role = employee.role

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "username": self.username,
            "role": self.role
        }


class EmployeeListResponse:
    @staticmethod
    def build(employees):
        return [EmployeeResponse(emp).to_dict() for emp in employees]