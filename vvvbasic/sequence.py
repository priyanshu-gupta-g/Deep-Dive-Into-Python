"""
Sequence Types Module
=============================================================================
Contains examples and use cases for String, List, Tuple, and Range types.
=============================================================================
"""

def demonstrate_sequence_types():
    print("\n\n[2] SEQUENCE TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. String (str)
    # -------------------------------------------------------------------------
    # Use Cases: Text, JSON, UI Messages.
    user_name = "Priyanshu Gupta"
    path = r"C:\Data\New"
    print(f"Type: {type(user_name)} | Create: '{user_name}'")
    print("Real-world Use: User inputs, File paths, Text processing, NLP.")

    # -------------------------------------------------------------------------
    # B. List (list)
    # -------------------------------------------------------------------------
    # Use Cases: Collections, Stacks, Database rows.
    todo_list = ["Buy groceries", 101, "Gym"]
    print(f"\nType: {type(todo_list)} | Create: {todo_list}")
    print("Real-world Use: Accumulating data chunks, Database query results.")

    # -------------------------------------------------------------------------
    # C. Tuple (tuple)
    # -------------------------------------------------------------------------
    # Use Cases: Fixed coordinates, Dictionary keys, Multiple return values.
    point_2d = (1920, 1080)
    print(f"\nType: {type(point_2d)} | Create: {point_2d}")
    print("Real-world Use: Fixed configs, Coordinates, Dictionary keys.")

    # -------------------------------------------------------------------------
    # D. Range (range)
    # -------------------------------------------------------------------------
    # Use Cases: Loops, Lazy sequence generation.
    loop_range = range(0, 10, 2)
    print(f"\nType: {type(loop_range)} | Create: range(0, 10, 2)")
    print("Real-world Use: Iteration control in loops, Memory-efficient number generation.")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is the main difference between a list and a tuple?
    A1: Lists are mutable (can be changed). Tuples are immutable (cannot be changed).
        Tuples are generally faster and safer for fixed data.

    Q2: How does `range()` work in Python 3?
    A2: It returns an immutable sequence type (not a list). It generates numbers 
        on demand (lazy evaluation), saving memory compared to Python 2's `range` 
        which returned a list.

    Q3: Are strings mutable in Python?
    A3: No, strings are immutable. operations like `replace` or concatenation 
        create a NEW string object.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - SEQUENCE")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_sequence_types()
    interview_questions()

