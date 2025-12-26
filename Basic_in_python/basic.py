# Conditional Logic 

# =============================================================================
# age = True
# licensed = True
# 
# if age: #condition
#     print('ok')
# elif licensed:
#     print('You are licensed')
# else:
#     print('sorry')
#     
# if age and licensed:
#     print('''Everything is ok now 
#           you can drive a car''')
# else:
#     print('Sorry! you can\'t drive now')
#     
# # truthy and false 
# =============================================================================

# =============================================================================
# # Ternary Operator 
# # condition_if_true if codition else condition_if_false 
# is_friend = ''
# print('Allow Messaging') if is_friend else print('Not Allow')
# =============================================================================

# =============================================================================
# # Short Circuiting 
# friend = 0.1
# best = 0.2
# 
# if friend and best:\
#     print('Best Friend Forever')  
# else:
#     print('Just Friend')
# =============================================================================
    
# Logical Operator 
# ==
# >
# <
# >=
# <=
# !=
# and 
# or
# not 

# =============================================================================
# print(4 == 5)
# print(not(True))
# print(not(False))
# 
# logic = 1
# logic2 = not 2
# if logic != logic2:
#     print((True))
# =============================================================================

# =============================================================================
# is_magic = True
# is_good = False
# # exercise
# if is_magic and is_good:
#     print('You are a good magician')
# elif is_magic and not is_good:
#     print('You are getting there')
# else: 
#     print('Unlock Magic Attribute')
#  
# # how sir does
# if is_magic and is_good:
#     print('You are a good magician')
# elif is_magic and not is_good:
#     print('You are getting there')
# elif not is_magic and not is_good : 
#     print('Unlock Magic Attribute')
# =============================================================================

# == vs is 
# =============================================================================
# print(True is 1)# false
# print('' is 1)# false
# print([] is 1)# false
# print(10 is 10.0)# false
# print([] is [])# false
# # is check the memory location
# =============================================================================

# print('\n')

# =============================================================================
# print(True == 1)# true
# print('' == 1)# false
# print([] == 1)# false
# print(10 == 10.0)# true
# print([] == [])# true
# # is compare the two data type 
# =============================================================================

# =============================================================================
# a = [1,2, 3, 4, 5, 6]
# b = [1,2, 3, 4, 5, 6]
# print(a == b)
# print(a is b)
# =============================================================================

# =============================================================================
# # loops serires 
# # for loop
# 
# user = {
#         'name': 'Priyanshu',
#         'age': 10000000000000,
#         'occupation':'bahut bada bussinesman' 
#         }
# 
# # for items in user.items():
# #     print(items)
#     
# # for items in user.keys():
# #     print(items)
#     
# # for items in user.values():
# #     print(items)
# 
# # =============================================================================
# # for k, v in user.items():
# #     print(k, '->',v)
# #     
# # for items in 50:#int float bool are not interable 
# #     print(items)
# # =============================================================================
# 
# # li = [1,2,3,4,5,6,7,8,9,10]
# # i = 0
# # for items in li:
# #     i = i + items
# #     print(i)
# =============================================================================


# Range vs enumerate 
# Range
# print(range())
# for i in range(0,10,2):
#     print('Prime number',i)
# enumerate
# for i in enumerate('Hello'):
#     print(i)

# =============================================================================
# # this element is at this place 
# # li = list(range(1023,12834))
# inp = int(input('Enter your element here: '))
# 
# for i, li in enumerate(range(1023,12834)):
#     if li == inp:
#         print(f'The value {inp} at index {i}')
# =============================================================================
    
# =============================================================================
# var = 0
# while var <= 10:
#     var += 1
#     print(var)
# else:
#     print('Work is done')
# =============================================================================

# =============================================================================
# for i in [1,2,3]:
#     print(i)
# # we are using for loop when we now the exact number for looping 
# # it's mean we know how many i have to loop
#     
# li = [1,2,3]
# i = 0
# while i < len(li):
#     i += 1
#     print(i)
# # in while we can't know how many i have to loop
# =============================================================================

