"""
VVVBASIC Package
=============================================================================
A comprehensive deep dive into Python Data Types, split into modules.
This __init__.py serves as the header file exposing all types.
=============================================================================
"""

from .numeric import demonstrate_numeric_types
from .sequence import demonstrate_sequence_types
from .mapping import demonstrate_mapping_types
from .sets import demonstrate_set_types
from .boolean import demonstrate_boolean_types
from .binary import demonstrate_binary_types
from .special import demonstrate_special_types

def run_all():
    print("="*80)
    print(" PYTHON DATA TYPES DEEP DIVE (MODULARIZED)")
    print("="*80)
    
    demonstrate_numeric_types()
    demonstrate_sequence_types()
    demonstrate_mapping_types()
    demonstrate_set_types()
    demonstrate_boolean_types()
    demonstrate_binary_types()
    demonstrate_special_types()

    print("\n" + "="*80)
    print(" END OF DEEP DIVE")
    print("="*80)

if __name__ == "__main__":
    run_all()
