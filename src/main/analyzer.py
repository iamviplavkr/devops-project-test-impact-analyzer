FILE_TEST_MAP = {
    "login.py": ["test_login.py"],
    "payment.py": ["test_payment.py"],
    "booking.py": ["test_booking.py"]
}

def get_impacted_tests(changed_files):
    impacted = set()

    for file in changed_files:
        if file in FILE_TEST_MAP:
            impacted.update(FILE_TEST_MAP[file])

    return list(impacted)