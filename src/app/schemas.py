from pydantic import BaseModel, Field


class OperationRequest(BaseModel):
    """
    Request schema for binary arithmetic operations.

    Attributes:
        a (int): First operand.
        b (int): Second operand.

    Notes:
        - Validation is handled at the API boundary.
        - Ensures only valid integers reach the service layer.
    """

    a: int = Field(..., description="First oprand")
    b: int = Field(..., description="Second operand")


class OperationResponse(BaseModel):
    """
    Standard response for arithmetic operations.

    Attributes:
        result (int): Computed result of the operation.
    """

    result: int
