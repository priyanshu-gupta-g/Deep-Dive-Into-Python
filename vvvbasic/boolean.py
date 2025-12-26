"""
Boolean Types Module
=============================================================================
Contains examples and use cases for Boolean types.
=============================================================================
"""

def demonstrate_boolean_types():
    print("\n\n[5] BOOLEAN TYPE")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Boolean (bool)
    # -------------------------------------------------------------------------
    # Use Cases: Control flow, Flags, Logic.
    is_authenticated = True
    has_errors = False
    
    print(f"Type: {type(is_authenticated)}")
    print(f"Examples: {is_authenticated}, {has_errors}")
    print("Real-world Use: Conditional logic, Feature flags, Binary states.")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What does `bool` inherit from in Python?
    A1: `bool` is a subclass of `int`. `True` is treated as 1 and `False` as 0 
        in numeric contexts.

    Q2: Can `True` be re-assigned in Python 3?
    A2: No, in Python 3, `True` and `False` are keywords and cannot be assigned 
        to. (In Python 2, it was possible).

    Q3: What constructs return Boolean values?
    A3: Comparison operators (`==`, `>`, `<`), logic operators (`and`, `or` - 
        though they return operands, result is boolean-compatible), and identity 
        checks (`is`, `in`).
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - BOOLEAN")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_boolean_types()
    interview_questions()

