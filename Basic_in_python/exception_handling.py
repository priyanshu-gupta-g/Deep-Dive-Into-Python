"""
Exception Handling Module
=============================================================================
Contains examples and use cases for Try, Except, Else, and Finally blocks.
=============================================================================
"""

def demonstrate_exceptions():
    print("\n[7] EXCEPTION HANDLING")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Basic Try-Except
    # -------------------------------------------------------------------------
    # Handling specific errors to prevent crashes
    try:
        age_input = "not_a_number"
        age = int(age_input)
        print(age)
    except ValueError as e:
        print(f"Caught Error: {e} (Please enter a valid number)")

    # -------------------------------------------------------------------------
    # B. Multiple Exceptions
    # -------------------------------------------------------------------------
    try:
        # result = 10 / 0      # ZeroDivisionError
        my_list = [1, 2]
        # value = my_list[5]   # IndexError
        pass # No error
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except IndexError:
        print("Error: List index out of range.")
    except Exception as e:
        # Good practice: Catch specific errors first, then general Exception
        print(f"Unexpected Error: {e}")

    # -------------------------------------------------------------------------
    # C. Else and Finally
    # -------------------------------------------------------------------------
    print("\nElse & Finally Flow:")
    try:
        print("  1. Trying operation...")
        result = 10 / 2
    except ZeroDivisionError:
        print("  x. Error happened.")
    else:
        # Runs ONLY if no exception occurs
        print(f"  2. Success! Result is {result}")
    finally:
        # Runs ALWAYS (cleanup code, closing files/db connections)
        print("  3. Cleanup/Finally block executed.")
        
    # -------------------------------------------------------------------------
    # D. Raising Exceptions
    # -------------------------------------------------------------------------
    # raise ValueError("Manual error")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is the difference between `except Exception` and a specific except?
    A1: `except Exception` catches almost all errors, which might hide bugs you 
        didn't intend to handle. Specific exceptions (e.g., `ValueError`) 
        allow you to handle known error states precisely without suppressing 
        unexpected crashes.

    Q2: When is the `finally` block executed?
    A2: It is executed ALWAYS, regardless of whether an exception occurred or not.
        It is typically used for cleanup actions (closing files, releasing resources).

    Q3: What does the `else` block do in a try-except statement?
    A3: The `else` block executes only if NO exception was raised in the `try` block.
        It separates the "success" logic from the error handling logic.

    Q4: Can we have multiple `except` blocks for a single `try` block?
    A4: Yes, to handle different types of exceptions differently. Python checks 
        them top-down and executes the first matching block.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - EXCEPTIONS")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_exceptions()
    interview_questions()
