"""
FastAPI transport layer exposing calculator operations over HTTP.

This module acts as a thin interface between HTTP requests and the
CalculatorService. It handles request validation, response formatting,
and exception-to-HTTP mapping while delegating all business logic to
the service layer.
"""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.schemas import OperationRequest, OperationResponse

from app.services.calculator_service import CalculatorService
from app.core.exceptions import CalculatorError

from app.config import load_config

app = FastAPI(title="Calculator API")


config = load_config()
service = CalculatorService(config=config)


@app.exception_handler(CalculatorError)
async def handle_calculator_errors(request: Request, exc: CalculatorError):
    """
    Convert domain-level errors into HTTP 400 responses.

    Returns:
        JSONResponse: {"detail": <error message>}
    """
    return JSONResponse(
        status_code=400,
        content={"detail": str(exc)},
    )


@app.exception_handler(Exception)
async def handle_unexpected_errors(request: Request, exc: Exception):
    """
    Catch unhandled exceptions and return a generic HTTP 500 response.

    Prevents internal error details from leaking to clients.
    """
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error"},
    )


@app.post("/add", response_model=OperationResponse)
def add(req: OperationRequest):
    """
    Add two integers.

    Request Body:
        - a (int): First operand
        - b (int): Second operand

    Returns:
        OperationResponse: Result of addition
    """
    result = service.add(req.a, req.b)
    return {"result": result}


@app.post("/subtract", response_model=OperationResponse)
def subtract(req: OperationRequest):
    """
    Subtract the second integer from the first.

    Request Body:
        - a (int): First operand
        - b (int): Second operand

    Returns:
        OperationResponse: Result of subtraction
    """
    result = service.subtract(req.a, req.b)
    return {"result": result}


@app.post("/multiply", response_model=OperationResponse)
def multiply(req: OperationRequest):
    """
    Multiply two integers.

    Request Body:
        - a (int): First operand
        - b (int): Second operand

    Returns:
        OperationResponse: Result of multiplication
    """
    result = service.multiply(req.a, req.b)
    return {"result": result}


@app.post("/divide", response_model=OperationResponse)
def divide(req: OperationRequest):
    """
    Divide the first integer by the second.

    Request Body:
        - a (int): Dividend
        - b (int): Divisor

    Returns:
        OperationResponse: Result of division
    """
    result = service.divide(req.a, req.b)
    return {"result": result}


@app.post("/power", response_model=OperationResponse)
def power(req: OperationRequest):
    """
    Raise the first integer to the power of the second.

    Request Body:
        - a (int): Base
        - b (int): Exponent

    Returns:
        OperationResponse: Result of exponentiation
    """
    result = service.power(req.a, req.b)
    return {"result": result}
