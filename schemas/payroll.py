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
        # Required fields
        if not all([self.batch_name, self.staff_id, self.basic_salary, self.hourly_rate, self.monthly_hours, self.worked_hours, self.late, self.leaves, self.early, self.bonus1, self.bonus2]):
            return False, "Missing Required Fields"

        if self.late < 0:
            return False, f"{self.late} Cannot Be Negative"

        if self.leaves < 0:
            return False, f"{self.leaves} Cannot Be Negative"
        
        if self.early < 0:
            return False, f"{self.early} Cannot Be Negative"
        
        if self.bonus1 < 0:
            return False, f"{self.bonus1} Cannot Be Negative"
        
        if self.bonus2 < 0:
            return False, f"{self.bonus2} Cannot Be Negative"
        
        return True, None
        
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
        

    def is_valid(self):
        # Required fields
        if not self.batch_name:
            return False, "Batch name is not provided"
        
        if not self.staff_id:
            return False, "Staff id is not provided"
        
        if self.late < 0:
            return False, f"{self.late} Cannot Be Negative"

        if self.leaves < 0:
            return False, f"{self.leaves} Cannot Be Negative"
        
        if self.early < 0:
            return False, f"{self.early} Cannot Be Negative"
        
        if self.bonus1 < 0:
            return False, f"{self.bonus1} Cannot Be Negative"
        
        if self.bonus2 < 0:
            return False, f"{self.bonus2} Cannot Be Negative"
        
        return True, None
        
    
    def has_any_updates(self):
        return any([self.basic_salary, self.hourly_rate, self.monthly_hours, self.worked_hours, self.late, self.leaves, self.early, self.bonus1, self.bonus2])


class DeletePayrollRequest:
    def __init__(self, data):
        self.batch_name = data.get("batch_name")
        self.staff_id = data.get("staff_id")
        
    def is_valid(self):
        if not all([self.batch_name, self.staff_id]):
            return False, "Username Is Required"
        
        return True, None


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