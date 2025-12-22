"""
VVVBASIC - Deep Dive into Python Data Types
=============================================================================
This file serves as a comprehensive reference for Python's built-in data types.
Each section lists the data type, provides examples, and explains real-world
use cases.

Author: Antigravity (on behalf of User)
Context: Deep Dive Into Python
=============================================================================
"""

import datetime
from decimal import Decimal
from collections import namedtuple

def main():
    print("="*80)
    print(" PYTHON DATA TYPES DEEP DIVE")
    print("="*80)

    # =========================================================================
    # 1. NUMERIC TYPES
    # =========================================================================
    print("\n[1] NUMERIC TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Integer (int)
    # -------------------------------------------------------------------------
    # Description: Whole numbers without a fractional component.
    # Use Cases:
    # - Counting items (e.g., number of active users, loop counters).
    # - Indexing sequences (e.g., accessing the 5th element of a list).
    # - Database IDs and primary keys.
    # - Mathematical operations requiring precision (e.g., combinatorics).
    
    my_int = 42
    population_count = 7_800_000_000  # Underscores for readability
    negative_balance = -500
    
    print(f"Type: {type(my_int)}")
    print(f"Examples: {my_int}, {population_count}, {negative_balance}")
    print("Real-world Use: Counting users, Array indexing, Database IDs.")

    # -------------------------------------------------------------------------
    # B. Floating Point (float)
    # -------------------------------------------------------------------------
    # Description: Real numbers with a floating-point representation (decimals).
    # Use Cases:
    # - Scientific calculations (typically required in physics, engineering).
    # - Measuring continuous quantities (temperature, speed, height).
    # - Representing geographical coordinates (latitude/longitude).
    # Note: Not recommended for financial currency due to precision issues (use Decimal).
    
    my_float = 3.14159
    temperature = 98.6
    scientific_notation = 1.5e2  # 150.0
    
    print(f"\nType: {type(my_float)}")
    print(f"Examples: {my_float}, {temperature}, {scientific_notation}")
    print("Real-world Use: Physics stats, Coordinates (GPS), Temperature measurements.")

    # -------------------------------------------------------------------------
    # C. Complex (complex)
    # -------------------------------------------------------------------------
    # Description: Numbers with a real and an imaginary component (j).
    # Use Cases:
    # - Electrical engineering (analyzing AC circuits).
    # - Signal processing / Fourier transforms.
    # - Advanced mathematics and physics vectors.
    
    my_complex = 3 + 4j
    
    print(f"\nType: {type(my_complex)}")
    print(f"Examples: {my_complex} (Real: {my_complex.real}, Imag: {my_complex.imag})")
    print("Real-world Use: Electrical Engineering (AC circuits), Signal Processing.")

    # =========================================================================
    # 2. SEQUENCE TYPES
    # =========================================================================
    print("\n\n[2] SEQUENCE TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. String (str)
    # -------------------------------------------------------------------------
    # Description: Immutable sequence of Unicode characters.
    # Use Cases:
    # - Storing textual data (names, addresses, messages).
    # - Parsing file contents (JSON, XML).
    # - UI labels and user feedback messages.
    # - Keys in dictionaries (since they are hashable).
    
    user_name = "Priyanshu Gupta"
    path = r"C:\Data\New"  # Raw string for paths
    multiline = """This is a
    multiline string."""
    
    print(f"Type: {type(user_name)}")
    print(f"Examples: '{user_name}'")
    print("Real-world Use: User inputs, File paths, Text processing, NLP.")

    # -------------------------------------------------------------------------
    # B. List (list)
    # -------------------------------------------------------------------------
    # Description: Mutable, ordered sequence of items.
    # Use Cases:
    # - Storing collections of homogeneous or heterogeneous items.
    # - Stack or Queue implementations (append/pop).
    # - Holding data rows from a database query.
    # - Dynamic arrays where size usually changes.
    
    todo_list = ["Buy groceries", 101, "Gym"]
    matrix = [[1, 2], [3, 4]]
    
    print(f"\nType: {type(todo_list)}")
    print(f"Examples: {todo_list}")
    print("Real-world Use: Accumulating data chunks, Database query results, To-do items.")

    # -------------------------------------------------------------------------
    # C. Tuple (tuple)
    # -------------------------------------------------------------------------
    # Description: Immutable, ordered sequence of items.
    # Use Cases:
    # - Returning multiple values from a function.
    # - Representing fixed collections (e.g., (x, y) coordinates, RGB colors).
    # - Dictionary keys (if containing only immutable types).
    # - Data integrity: ensuring data doesn't change accidentally.
    
    point_2d = (1920, 1080)
    rgb_red = (255, 0, 0)
    
    print(f"\nType: {type(point_2d)}")
    print(f"Examples: {point_2d}, RedColor={rgb_red}")
    print("Real-world Use: Fixed configs, Coordinates, Dictionary keys, Function returns.")

    # -------------------------------------------------------------------------
    # D. Range (range)
    # -------------------------------------------------------------------------
    # Description: Immutable sequence of numbers.
    # Use Cases:
    # - Loops (for i in range...).
    # - Generating index lists without storing them in memory (lazy evaluation).
    
    loop_range = range(0, 10, 2)
    
    print(f"\nType: {type(loop_range)}")
    print(f"Examples: list(range(0,10,2)) -> {list(loop_range)}")
    print("Real-world Use: Iteration control in loops, Memory-efficient number generation.")

    # =========================================================================
    # 3. MAPPING TYPE
    # =========================================================================
    print("\n\n[3] MAPPING TYPE")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Dictionary (dict)
    # -------------------------------------------------------------------------
    # Description: Mutable, unordered (insertion-ordered in 3.7+) collection of key-value pairs.
    # Use Cases:
    # - Fast lookups by key (O(1) average time complexity).
    # - Representing objects or records (e.g., JSON responses).
    # - Caching / Memoization.
    # - Configuration settings.
    
    user_profile = {
        "id": 101,
        "username": "pg871",
        "is_active": True,
        "roles": ["admin", "editor"]
    }
    
    print(f"Type: {type(user_profile)}")
    print(f"Examples: {user_profile}")
    print("Real-world Use: JSON APIs, Caching configurations, User profiles, Fast lookups.")

    # =========================================================================
    # 4. SET TYPES
    # =========================================================================
    print("\n\n[4] SET TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Set (set)
    # -------------------------------------------------------------------------
    # Description: Mutable, unordered collection of unique elements.
    # Use Cases:
    # - Removing duplicates from a list.
    # - Mathematical set operations (union, intersection, difference).
    # - Membership testing (checking if an item exists is faster than lists).
    
    unique_ids = {101, 102, 103, 101} # 101 effectively removed
    
    print(f"Type: {type(unique_ids)}")
    print(f"Examples: {unique_ids}")
    print("Real-world Use: Deduplication, Membership testing, Access control lists.")

    # -------------------------------------------------------------------------
    # B. FrozenSet (frozenset)
    # -------------------------------------------------------------------------
    # Description: Immutable version of a set.
    # Use Cases:
    # - Using a set as a key in a dictionary (since it's hashable).
    # - Ensuring a set of flags/permissions cannot be modified.
    
    permissions = frozenset(["read", "execute"])
    
    print(f"\nType: {type(permissions)}")
    print(f"Examples: {permissions}")
    print("Real-world Use: Dictionary keys requiring set behaviors, Fixed permission groups.")

    # =========================================================================
    # 5. BOOLEAN TYPE
    # =========================================================================
    print("\n\n[5] BOOLEAN TYPE")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Boolean (bool)
    # -------------------------------------------------------------------------
    # Description: Represents Truthy (True) or Falsy (False) values.
    # Use Cases:
    # - Control flow (if/else statements).
    # - Flags (is_visible, has_permission).
    # - Result of comparisons (x > y).
    
    is_authenticated = True
    has_errors = False
    
    print(f"Type: {type(is_authenticated)}")
    print(f"Examples: {is_authenticated}, {has_errors}")
    print("Real-world Use: Conditional logic, Feature flags, Binary states.")

    # =========================================================================
    # 6. BINARY TYPES
    # =========================================================================
    print("\n\n[6] BINARY TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Bytes (bytes)
    # -------------------------------------------------------------------------
    # Description: Immutable sequence of bytes.
    # Use Cases:
    # - Binary file I/O (images, audio).
    # - Network communication protocols (sockets, HTTP raw payloads).
    # - Encryption/Hashing inputs.
    
    data_packet = b'\x00\xFF\xA5'
    message_bytes = b"Hello"
    
    print(f"Type: {type(data_packet)}")
    print(f"Examples: {data_packet}")
    print("Real-world Use: Image processing, Network sockets, Cryptography.")

    # -------------------------------------------------------------------------
    # B. Bytearray (bytearray)
    # -------------------------------------------------------------------------
    # Description: Mutable sequence of bytes.
    # Use Cases:
    # - Buffering large amounts of binary data where modification is needed.
    # - Manipulating binary streams without copying (more efficient).
    
    mutable_buffer = bytearray(b"Hello")
    mutable_buffer[0] = 74 # 'J'
    
    print(f"\nType: {type(mutable_buffer)}")
    print(f"Examples: {mutable_buffer} (Modified 'H' to 'J')")
    print("Real-world Use: Low-level buffering, Binary stream manipulation.")

    # =========================================================================
    # 7. SPECIAL TYPES AND OTHERS
    # =========================================================================
    print("\n\n[7] SPECIAL & OTHER USEFUL TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. NoneType (None)
    # -------------------------------------------------------------------------
    # Description: Represents the absence of a value or a null value.
    # Use Cases:
    # - Default parameter values in functions.
    # - Return value of functions that don't return anything.
    # - Initializing variables that will be assigned later.
    
    empty_val = None
    
    print(f"Type: {type(empty_val)}")
    print(f"Examples: {empty_val}")
    print("Real-world Use: Null flagging, optional arguments, placeholder for missing data.")

    print("\n" + "="*80)
    print(" END OF DEEP DIVE")
    print("="*80)

if __name__ == "__main__":
    main()
