def login(username, password):
    if username == "admin" and password == "123456":
        return "Login success"
    else:
        return "Invalid credentials"