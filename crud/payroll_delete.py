from database import db
from models import Payroll
from sqlalchemy.exc import IntegrityError

def delete_payroll_crud(batch_name, staff_id ):
    try:
        delete_query = Payroll.query.filter_by(batch_name=batch_name, staff_id=staff_id).first()

        db.session.delete(delete_query)
        db.session.commit()

        return delete_query
    
    except IntegrityError:
        raise

    except Exception:
        raise