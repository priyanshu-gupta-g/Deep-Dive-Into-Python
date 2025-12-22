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
