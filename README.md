# 🧮 Python Calculator (Modular CLI Application)

![Python](https://img.shields.io/badge/Python-3.10%2B\-blue)
![Tests](https://img.shields.io/badge/tests-pytest-green)
![Code Style](https://img.shields.io/badge/code%20style-black-black)
![Lint](https://img.shields.io/badge/lint-flake8-blue)


A modular and extensible Python calculator application built with a clean, layered architecture.

This project demonstrates backend-oriented engineering practices such as:

- Separation of concerns (utility → service → interface)
- Input validation and error handling
- Structured logging
- Command-line interface design
- Automated testing with `pytest`
- Code quality enforcement using `black` and `flake8`

---

## 📂 Project Structure

```text
src/
  app/
    __init__.py
    math_utils.py
    calculator_service.py
    cli.py

tests/
  test_math_utils.py
  test_calculator_service.py
  test_cli.py
```

---

## ⚙️ Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment:

- Windows:

```bash
venv\Scripts\activate
```

- macOS/Linux:

```bash
source venv/bin/activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```
---

## 🧪 Run Tests

```bash
pytest
```
Covers:
- Utility functions
- Service layer delegation
- CLI behavior

## ▶️ Run CLI Using `-m`

Run the CLI as a module from the project root:

```bash
python -m src.app.cli <operation> <a> <b>
```

Example:

```bash
python -m src.app.cli add 10 5
python -m src.app.cli divide 10 2
python -m src.app.cli power 2 3
```

### Verbose Mode

```bash
python -m src.app.cli add 5 3 --verbose
```

---

## Architecture Overview

- Utility Layer — `math_utils.py`
  - Implements core arithmetic operations:
    - `add`, `subtract`, `multiply`, `divide`, `power`
  - Enforces strict integer validation
  - Contains all business logic

- Service Layer — `calculator_service.py`
  - Provides `CalculatorService`
  - Delegates operations to `math_utils`
  - Keeps business logic decoupled from interfaces

- Interface Layer — `cli.py`
  - Built using `argparse`
  - Supports module execution (`python -m`)
  - Uses structured logging (`logging`)
  - Includes optional verbose mode (`--verbose`)

### 🔁 Layer flow:
```markdown
CLI → Service → Utility
```

---

## 📌 Features
- Integer-only input validation
- Division returns floating-point result
- Exponentiation support via `power(a, b)`
- Structured logging (INFO / DEBUG / ERROR)
- Verbose mode for debugging (`--verbose`)
- Modular design enabling easy extension of new operations
- Fully tested with `pytest`

## 🧼 Code Quality
- Formatted using `black`
- Linted using `flake8`
- Clean, consistent, and maintainable codebase

## 📎 Notes
- CLI uses logging instead of print statements
- Invalid inputs are handled via argparse and exception handling
- Project follows a scalable backend architecture pattern
