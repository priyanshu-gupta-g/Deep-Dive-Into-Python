"""
Functional Programming Module
=============================================================================
Contains examples and use cases for Functional Programming concept:
Pure Functions, Lambda, Map, Filter, Zip, and Reduce.
=============================================================================
"""
from functools import reduce

def demonstrate_functional_programming():
    print("\n[5] FUNCTIONAL PROGRAMMING")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Pure Functions
    # -------------------------------------------------------------------------
    # 1. Always produces the same output for the same input.
    # 2. No side effects (doesn't change global state).
    def multiply_by_2(item):
        return item * 2

    print(f"Pure Function Output (2*2): {multiply_by_2(2)}")

    # -------------------------------------------------------------------------
    # B. Map()
    # -------------------------------------------------------------------------
    # Syntax: map(function, iterable)
    my_list = [1, 2, 3]
    mapped_list = list(map(multiply_by_2, my_list))
    print(f"\nMap (Original: {my_list}): {mapped_list}")

    # -------------------------------------------------------------------------
    # C. Filter()
    # -------------------------------------------------------------------------
    # Syntax: filter(function, iterable)
    def check_odd(item):
        return item % 2 != 0

    filtered_list = list(filter(check_odd, my_list))
    print(f"Filter (Odd from {my_list}): {filtered_list}")

    # -------------------------------------------------------------------------
    # D. Zip()
    # -------------------------------------------------------------------------
    # Zips two iterables together into tuples
    usernames = ['user1', 'user2', 'user3']
    ids = [101, 102, 103, 104] # Extra item is ignored
    zipped = list(zip(usernames, ids))
    print(f"Zip: {zipped}")

    # -------------------------------------------------------------------------
    # E. Reduce()
    # -------------------------------------------------------------------------
    # Accumulates a value
    def accumulator(acc, item):
        return acc + item

    total_sum = reduce(accumulator, my_list, 0)
    print(f"Reduce (Sum of {my_list}): {total_sum}")

    # -------------------------------------------------------------------------
    # F. Lambda Expressions
    # -------------------------------------------------------------------------
    # Anonymous one-line functions
    # lambda param: action(param)
    print("\nLambda Examples:")
    print(f"  Multiply by 3: {list(map(lambda item: item * 3, my_list))}")
    print(f"  Filter Even: {list(filter(lambda item: item % 2 == 0, my_list))}")

# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is a Pure Function?
    A1: A function that:
        1. Given the same input, will always return the same output.
        2. Produces no side effects (does not modify external state).

    Q2: What is the difference between `map` and `filter`?
    A2: `map` transforms every element in an iterable based on a function.
        `filter` returns only the elements that satisfy a condition (True/False).

    Q3: What makes `lambda` functions "anonymous"?
    A3: They are defined without a name (using `lambda` instead of `def`). 
        They are typically used for short, throwaway functions as arguments 
        to HOFs (Higher Order Functions) like map/filter.
    
    Q4: Explain how `reduce` works.
    A4: It takes a function (two arguments: accumulator, current_item) and 
        an iterable. It applies the function cumulatively to the items, 
        reducing the iterable to a single value.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - FUNCTIONAL PROGRAMMING")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_functional_programming()
    interview_questions()
