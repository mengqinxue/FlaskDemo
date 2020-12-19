from flask import Blueprint, request, render_template, redirect

from database import db
from app.modules.user.module import UserModule


user_bp = Blueprint('user', __name__)


@user_bp.route('/user')
def user_center():
    return 'user operations'


@user_bp.route('/user/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        if request.form.get('password') != request.form.get('repassword'):
            return render_template('/user/register.html')
        else:
            password = request.form.get('password')
        phone = request.form.get('phone')

        # Create data module
        user = UserModule(username, password, phone)
        print(user)

        # Create user buffer
        db.session.add(user)

        # Commit
        db.session.commit()
        return 'Register Successfully!'
    else:
        return render_template('/user/register.html')


@user_bp.route('/user/login', methods=['GET', 'POST'])
def login():
    return 'user login'


@user_bp.route('/user/logout', methods=['GET', 'POST'])
def logout():
    return 'user logout'

@user_bp.route('/user/show', methods=['GET', 'POST'])
def show():
    return render_template('/user/show.html')

