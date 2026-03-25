from services.credit_modifier_service import get_credit_modifier

# For money
MIN_AMOUNT = 2000
MAX_AMOUNT = 10000
# For months
MIN_PERIOD = 12
MAX_PERIOD = 60

def calculate_decision(personal_code, loan_amount, loan_period):
    """
    Returns the maximum approvable loan amount and period for the given personal code.
    Paramater loan_amount is actually never used in coding because it does not affect the algorithm output.
    Just simple if checks to determine when to call find_best_offer and try_longer_period methods.
    """
    modifier = get_credit_modifier(personal_code)
    if modifier == -1:
        return False, None, None, "Unknown personal code."
    elif modifier == 0:
        return False, None, None, "Sparrow!!! You have a debt to pay."

    approved_amount, approved_period = find_best_offer(modifier, loan_period)
    if approved_amount is None:
        approved_amount, approved_period = try_longer_period(modifier, loan_period)

    if approved_amount is None:
        return False, None, None, f"Requested {loan_amount}€, but no suitable loan found within any period."

    if approved_period != loan_period:
        return True, approved_amount, approved_period, f"Requested {loan_amount}€ for {loan_period} months. Approved {approved_amount}€ with an adjusted period of {approved_period} months."

    if approved_amount >= loan_amount:
        return True, approved_amount, approved_period, f"Requested {loan_amount}€. Approved up to {approved_amount}€."
    else:
        return True, approved_amount, approved_period, f"Requested {loan_amount}€, but maximum approvable amount is {approved_amount}€."


def find_best_offer(modifier, period):
    """Calculates the maximum approvable amount for a given period."""
    max_amount = modifier * period
    max_amount = min(max_amount, MAX_AMOUNT)
    if max_amount >= MIN_AMOUNT:
        return max_amount, period
    return None, None


def try_longer_period(modifier, current_period):
    """
    Finds the period that fits with the biggest amount of a loan.
    """
    best_amount, best_period = None, None
    for period in range(current_period + 1, MAX_PERIOD + 1):
        amount, _ = find_best_offer(modifier, period)
        if amount is not None and (best_amount is None or amount > best_amount):
            best_amount, best_period = amount, period

    return best_amount, best_period
