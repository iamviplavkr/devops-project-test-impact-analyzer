from src.main.payment import process_payment

def test_payment_success():
    assert process_payment(100) == "Payment successful"

def test_payment_fail():
    assert process_payment(0) == "Invalid payment"