# Test Impact Analyzer with CI/CD Integration

## Project Overview

Test Impact Analyzer is a DevOps-based automation project that detects changed source files using Git and executes only the impacted test cases instead of running the complete test suite. This helps reduce testing time and improves CI/CD pipeline efficiency.

The project is built using Python, Flask, Pytest, Git, and GitHub Actions.

---

# Features

- Detects changed files automatically using Git
- Maps source files to corresponding test cases
- Executes only impacted tests
- Automated testing using Pytest
- CI/CD integration using GitHub Actions
- Modular and scalable architecture

---

# Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Flask | REST API development |
| Pytest | Automated testing |
| Git | Change detection |
| GitHub Actions | CI/CD pipeline |

---

# Project Structure

```plaintext
DEVOPS-PROJECT-TEST-IMPACT-ANALYZER/
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── src/
│   ├── main/
│   │   ├── analyzer.py
│   │   ├── app.py
│   │   ├── login.py
│   │   ├── payment.py
│   │   └── booking.py
│   │
│   └── scripts/
│       └── run_tests.py
│
├── tests/
│   └── unit/
│       ├── test_login.py
│       ├── test_payment.py
│       └── test_booking.py
│
├── requirements.txt
└── README.md
```

---

# Workflow

1. Developer modifies source code files
2. Git detects changed files using `git diff`
3. Analyzer identifies impacted test cases
4. Only impacted tests are executed
5. GitHub Actions automates the CI/CD pipeline

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/iamviplavkr/devops-project-test-impact-analyzer.git
cd devops-project-test-impact-analyzer
```

---

## 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## 3. Run Flask Application

```bash
python src/main/app.py
```

Application runs on:

```plaintext
http://127.0.0.1:8080
```

---

## 4. Run Test Impact Analyzer

```bash
python src/scripts/run_tests.py
```

---

# API Endpoint

## Analyze Changed Files

### Endpoint

```plaintext
POST /analyze
```

### Sample Request

```json
{
  "files": ["login.py"]
}
```

### Sample Response

```json
{
  "status": "success",
  "changed_files": ["login.py"],
  "impacted_tests": ["test_login.py"],
  "count": 1
}
```

---

# Core Modules

## analyzer.py

Maintains mapping between source files and test files.

Example:

```python
FILE_TEST_MAP = {
    "login.py": ["test_login.py"],
    "payment.py": ["test_payment.py"],
    "booking.py": ["test_booking.py"]
}
```

---

## run_tests.py

- Detects changed files using Git
- Identifies impacted tests
- Executes impacted tests using Pytest

---

# CI/CD Pipeline

GitHub Actions workflow automates:

- Dependency installation
- Test execution
- Impact analysis execution

Workflow file:

```plaintext
.github/workflows/ci-cd.yml
```

---

# Sample Output

```plaintext
Changed Files: ['login.py']
Impacted Tests: ['test_login.py']

================= test session starts =================
1 passed
```

---

# Advantages

- Reduces unnecessary test execution
- Improves CI/CD efficiency
- Faster feedback for developers
- Scalable for large applications

---

# Future Enhancements

- AI-based dependency analysis
- Parallel test execution
- Docker integration
- Dashboard for visualization
- Database-based test mapping

---

# Author

**Viplav Kumar**  
B.Tech CSE, Manipal University Jaipur

GitHub: https://github.com/iamviplavkr
LinkedIn: https://www.linkedin.com/in/viplav-kumar/

---

# Conclusion

This project demonstrates practical DevOps concepts including Git-based change detection, selective test execution, CI/CD automation, and test optimization. It showcases how intelligent testing strategies can improve software delivery efficiency in real-world development environments.

