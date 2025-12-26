"""
Special Types Module
=============================================================================
Contains examples and use cases for NoneType.
=============================================================================
"""

def demonstrate_special_types():
    print("\n\n[7] SPECIAL & OTHER USEFUL TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. NoneType (None)
    # -------------------------------------------------------------------------
    # Use Cases: Null checks, Defaults, Void returns.
    empty_val = None
    
    print(f"Type: {type(empty_val)}")
    print(f"Examples: {empty_val}")
    print("Real-world Use: Null flagging, optional arguments, placeholder for missing data.")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: Is `None` the same as `0` or `False`?
    A1: No. `None` is a unique object of type `NoneType`. `0` is an integer, 
        and `False` is a boolean. `None == False` evaluates to False.

    Q2: How do you check if a variable is None?
    A2: The best practice is to use `is`: `if var is None:`. This checks identity, 
        which is safer and faster than equality `==`.

    Q3: Can a function return nothing?
    A3: All functions in Python return `None` implicitly if no `return` statement 
        is executed.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - SPECIAL")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_special_types()
    interview_questions()

