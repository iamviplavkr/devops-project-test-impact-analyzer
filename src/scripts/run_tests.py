import subprocess
from analyzer import get_impacted_tests

def get_changed_files():
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1"],
            capture_output=True,
            text=True,
            check=True
        )

        changed_files = result.stdout.strip().split("\n")

        # Remove empty strings
        return [file.split("/")[-1] for file in changed_files if file]

    except subprocess.CalledProcessError:
        print("Error getting changed files from Git")
        return []


# 🔥 AUTO DETECT CHANGES
changed_files = get_changed_files()

print("Changed Files:", changed_files)

# 🔍 FIND IMPACTED TESTS
tests = get_impacted_tests(changed_files)

print("Impacted Tests:", tests)

# ▶️ RUN ONLY IMPACTED TESTS
for test in tests:
    subprocess.run(["pytest", f"tests/unit/{test}"])