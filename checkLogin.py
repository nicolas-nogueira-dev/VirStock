from werkzeug.security import check_password_hash

def checkPassword(userName,password):
    with open(".users", "r") as f:
        rawData = f.read()
        temp = rawData.split("\n")
        temp2 = []
        for _ in temp:
            temp2 += [_.split("|")]
        del temp2[-1]
        users = {}
        for _ in temp2:
            users[_[0]] = {"name":_[0],"password":_[1]}
    try:
        return check_password_hash(users[userName]["password"], str(password))
    except:
        return False
