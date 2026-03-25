CREDIT_MODIFIERS = {
    "49002010965": 0,     # võlg
    "49002010976": 100,   # segment 1
    "49002010987": 300,   # segment 2
    "49002010998": 1000,  # segment 3
}

def get_credit_modifier(personal_code: str) -> int:
    """
    Returns credit modifier based on personal code.
    -1 if personal code does not exist.
    """
    return CREDIT_MODIFIERS.get(personal_code, -1)