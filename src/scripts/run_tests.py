import subprocess
from analyzer import get_impacted_tests

changed_files = ["login.py"]

tests = get_impacted_tests(changed_files)

for test in tests:
    subprocess.run(["pytest", f"tests/unit/{test}"])