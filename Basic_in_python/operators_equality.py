"""
Operators and Equality Module
=============================================================================
Contains examples and use cases for Logical Operators, Comparison Operators,
and Reference Equality (is vs ==).
=============================================================================
"""

def demonstrate_operators():
    print("\n[2] OPERATORS & EQUALITY")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Logical Operators
    # -------------------------------------------------------------------------
    # and, or, not
    x = True
    y = False
    print(f"NOT True: {not x}")
    print(f"True AND False: {x and y}")
    print(f"True OR False: {x or y}")

    # -------------------------------------------------------------------------
    # B. 'is' vs '=='
    # -------------------------------------------------------------------------
    # '==' compares values
    # 'is' compares memory location (identity)
    
    list_a = [1, 2, 3]
    list_b = [1, 2, 3]
    list_c = list_a

    print(f"\nComparing lists: {list_a} and {list_b}")
    print(f"list_a == list_b: {list_a == list_b} (Same Value)")
    print(f"list_a is list_b: {list_a is list_b} (Different Memory)")
    print(f"list_a is list_c: {list_a is list_c} (Same Memory)")

    # -------------------------------------------------------------------------
    # C. Operator Precedence
    # -------------------------------------------------------------------------
    # () > ** > * / > + - > and > or
    result = True or False and False 
    # Evaluates as: True or (False and False) -> True or False -> True
    print(f"\nPrecedence Example (True or False and False): {result}")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: Explain the difference between `is` and `==`.
    A1: `==` compares the *values* of two objects. `is` compares the *identity* 
        (memory address) of two objects. 
        Example: `[] == []` is True, `[] is []` is False.

    Q2: What is the operator precedence of `and` vs `or`?
    A2: `and` has higher precedence than `or`. 
        Expression `A or B and C` is evaluated as `A or (B and C)`.

    Q3: How does the `not` operator work with non-boolean values?
    A3: It converts the value to a boolean (truthy/falsy check) and then inverts it.
        `not []` -> `not False` -> `True`.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - OPERATORS")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_operators()
    interview_questions()
