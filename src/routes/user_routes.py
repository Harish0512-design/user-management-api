from datetime import datetime
from flask import Blueprint, request, jsonify
from src.services.user_service import UserService
from src.schemas.user_schema import UserSchema
from marshmallow import ValidationError

user_bp = Blueprint('user_bp', __name__)
user_service = UserService()
user_schema = UserSchema()


@user_bp.errorhandler(ValidationError)
def handle_validation_error(error):
    return jsonify(
        {
            "message": "Invalid input",
            "errors": error.messages,
            "success": False
        }
    ), 400


@user_bp.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.get_json()
        if "dob" not in data:
            return {
                "message": "DOB is missing",
                "success": False
            }, 400

        try:
            data["dob"] = datetime.strptime(data["dob"], "%Y-%m-%d").date()
        except ValueError:
            return {
                "message": "Invalid DOB format, expected YYYY-MM-DD",
                "success": False
            }, 400

        user_data = user_schema.load(data)
        user_id = user_service.create_user(user_data)
        return jsonify({
            "message": "User created successfully.",
            "user_id": user_id,
            "success": True
        }), 201

    except ValidationError as e:
        return handle_validation_error(e)
    except Exception as e:
        return jsonify(
            {
                "message": "An error occurred while creating the user.",
                "error": str(e),
                "success": False
            }
        ), 500


@user_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    try:
        user = user_service.get_user(user_id)
        if user:
            user['_id'] = str(user['_id'])

            if isinstance(user["dob"], datetime):
                user["dob"] = user["dob"].strftime("%Y-%m-%d")

            return jsonify({
                "message": "User retrieved successfully.",
                "data": user,
                "success": True
            }), 200

        return jsonify({
            "message": "User not found",
            "success": False
        }), 404

    except Exception as e:
        return jsonify(
            {
                "message": "An error occurred while retrieving the user.",
                "error": str(e),
                "success": False
            }
        ), 500


@user_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        updated_data = user_schema.load(
            request.get_json(), partial=True)

        if user_service.update_user(user_id, updated_data):
            return jsonify(
                {
                    "message": "User updated",
                    "success": True
                }
            ), 200

        return jsonify(
            {
                "message": "User not found",
                "success": False
            }
        ), 404

    except ValidationError as e:
        return handle_validation_error(e)
    except Exception as e:
        return jsonify(
            {
                "message": "An error occurred while updating the user.",
                "error": str(e),
                "success": False
            }
        ), 500


@user_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        if user_service.delete_user(user_id):
            return jsonify({
                "message": "User deleted",
                "success": True
            }), 200

        return jsonify({
            "message": "User not found",
            "success": False
        }), 404

    except Exception as e:
        return jsonify(
            {
                "message": "An error occurred while deleting the user.",
                "error": str(e),
                "success": False
            }
        ), 500
