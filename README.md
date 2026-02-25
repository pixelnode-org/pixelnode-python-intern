## Project Overview

This project is a modular Python calculator application designed with clear separation of concerns. It includes:

- Core arithmetic operations: `add`, `subtract`, `multiply`, and `divide`
- Strict integer input validation in utility logic
- A service layer (`CalculatorService`) that delegates computation to utility functions
- A command-line interface built with `argparse`
- Unit tests written with `pytest`

## Project Structure

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

## Create Virtual Environment

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

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Tests

```bash
pytest
```

## Run CLI Using `-m`

Run the CLI as a module from the project root:

```bash
python -m src.app.cli <operation> <a> <b>
```

Example:

```bash
python -m src.app.cli add 10 5
```

## Architecture Overview

- `math_utils.py`
- Implements arithmetic functions with strict integer validation
- `divide()` returns a `float`

- `calculator_service.py`
- Defines `CalculatorService`
- Delegates operation handling to `math_utils`

- `cli.py`
- Parses command-line arguments using `argparse`
- Calls `CalculatorService` and prints results

Layer flow:

- CLI layer -> Service layer -> Utility layer

## Notes

- All arithmetic inputs are validated as integers
- Division returns floating-point output
- The service layer keeps CLI logic separate from math implementation
- Tests cover utility functions, service behavior, and CLI execution
