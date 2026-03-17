# 🚀 Test Impact Analyzer  
### Analyze which tests are impacted by code changes

---

## 👨‍💻 Student Details
- **Name:** Viplav Kumar  
- **Registration No:** 23FE10CSE00421  
- **Course:** CSE3253 DevOps [PE6]  
- **Semester:** VI (2025–2026)  
- **Project Type:** Testing  
- **Difficulty:** Intermediate  

---

## 📌 Project Overview

### ❓ Problem Statement
In modern software systems, running the entire test suite after every code change is inefficient, time-consuming, and costly. Even small changes trigger unnecessary execution of unrelated tests.

---

### 💡 Solution
This project implements a **Test Impact Analyzer**, which identifies and executes only those test cases that are affected by recent code changes.

---

## 🎯 Objectives

- Identify impacted test cases based on code changes  
- Reduce test execution time  
- Improve CI/CD pipeline efficiency  
- Automate selective test execution  

---

## ✨ Key Features

- 🔍 Detect changed source files  
- 🧠 Map source files to corresponding test cases  
- ⚡ Execute only impacted tests  
- 🌐 REST API for analysis  
- 🔄 CI/CD integration using GitHub Actions  

---

## ⚙️ Technology Stack

### 🧩 Core Technologies
- **Language:** Python  
- **Framework:** Flask  
- **Testing:** Pytest  

### 🔧 DevOps Tools
- **Version Control:** Git, GitHub  
- **CI/CD:** GitHub Actions    

---

## 🧠 How It Works

### 🔄 Workflow

1. Developer makes changes in code  
2. Changed files are detected  
3. Analyzer maps changed files to test cases  
4. Only impacted tests are selected  
5. Selected tests are executed  
6. Faster CI/CD pipeline  

---

### 📊 Flow Diagram

Code Change → Detect Files → Analyzer → Impacted Tests → Execute Tests → Faster Pipeline


---

## 🧪 Example

### Input
```json
{
  "files": ["login.py"]
}

