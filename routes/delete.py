from flask import Blueprint, request, jsonify
from database import db
from models import Employee

delete_bp = Blueprint("delete_bp", __name__, url_prefix="/employee")

@delete_bp.route("/delete", methods=["DELETE"])
def delete_employee():
    data = request.json
    username = data.get("username")

    if not username:
        return jsonify({"error": "Username required"}), 400

    employee = Employee.query.filter_by(username=username).first()

    if not employee:
        return jsonify({"error": "Employee not found"}), 404

    db.session.delete(employee)
    db.session.commit()

    return jsonify({"message": "Employee deleted successfully"}), 200