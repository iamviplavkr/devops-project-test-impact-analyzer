from src.main.login import login

def test_login_success():
    assert login("admin", "1234") == "Login success"

def test_login_fail():
    assert login("user", "wrong") == "Invalid credentials"