from database import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="guest")
    
    def __repr__(self):
        return f"<Employee {self.username}>"
    

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "username": self.username,
            "password": self.password,
            "role": self.role
        }
    
class Payroll(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    staff_id = db.Column(db.Integer, db.ForeignKey('staff_id'), nullable=False )
    batch_name = db.Column(db.String(20), nullable=False)
    basic_salary = db.Column(db.Integer, nullable=False)
    hourly_rate = db.Column(db.Integer, nullable=False)
    monthly_hours = db.Column(db.Integer, nullable=False)
    worked_hours = db.Column(db.Integer, nullable=False)
    late = db.Column(db.Integer, nullable=False)
    leaves = db.Column(db.Integer, nullable=False)
    early = db.Column(db.Integer, nullable=False)
    bonus1 = db.Column(db.Integer, nullable=False)
    bonus2 = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f"<Employee {self.username}>"
    

    def to_dict(self):
        return {
            "id": self.id,
            "staff_id": self.staff_id,
            "batch_name": self.batch_name,
            "basic_salary": self.basic_salary,
            "hourly_rate": self.hourly_rate,
            "monthly_hours": self.monthly_hours,
            "worked_hours": self.worked_hours,
            "late": self.late,
            "leaves": self.leaves,
            "early": self.early,
            "bonus1": self.bonus1,
            "bonus2": self.bonus2,
        }

    @classmethod
    def to_dict_list(cls, payrolls):
        return [emp.to_dict() for emp in payrolls]