"""
FastAPI transport layer exposing calculator operations over HTTP.

This module acts as a thin interface between HTTP requests and the
CalculatorService. It handles request validation, response formatting,
and exception-to-HTTP mapping while delegating all business logic to
the service layer.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.app.services.calculator_service import CalculatorService
from src.app.core.exceptions import (
    CalculatorError,
    InvalidInputError,
    DivisionByZeroError,
)
from src.app.config import get_config


app = FastAPI(title="Calculator API")


config = get_config()
service = CalculatorService(config=config)


class OperationRequest(BaseModel):
    """
    Request payload for arithmetic operations.

    Attributes:
        a (int): First operand.
        b (int): Second operand.
    """
    a: int
    b: int


class OperationResponse(BaseModel):
    """
    Standard response for arithmetic operations.

    Attributes:
        result (int): Computed result of the operation.
    """
    result: int


def handle_exception(e: Exception):
    """
    Map domain-specific exceptions to HTTP responses.

    Args:
        e (Exception): Exception raised during service execution.

    Raises:
        HTTPException: Translated HTTP error response.

    Mapping:
        - InvalidInputError → 400 Bad Request
        - DivisionByZeroError → 400 Bad Request
        - CalculatorError → 400 Bad Request
        - Any other exception → 500 Internal Server Error
    """
    if isinstance(e, InvalidInputError):
        raise HTTPException(status_code=400, detail=str(e))
    elif isinstance(e, DivisionByZeroError):
        raise HTTPException(status_code=400, detail=str(e))
    elif isinstance(e, CalculatorError):
        raise HTTPException(status_code=400, detail=str(e))
    else:
        raise HTTPException(status_code=500, detail="Internal Server Error")


@app.post("/add", response_model=OperationResponse)
def add(req: OperationRequest):
    """
    Add two integers.

    Request Body:
        - a (int): First operand
        - b (int): Second operand

    Returns:
        OperationResponse: Result of addition

    Errors:
        400: Invalid input
        500: Internal server error
    """
    try:
        result = service.add(req.a, req.b)
        return {"result": result}
    except Exception as e:
        handle_exception(e)


@app.post("/subtract", response_model=OperationResponse)
def subtract(req: OperationRequest):
    """
    Subtract the second integer from the first.

    Request Body:
        - a (int): First operand
        - b (int): Second operand

    Returns:
        OperationResponse: Result of subtraction

    Errors:
        400: Invalid input
        500: Internal server error
    """
    try:
        result = service.subtract(req.a, req.b)
        return {"result": result}
    except Exception as e:
        handle_exception(e)


@app.post("/multiply", response_model=OperationResponse)
def multiply(req: OperationRequest):
    """
    Multiply two integers.

    Request Body:
        - a (int): First operand
        - b (int): Second operand

    Returns:
        OperationResponse: Result of multiplication

    Errors:
        400: Invalid input
        500: Internal server error
    """
    try:
        result = service.multiply(req.a, req.b)
        return {"result": result}
    except Exception as e:
        handle_exception(e)


@app.post("/divide", response_model=OperationResponse)
def divide(req: OperationRequest):
    """
    Divide the first integer by the second.

    Request Body:
        - a (int): Dividend
        - b (int): Divisor

    Returns:
        OperationResponse: Result of division

    Errors:
        400: Invalid input or division by zero
        500: Internal server error
    """
    try:
        result = service.divide(req.a, req.b)
        return {"result": result}
    except Exception as e:
        handle_exception(e)


@app.post("/power", response_model=OperationResponse)
def power(req: OperationRequest):
    """
    Raise the first integer to the power of the second.

    Request Body:
        - a (int): Base
        - b (int): Exponent

    Returns:
        OperationResponse: Result of exponentiation

    Errors:
        400: Invalid input
        500: Internal server error
    """
    try:
        result = service.power(req.a, req.b)
        return {"result": result}
    except Exception as e:
        handle_exception(e)