# =============================================================================
# while True:
#     response = input('Tell me somethings: ')
#     if response == 'Bye Sir':
#         break
# =============================================================================

# =============================================================================
# i = 0
# while i < 5:
#     print('Hi')
#     i+= 1
# =============================================================================
# =============================================================================
# # continue 
# # pass 
# 
# li = [
#       [0,0,0,1,0,0,0],
#       [0,0,1,1,1,0,0],
#       [0,1,1,1,1,1,0],
#       [1,1,1,1,1,1,1],
#       [0,0,0,1,0,0,0],
#       [0,0,0,1,0,0,0]
#       ]
# =============================================================================

# =============================================================================
# for row in li:
#     for v in row:
#         if v == 0:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print('')
# =============================================================================

# =============================================================================
# # Find Duplicate
# sl = [1,2,3,4,4,2,5,2,4,2,6,2,8,1,5,4,6,5,6,8,8,9,7,5,4,6,]
# duplicates = []
# 
# for num in sl:
#     if sl.count(num) > 1:
#         if num not in duplicates:
#             duplicates.append(num)
# print(duplicates)
# =============================================================================
        
# =============================================================================
# # function (own function print(), set(),list() and all are in build function)
# def say_my_name():#defining function
#     print('Priyanshu')
#         
# say_my_name()#invoking function
# =============================================================================

# =============================================================================
# # Prameters and Arguments
# def say_my_name(title, name, surname):# Defining function with parameters
#     print(f'{title} {name} {surname}')
# 
# # positional arguments 
# 
# # say_my_name('Python Lerner', 'Gupta')# Invokking fucntion  with argument 
# 
# # keyword arguments 
# 
# # say_my_name( surname = 'Gupta', name = 'Priyanshu', title = 'Python Lerner')# Invokking fucntion  with argument 
# 
# # Default Parameters
# 
# def about(name = 'Priyanshu', surname = 'Gupta'):
#     print(f'{name} {surname}')
# 
# about()
# about('Prince', 'G')
# 
# =============================================================================

# =============================================================================
# # Return 
# # def sum(num1 = 46, num2 = 12):
# #     return num1 + num2
# # print(sum())
# 
# # DRY
# # Return somethings and manipulate data
# def days_to_seconds(days):
#     print('Hello!')
#     return days*24*60*60# after "return" it's was stoped and didn't go enxt step/code 
#     print('Hello!')# it's can't be execute anythings 
# 
# print(days_to_seconds(8))
# 
# # nested function
# def days_to_seconds(days):
#     def day_sec(days):
#         return days*24*60*60# after "return" it's was stoped and didn't go enxt step/code 
#     return day_sec(days)
# 
# print(days_to_seconds(8))
# =============================================================================

# function vs methods 
'''Function and Method are very difference 
   because Method are object that are depedence on something else
   and funcion are independent'''
   
# def anythings():
#     print(5+6)
    
# anythings()

# print('hellooooo'.capitalize())
# print('hellooooo'.upper())

# =============================================================================
# 
# # A Simple Class with Methods (this was generated by ai not myself)
# class Calculator:
#     # Constructor method (called when you create an object)
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
# 
#     # Method to add numbers
#     def add(self):
#         return self.a + self.b
# 
#     # Method to subtract numbers
#     def subtract(self):
#         return self.a - self.b
# 
#     # Method to multiply numbers
#     def multiply(self):
#         return self.a * self.b
# 
#     # Method to divide numbers
#     def divide(self):
#         if self.b != 0:
#             return self.a / self.b
#         else:
#             return "Division by zero not allowed!"
#         
# # Create object
# calc = Calculator(10, 5)
# 
# # Print results
# print("Addition:", calc.add())
# print("Subtraction:", calc.subtract())
# print("Multiplication:", calc.multiply())
# print("Division:", calc.divide())
# =============================================================================


