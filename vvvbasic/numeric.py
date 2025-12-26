"""
Numeric Types Module
=============================================================================
Contains examples and use cases for Integer, Float, and Complex types.
=============================================================================
"""

def demonstrate_numeric_types():
    print("\n[1] NUMERIC TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Integer (int)
    # -------------------------------------------------------------------------
    # Use Cases: Counting, Indexing, IDs.
    my_int = 42
    population_count = 7_800_000_000
    print(f"Type: {type(my_int)} | Examples: {my_int}, {population_count}")
    print("Real-world Use: Counting users, Array indexing, Database IDs.")

    # -------------------------------------------------------------------------
    # B. Floating Point (float)
    # -------------------------------------------------------------------------
    # Use Cases: Measurements, Scientific calc, Coordinates.
    my_float = 3.14159
    temperature = 98.6
    print(f"\nType: {type(my_float)} | Examples: {my_float}, {temperature}")
    print("Real-world Use: Physics stats, Coordinates (GPS), Temperature measurements.")

    # -------------------------------------------------------------------------
    # C. Complex (complex)
    # -------------------------------------------------------------------------
    # Use Cases: Electrical Engineering, Signal Processing.
    my_complex = 3 + 4j
    print(f"\nType: {type(my_complex)} | Examples: {my_complex}")
    print("Real-world Use: Electrical Engineering (AC circuits), Signal Processing.")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is the precision of a float in Python?
    A1: Python floats are typically implemented as double-precision (64-bit) 
        floating-point numbers, roughly 15-17 decimal digits of precision.

    Q2: How does Python handle large integers?
    A2: Python 3 handles arbitrarily large integers. The size is limited only 
        by the available memory, unlike languages like C/Java (int/long limits).

    Q3: What happens when you divide two integers?
    A3: In Python 3, `/` always performs true division and returns a float (e.g., `5/2 -> 2.5`). 
        `//` performs floor division and returns an integer (e.g., `5//2 -> 2`).
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - NUMERIC")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_numeric_types()
    interview_questions()

