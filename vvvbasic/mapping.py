"""
Mapping Types Module
=============================================================================
Contains examples and use cases for Dictionary types.
=============================================================================
"""

def demonstrate_mapping_types():
    print("\n\n[3] MAPPING TYPE")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Dictionary (dict)
    # -------------------------------------------------------------------------
    # Use Cases: Lookups, Objects/Records, JSON, Caching.
    user_profile = {
        "id": 101,
        "username": "pg871",
        "is_active": True
    }
    
    print(f"Type: {type(user_profile)}")
    print(f"Examples: {user_profile}")
    print("Real-world Use: JSON APIs, Caching configurations, User profiles, Fast lookups.")
