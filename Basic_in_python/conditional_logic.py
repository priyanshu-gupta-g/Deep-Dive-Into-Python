"""
Conditional Logic Module
=============================================================================
Contains examples and use cases for Conditional Logic, Ternary Operators, 
and Short Circuiting in Python.
=============================================================================
"""

def demonstrate_conditional_logic():
    print("\n[1] CONDITIONAL LOGIC")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Basic If-Elif-Else
    # -------------------------------------------------------------------------
    age = True
    licensed = True

    print(f"Status: Age={age}, Licensed={licensed}")
    
    if age and licensed:
        print("Result: You are allowed to drive.")
    elif age and not licensed:
        print("Result: You are old enough but need a license.")
    else:
        print("Result: You are not allowed to drive.")

    # -------------------------------------------------------------------------
    # B. Ternary Operator
    # -------------------------------------------------------------------------
    # Syntax: value_if_true if condition else value_if_false
    is_friend = True
    message_status = "valid" if is_friend else "invalid"
    print(f"\nTernary Check: User is friend? -> {message_status}")

    # -------------------------------------------------------------------------
    # C. Short Circuiting
    # -------------------------------------------------------------------------
    # Python stops evaluating as soon as the result is determined.
    has_ticket = True
    is_vip = False

    if has_ticket or is_vip: # If has_ticket is True, is_vip is never checked
        print("\nShort Circuit: Access Granted (Ticket checked, VIP ignored)")
    
    # -------------------------------------------------------------------------
    # D. Truthy and Falsy
    # -------------------------------------------------------------------------
    # Falsy values: 0, 0.0, '', [], {}, (), None, False
    username = '' # Falsy
    if username:
        print(f"User: {username}")
    else:
        print("\nTruthy/Falsy: No username provided (Empty string is falsy).")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is Short Circuiting in Python?
    A1: It's an optimization where Python stops evaluating a boolean expression 
        as soon as the truth value is determined. 
        - `OR`: if first operand is True, return it.
        - `AND`: if first operand is False, return it.
    
    Q2: What is the difference between `==` and `is`? (Preview)
    A2: `==` checks for value equality, while `is` checks for reference equality 
       (memory address).
    
    Q3: Which values are considered Falsy in Python?
    A3: 0, 0.0, False, None, empty sequences ('', [], (), {}).
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - CONDITIONAL LOGIC")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_conditional_logic()
    interview_questions()
