from flask import request, Response, Blueprint
from controllers import user_controller

users = Blueprint('users', __name__)

@app.route('/user/add', methods=['POST'])
def add_user() -> Response:
    return user_controller.user_add(request)

@app.route('/user/get-all', methods=['GET'])
def get_all_active_users() -> Response:
    return user_controller.get_all_active_users(request)

