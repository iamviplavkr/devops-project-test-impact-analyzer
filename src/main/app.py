from flask import Flask, request, jsonify
from analyzer import get_impacted_tests

app = Flask(__name__)

@app.route('/')
def home():
    return "Test Impact Analyzer API is running 🚀"

@app.route('/analyze', methods=['POST'])
def analyze():
    changed_files = request.json.get("files", [])
    impacted = get_impacted_tests(changed_files)

    return jsonify({
        "status": "success",
        "changed_files": changed_files,
        "impacted_tests": impacted,
        "count": len(impacted)
    })

if __name__ == "__main__":
    app.run(port=8080)