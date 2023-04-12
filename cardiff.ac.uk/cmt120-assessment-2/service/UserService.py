from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db
from database import User
from flask_login import login_user


def add_new_user(name: str, email: str, password: str) -> bool:
    """
    Add new user to database with given info
    :param name: name of user
    :param email: email of user
    :param password: password of user
    :return: True if success
    """
    user = User.query.filter_by(
        email=email).first()  # if this returns a user, then the email already exists in database

    if user:  # if a user is found, we want to redirect back to signup page so user can try again
        return False

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return True


def check_user_login(email: str, password: str, remember: bool) -> bool:
    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        return False
    else:
        # if the above check passes, then we know the user has the right credentials

        login_user(user, remember=remember)
        return True


def get_user_by_id(user_id: int) -> User:

    return user
