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

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: Are dictionaries ordered in Python?
    A1: As of Python 3.7+, dictionaries are guaranteed to maintain insertion order. 
        Before that, they were unordered.

    Q2: What keys can be used in a dictionary?
    A2: Any *immutable* (hashable) type can be a key. Strings, numbers, and tuples 
        are common. Lists and other dicts cannot be keys.

    Q3: What is the complexity of a dictionary lookup?
    A3: Average case O(1) (Constant time) due to hashing. Verified by hash of the key.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - MAPPING")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_mapping_types()
    interview_questions()

