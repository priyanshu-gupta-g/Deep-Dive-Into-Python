"""
Loops and Iterables Module
=============================================================================
Contains examples and use cases for Loops (for, while), Iterables, 
Range, Enumerate, and Loop Control Statements (break, continue, pass).
=============================================================================
"""

def demonstrate_loops():
    print("\n[3] LOOPS & ITERABLES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. For Loop & Iterables
    # -------------------------------------------------------------------------
    user_data = {
        'name': 'Priyanshu',
        'age': 99,
        'occupation': 'Developer'
    }
    
    print("Iterating Dictionary Items:")
    for key, value in user_data.items():
        print(f"  {key} -> {value}")

    # -------------------------------------------------------------------------
    # B. Range() and Enumerate()
    # -------------------------------------------------------------------------
    print("\nRange vs Enumerate:")
    # Range: Generates a sequence of numbers
    for i in range(0, 5, 2): # start, stop, step
        print(f"  Range Index: {i}")

    # Enumerate: Returns index and value
    brands = ['Nike', 'Adidas', 'Puma']
    for index, brand in enumerate(brands):
        print(f"  Enumerate: {index} -> {brand}")

    # -------------------------------------------------------------------------
    # C. While Loop
    # -------------------------------------------------------------------------
    print("\nWhile Loop:")
    counter = 0
    while counter < 3:
        print(f"  Count: {counter}")
        counter += 1
    # Note: 'else' block in loops executes if loop finishes without break
    else: 
        print("  Loop completed successfully.")

    # -------------------------------------------------------------------------
    # D. Break, Continue, Pass
    # -------------------------------------------------------------------------
    print("\nControl Statements:")
    for num in range(5):
        if num == 1:
            continue # Skip this iteration
        if num == 3:
            break    # Exit loop
        print(f"  Number: {num}")

    # -------------------------------------------------------------------------
    # E. Exercise: Find Duplicates
    # -------------------------------------------------------------------------
    data = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
    duplicates = []
    for item in data:
        if data.count(item) > 1 and item not in duplicates:
            duplicates.append(item)
    print(f"\nDuplicates found: {duplicates}")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is the difference between `range` and `xrange` (legacy)?
    A1: In Python 3, `range()` returns an iterable object (lazy evaluation). 
        In Python 2, `range()` returned a list (memory heavy), and `xrange()` 
        was the lazy version. Python 3's `range` is essentially Python 2's `xrange`.

    Q2: When would you use a `while` loop over a `for` loop?
    A2: Use `for` loops when you know the number of iterations or are iterating 
        over a collection. Use `while` loops when the condition to stop is dynamic 
        or not based on a fixed sequence (e.g., waiting for user input).

    Q3: What does the `else` clause do in a loop?
    A3: The `else` block executes ONLY if the loop completes normally (i.e., NOT
        terminated by a `break` statement).
        
    Q4: What is the use of `enumerate()`?
    A4: It adds a counter to an iterable and returns it as an enumerate object 
        (index, value). It's cleaner than initializing a separate counter variable.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - LOOPS")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_loops()
    interview_questions()