# =============================================================================
# # Using the Methods (this also generate by ai not myself)
# 
# Create an object of Calculator
# calc = Calculator(10, 5)
# 
# print("Addition:", calc.add())        # calls add method
# print("Subtraction:", calc.subtract()) # calls subtract method
# print("Multiplication:", calc.multiply()) # calls multiply method
# print("Division:", calc.divide())     # calls divide method
# =============================================================================

# =============================================================================
# def temp(a):
#     '''
#     This function is pretty useless but it returns param a 
#     '''
#     print(a)
#     
# # temp('a')d
# 
# # Dunder methods 
# print(temp.__doc__)
# =============================================================================


# =============================================================================
# # how make code clean an attractive 
# def is_even_or_odd(a):
#     '''
#     
# 
#     Parameters
#     ----------
#     a : Takes a number.
# 
#     Returns
#     -------
#     bool
#         DESCRIPTION. To check if the number passed as param is even or odd
# 
#     '''
#     if a % 2 == 0:
#         return True
#     return False
#     
# print(is_even_or_odd(5))
# =============================================================================

# *args and **kwarp

# =============================================================================
# def super_func(*args):
#     return sum(args)
# 
# print(super_func(1,2,3,4,5))
# =============================================================================

# =============================================================================
# def super_func(*args, kwargs):
#     print(args, kwargs)
#     # return sum(args, kwargs.values())
# 
# print(super_func(1,2,3,4,5, first = 1, second = 2))
# =============================================================================
# =============================================================================
# 
# def super_func(name, *args, last_name, **kwargs):
#     total = 0
#     for item in kwargs.values():
#         total += item
#     return sum(args, total)
# 
# print(super_func(1,2,3,4,5,6, first = 10, second = 20))
# 
# #  Rules : def somethings(parameter, *args, default param, **kwargs)
# =============================================================================
 

# =============================================================================
# # highest even
# 
# li = [2,10,4,623,9,21,92,83]
# def highest_even(number):
#     evens = []
#     for i in number:
#         if i %2 == 0:
#             evens.append(i)
#         print(evens)
#     return max(evens)
# 
# print(highest_even(li))
# =============================================================================


# =============================================================================
# # Scope
# 
# a = 10 # Global variable 
# 
# def confusion():
#     a = 15 # Local variable
#     print(a)# now it will print local variable 
#     
# def parent():
#     a = 20 # Parent Local Variable 
#     def confusion():
#         # now it will call a parent variable 
#         print(a)
#         
#     return confusion()
# 
# def parent1():
#     # now it will call a Global variable 
#     def confusion():
# 
#         print(a)
#         
#     return confusion()
# 
# # print(a)
# confusion()
# parent()
# parent1()
# 
# # Scope Rules
# # 1. Local variable 
# # 2. Parent local
# # 3. Global variable
# =============================================================================


# =============================================================================
# # Global and Non Local
# 
# total = 0
# 
# def count1():
#     global total
#     total += 1
#     print(total)
#     
# # print(count1())
# 
# def count(total):
#     total += 1
#     return total
# 
# # print(count(count(count(count(count(count(count(count(0)))))))))
# 
# def local():
#     x = 'Local'
#     def nonloc():
#         nonlocal x 
#         x = 'NOn Local'
#         return x
#         print(x)
#     nonloc()
#     print(x)
# 
# print(local())
# =============================================================================
        

# Pure Function 

# Shuld always produce the same output for the same input
# Should not create any side effects
# map(), filter(), zip() and reduce()


# def mul_by_2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list


def mul_by_2(items):
    return items*2

# print(mul_by_2([1,2,3]))

print(list(map(mul_by_2, [1,2,3])))






    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    




 













































































































































































































































































































































































































































































































































































































































































































































































