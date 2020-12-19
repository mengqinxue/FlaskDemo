from flask import Blueprint, request, render_template, redirect

from app.modules.user.user import User

user_bp = Blueprint('user', __name__)

users = []
users.append(User('max', '123', '12346'))

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

        users.append(User(username, password, phone))
        print(users)
        return redirect('/user/show.html')
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
    return render_template('/user/show.html', users=users)

