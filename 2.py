import re
def usernameValidity(test_string):
    pattern = '^(?=.{8,12}$)(?![_.])(?!.*[_.]{2})[a-z0-9._]+(?<![_.])$'
    if (re.match(pattern, test_string)):
        return bool(True)
    return bool(False)
def passwordValidity(test_string):
    pattern = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$'
    if(re.match(pattern, test_string)):
        return bool(True)
    return bool(False)

print(usernameValidity("johnsmith26"),passwordValidity("j0hn5m!th"))
