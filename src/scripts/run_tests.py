import subprocess
import sys
import os

# ✅ Add path to main folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../main')))

from analyzer import get_impacted_tests

def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1"],
        capture_output=True,
        text=True
    )
    return [file.split("/")[-1] for file in result.stdout.splitlines()]

changed_files = get_changed_files()

print("Changed Files:", changed_files)

tests = get_impacted_tests(changed_files)

print("Impacted Tests:", tests)

for test in tests:
    subprocess.run([sys.executable, "-m", "pytest", f"tests/unit/{test}"])