def login(username, password):
    if username == "admin" and password == "1234":
        return "Login success"
    else:
        return "Invalid credentials"