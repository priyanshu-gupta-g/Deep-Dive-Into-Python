"""
Functions Basics Module
=============================================================================
Contains examples and use cases for Functions, Parameters, Arguments,
Return values, and Variable Scope (Global/Local/Nonlocal).
=============================================================================
"""

def demonstrate_functions():
    print("\n[4] FUNCTIONS BASICS")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Parameters and Arguments
    # -------------------------------------------------------------------------
    def greet(name, role="User"): # 'role' is a default parameter
        return f"Welcome, {name}. Your role is {role}."

    print(greet("Priyanshu", "Admin"))      # Positional arguments
    print(greet(role="Guest", name="Bob"))  # Keyword arguments
    print(greet("Charlie"))                 # Default argument used

    # -------------------------------------------------------------------------
    # B. *args and **kwargs
    # -------------------------------------------------------------------------
    # *args: Tuple of positional arguments
    # **kwargs: Dictionary of keyword arguments
    def varied_inputs(*args, **kwargs):
        total = sum(args)
        prefix = kwargs.get('prefix', 'Sum')
        return f"{prefix}: {total}"
    
    print(f"\n*Args/**Kwargs: {varied_inputs(1, 2, 3, 4, prefix='Total Value')}")

    # -------------------------------------------------------------------------
    # C. Scope: Global vs Local
    # -------------------------------------------------------------------------
    print("\nScope Rules (LEGB - Local, Enclosing, Global, Built-in):")
    total = 0 # Global

    def count_local():
        total = 5 # Local
        return total
    
    def count_global():
        global total
        total += 1 # Modifies global variable
        return total

    print(f"  Local Scope: {count_local()}")
    print(f"  Global Scope Modified: {count_global()}")

    # -------------------------------------------------------------------------
    # D. Nested Functions & Nonlocal
    # -------------------------------------------------------------------------
    def outer():
        x = "local"
        def inner():
            nonlocal x # Refers to 'x' in 'outer' function, not global
            x = "nonlocal"
            print("  Inner:", x)
        inner()
        print("  Outer:", x)
    
    print("Nested Scope:")
    outer()

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is the difference between `*args` and `**kwargs`?
    A1: `*args` collects extra positional arguments into a tuple. 
        `**kwargs` collects extra keyword arguments into a dictionary.

    Q2: Explain the LEGB rule for Python scope.
    A2: It determines the order in which Python looks up variable names:
        1. Local (inside function)
        2. Enclosing (inside enclosing functions defined within)
        3. Global (module level)
        4. Built-in (Python built-ins like `len`, `str`)

    Q3: Why should you avoid mutable default arguments (e.g., `def f(a=[])`)?
    A3: Default arguments are evaluated only ONCE when the function is defined, 
        not every time it is called. If a mutable object (list, dict) is modified 
        in the function, that change persists across future calls.
        *Fix*: use `None` as default and assign generic list inside function.

    Q4: What is the purpose of the `global` and `nonlocal` keywords?
    A4: `global` allows modifying a global variable inside a local scope.
        `nonlocal` allows modifying a variable in the nearest enclosing scope 
        (that is not global).
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - FUNCTIONS")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_functions()
    interview_questions()
