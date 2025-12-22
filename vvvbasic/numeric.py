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
