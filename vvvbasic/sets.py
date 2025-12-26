"""
Set Types Module
=============================================================================
Contains examples and use cases for Set and Frozenset types.
=============================================================================
"""

def demonstrate_set_types():
    print("\n\n[4] SET TYPES")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Set (set)
    # -------------------------------------------------------------------------
    # Use Cases: Deduplication, Math set ops, Fast membership test.
    unique_ids = {101, 102, 103, 101}
    print(f"Type: {type(unique_ids)} | Result: {unique_ids}")
    print("Real-world Use: Deduplication, Membership testing, Access control lists.")

    # -------------------------------------------------------------------------
    # B. FrozenSet (frozenset)
    # -------------------------------------------------------------------------
    # Use Cases: Immutable sets, Dictionary keys.
    permissions = frozenset(["read", "execute"])
    print(f"\nType: {type(permissions)} | Result: {permissions}")
    print("Real-world Use: Dictionary keys requiring set behaviors, Fixed permission groups.")

    # -------------------------------------------------------------------------
    # C. Common Set Methods
    # -------------------------------------------------------------------------
    # .difference()
    # .discard()
    # .difference_update()
    # .intersection()
    # .issubset()
    # .issuperset()
    # .union()

    # -------------------------------------------------------------------------
    # C. Common Set Operations
    # -------------------------------------------------------------------------
    # Demonstrating standard methods: difference, discard, intersection, union, etc.
    
    my_set = {1, 2, 3, 4, 5}
    my_set1 = {4, 5, 6}
    your_set = {4, 5, 6, 7, 8}
    
    print("\n--- Set Operations Examples ---")
    print(f"Set 1: {my_set}")
    print(f"Set 2: {your_set}")

    # 1. Difference (Elements in my_set but not in your_set)
    # Note: .difference() returns a new set, does not modify the original.
    diff = my_set.difference(your_set)
    print(f"Difference (my_set - your_set): {diff}")

    # 2. Discard (Remove element safely)
    # .discard(x) removes x if present; does nothing if x is not found (unlike .remove() which raises KeyError).
    my_set.discard(5)
    print(f"After discard(5): {my_set}")

    # 3. Intersection (Elements common to both sets)
    # Can use .intersection() method or & operator
    common = my_set.intersection(your_set)
    print(f"Intersection (my_set & your_set): {common}")
    print(f"Intersection using '&' operator: {my_set & your_set}")

    # 4. Union (All unique elements from both sets)
    # Can use .union() method or | operator
    combined = my_set.union(your_set)
    print(f"Union (my_set | your_set): {combined}")
    print(f"Union using '|' operator: {my_set | your_set}")

    # 5. Subset and Superset Tests
    print(f"Is my_set1 {my_set1} a subset of your_set? {my_set1.issubset(your_set)}")
    print(f"Is my_set1 {my_set1} a superset of your_set? {my_set1.issuperset(your_set)}")

    # 6. Difference Update
    # Removes elements found in another set from this set in-place.
    my_set.difference_update(your_set)
    print(f"After difference_update (removing elements from your_set): {my_set}")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What are the key properties of a Set?
    A1: Sets are unordered, unindexed, and contain only unique elements.

    Q2: Can a Set contain a List?
    A2: No, set elements must be hashable (immutable). Lists are mutable, so 
        they cannot be added to a set. Tuples can be added if they contain 
        only immutable items.

    Q3: What is a `frozenset`?
    A3: It is an immutable version of a set. Because it is immutable/hashable, 
        it can be used as a key in a dictionary or an element in another set.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - SETS")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_set_types()
    interview_questions()

