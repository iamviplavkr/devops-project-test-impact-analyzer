import subprocess
from flask import Flask, jsonify
from analyzer import get_impacted_tests

app = Flask(__name__)

def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1"],
        capture_output=True,
        text=True
    )
    return [file.split("/")[-1] for file in result.stdout.splitlines()]

@app.route('/')
def home():
    return "Test Impact Analyzer API (Git Enabled) 🚀"

@app.route('/analyze', methods=['GET'])
def analyze():
    changed_files = get_changed_files()
    impacted = get_impacted_tests(changed_files)

    return jsonify({
        "status": "success",
        "changed_files": changed_files,
        "impacted_tests": impacted,
        "count": len(impacted)
    })

if __name__ == "__main__":
    app.run(port=8080)