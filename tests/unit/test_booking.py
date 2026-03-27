from src.main.booking import book_slot

def test_booking_success():
    assert book_slot(1) == "Booking confirmed"

def test_booking_fail():
    assert book_slot(0) == "Invalid slot"