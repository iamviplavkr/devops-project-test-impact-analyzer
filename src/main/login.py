def login(username, password):
    if username == "admin" and password == "12345":
        return "Login success"
    else:
        return "Invalid credentials"