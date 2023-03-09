import re

def check_password(password):
    security = 5
    if len(password) < 8:
        security -= 1
    if re.search('[0-9]', password) is None:
        security -= 1
    if re.search('[A-Z]', password) is None:
        security -= 1
    if re.search('[a-z]', password) is None:
        security -= 1
    if re.search('[!@#$%^&*_]', password) is None:
        security -= 1
    level = security_level(security)
    return level


def security_level(security):
    if security == 5:
        return 'Very Strong'
    elif security == 4:
        return 'Strong'
    elif security == 3:
        return 'Medium'
    elif security == 2:
        return 'Weak'
    else:
        return 'Very Weak'
    

def common_used_passwords(password):
    with open('passwords.txt', 'r') as file:
        for line in file:
            if password == line.strip():
                return True
        return False



if __name__ == '__main__':
    password = input('Enter the password:')
    print(check_password(password))