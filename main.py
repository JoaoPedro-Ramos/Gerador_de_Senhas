from secrets import choice
import string

def create_list():
    _list = string.ascii_letters + string.digits + string.punctuation
    return _list

def create_password(password_length=8, _list=create_list()):
    password = [choice(_list) for i in range(password_length)]
    return ''.join(password)

