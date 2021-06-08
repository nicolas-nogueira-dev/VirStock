from werkzeug.security import generate_password_hash

name = input("name : ")
sercure_password = generate_password_hash(input("password : "))

with open(".users", "a") as f:
    f.write(f"{name}|{sercure_password}\n")
