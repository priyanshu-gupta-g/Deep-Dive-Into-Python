"""
OOP Concepts and Clean Code Module
=============================================================================
Contains examples and use cases for Classes, Objects, Methods vs Functions,
Docstrings, and Clean Code practices.
=============================================================================
"""

def demonstrate_oop():
    print("\n[6] OOP & CODE QUALITY")
    print("-" * 20)

    # -------------------------------------------------------------------------
    # A. Class and Object
    # -------------------------------------------------------------------------
    class Player:
        # Class Object Attribute (Static-like)
        membership = True

        # Init (Constructor) Method
        def __init__(self, name, age):
            self.name = name  # Attribute
            self.age = age

        # Instance Method
        def shout(self):
            return f"My name is {self.name}!"

        # Class Method
        @classmethod
        def adding_things(cls, num1, num2):
            return num1 + num2

    # Instantiation
    player1 = Player('Cindy', 20)
    print(f"Object Created: {player1.name}, Age: {player1.age}")
    print(f"Method Call: {player1.shout()}")
    print(f"Class Attribute: Player.membership = {Player.membership}")

    # -------------------------------------------------------------------------
    # B. Functions vs Methods
    # -------------------------------------------------------------------------
    # Function: independent, called by name -> my_func()
    # Method: owned by an object, called on object -> obj.my_method()
    
    def separate_function():
        return "I am a function"
    
    print(f"\nFunction: {separate_function()}")
    # player1.shout() is a Method

    # -------------------------------------------------------------------------
    # C. Docstrings
    # -------------------------------------------------------------------------
    def complex_calculation(a, b):
        """
        Performs a complex calculation.
        
        Parameters:
        a (int): First number
        b (int): Second number
        
        Returns:
        int: The sum of a and b
        """
        return a + b
    
    print("\nDocstring Check:")
    print(complex_calculation.__doc__)

    # -------------------------------------------------------------------------
    # D. Clean Code Practices
    # -------------------------------------------------------------------------
    # 1. Meaningful Names: `user_age` vs `a`
    # 2. Single Responsibility: Function should do one thing
    # 3. DRY (Don't Repeat Yourself)
    
    def is_even(num):
        """Checks if a number is even."""
        return num % 2 == 0 # Clean boolean return

    print(f"\nClean Code Example (is_even 4): {is_even(4)}")


# =============================================================================
# INTERVIEW QUESTIONS
# =============================================================================
def interview_questions():
    """
    Q1: What is the `__init__` method?
    A1: It is the constructor method in Python. It is automatically called 
        when a new instance (object) of a class is created. It initializes 
        the object's state (attributes).

    Q2: What is `self` in Python?
    A2: `self` represents the instance of the class. By using `self`, we can 
        access the attributes and methods of the class in Python. It binds 
        the attributes with the given arguments.

    Q3: Distinction between Class Method vs Static Method?
    A3: 
        - @classmethod: Takes `cls` as first param. Can access class state.
        - @staticmethod: No implicit first param. Behaves like a regular function 
          but belongs to the class namespace. Can't access class/instance state.
    
    Q4: Why use Docstrings?
    A4: They provide a convenient way of associating documentation with 
        Python modules, functions, classes, and methods. Accessible via `.__doc__` 
        attribute or `help()`.
    """
    print("\n" + "="*30)
    print(" INTERVIEW QUESTIONS - OOP")
    print("="*30)
    print(interview_questions.__doc__)

if __name__ == "__main__":
    demonstrate_oop()
    interview_questions()
