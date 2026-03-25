from pydantic import BaseModel, Field

"""Shows how data should look like."""
class LoanRequest(BaseModel):
    personal_code: str
    loan_amount: float = Field(ge=2000, le=10000)
    loan_period: int = Field(ge=12, le=60)

class LoanDecision(BaseModel):
    approved: bool
    approved_amount: float | None
    approved_period: int | None
    message: str