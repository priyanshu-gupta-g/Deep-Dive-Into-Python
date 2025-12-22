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
