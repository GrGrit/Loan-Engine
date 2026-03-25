from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import LoanRequest, LoanDecision
from services.loan_decision_service import calculate_decision

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/loan-decision", response_model=LoanDecision)
def loan_decision(request: LoanRequest):
    approved, amount, period, message = calculate_decision(
        request.personal_code,
        request.loan_amount,
        request.loan_period
    )
    return LoanDecision(
        approved=approved,
        approved_amount=amount,
        approved_period=period,
        message=message
    )