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
        

    def has_batch_name(self):
        return self.batch_name is not None

    def has_staff_id(self):
        return self.staff_id is not None
    
    def has_any_updates(self):
        return any([self.basic_salary, self.hourly_rate, self.monthly_hours, self.worked_hours, self.late, self.leaves, self.early, self.bonus1, self.bonus2])


class DeletePayrollRequest:
    def __init__(self, data):
        self.batch_name = data.get("batch_name")
        self.staff_id = data.get("staff_id")

    def is_valid(self):
        return all([self.batch_name, self.staff_id])


class PayrollResponse:
    def __init__(self, payroll):
        self.batch_name = payroll.batch_name
        self.staff_id = payroll.staff_id
        self.basic_salary = payroll.basic_salary
        self.hourly_rate = payroll.hourly_rate
        self.monthly_hours = payroll.monthly_hours
        self.worked_hours = payroll.worked_hours
        self.late = payroll.late
        self.leaves = payroll.leaves
        self.early = payroll.early
        self.bonus1 = payroll.bonus1
        self.bonus2 = payroll.bonus2

    def to_dict(self):
        return {
            "batch_name": self.batch_name,
            "staff_id": self.staff_id,
            "basic_salary": self.basic_salary,
            "hourly_rate": self.hourly_rate,
            "worked_hours": self.monthly_hours,
            "late": self.late,
            "leaves": self.leaves,
            "early": self.early,
            "bonus1": self.bonus1,
            "bonus2": self.bonus2
        }


class PayrollListResponse:
    @staticmethod
    def build(payrolls):
        return [PayrollResponse(emp).to_dict() for emp in payrolls]