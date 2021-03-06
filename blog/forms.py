from blog.models import User
from blog.security import check_password_hash


async def validate_login_form(form):
    error = None

    username = form['username']
    password = form['password']

    if not username:
        return 'username is required'
    if not password:
        return 'password is required'

    user = await User.query.where(User.username == username).gino.first()
    if not user:
        return 'Invalid username'
    if not check_password_hash(password, user.password_hash):
        return 'Invalid password'
    else:
        return None

    return 'error'
