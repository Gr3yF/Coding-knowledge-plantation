#METHODS

# method = a function that is only available to a specific data type
# Syntax - variable.method()

# --------------------------------------------------------------------

#FUNCTIONS

# Function = a code to perform a task
# There are many built-in functions that do all sorts of things
# Syntax - function(<variable/data structure>)
# Depending on the function it can also have other necessary arguments or options
# NOTE: you can call a function within a function

# help(<function_name> or <dtype> or <structure>) - returns information on the inputted function 
#
# type() - checks the data type of a variable, value, or function
#
# print() - displays outputs
#
# range(start_index#,end_index#,step_default_1) - used with a for loop
#
# max() - find the largest value in a data structure
#
# min() - find the smallest value in a data structure
#
# sum() - add up all elements in a data structure
#
# round(#,#_of_decimals) - trim a float to a specified # of decimal places
#
# len() - counts the number of elements of a variable, incompatible with floats, int, or bool dtypes
#
# sorted() - sort elements in a data structure in ascending order

# Defining a custom function:
# General syntax - def <function_name>(argument(s)):
#                       <code block>
def average(values):
    """This is a docstring which is used to help others
    understand how to use the function. This function
    finds the mean in a sequence of values and round to
    two decimal places."""
    #calculate the average
    average_value = sum(values)/len(values)
    #round results
    rounded_average = round(average_value, 2)
    #return result
    return rounded_average #only when you need to return a value

sales = [125.97,84.32,99.78,154.21,78.50,83.67,111.13]
print(average(sales))
# more complex function adding keyword argument and defaults
def average(values, rounded=False):
    """
    Find the mean in a sequence of values and round to two
    two decimal places.

    Args:
        values (list): A list of numeric values.
    
    Returns:
        rounded_average (float): The mean of values,
        rounded to two decimal places.
    """
    # Round average to two decimal places if rounded is True
    if rounded == True:
        average_value = sum(values)/len(values)
        rounded_average = round(average_value, 2)
        return rounded_average
    else:
        average_value = sum(values)/len(values)
        return average_value

print(average(sales,True))
print(average(sales))
print(average(sales,rounded=False))
#print(help(average))

# Accessing & Updating a docstring:
# General syntax - <function>.__doc__
# Two sets of double underscores are referred to as "dunder" in programming
# .__doc__ - "dunder-doc" attribute of the <function>
print(average.__doc__)
# Since it is an attribute you can also update it as follows:
average.__doc__ = "Calculate the mean of values in a data structure, rounding the results to 2 digits"
print(average.__doc__)

# Arbitrary Arguments:
# Allow functions to accept any number of arguments
def average(*args): #conventional naming - "*args" 
    #calculate the average
    average_value = sum(args)/len(args) 
    #round results
    rounded_average = round(average_value, 2)
    #return result
    return rounded_average #only when you need to return a value
# Allows a variety of uses while producing expected results!
# Calling average with six positional arguments
print(average(15, 29, 4, 13, 11, 8))
# * - tells python to convert args. to a single iterable(tuple)
# Calculating across multiple lists
print(average(*[15, 29], *[4,13], *[11,8])) #same result

# Arbitrary keyword arguments:
# General syntax - **kwargs (conventional naming)
# keyword_arg = value, this is equivalent to the key-value pairs that we've seen in dictionaries
# To enable this, we first modify our function as follows
def average(**kwargs):
        #calculate the average
    average_value = sum(kwargs.values())/len(kwargs.values()) #changed with the presumption dictionaries will be used, now working with the dot-values method of our kwargs
    #round results
    rounded_average = round(average_value, 2)
    #return result
    return rounded_average #only when you need to return a value
# Calling average with six kwargs
print(average(a=15, b=29, c=4, d=13, e=11, f=8))
# Calling average with one kwarg
print(average(**{'a':15,'b':29,'c':4,'d':13,'e':11,'f':8}))
# Calling average with three kwargs
print(average(**{'a':15,'b':29}, **{'c':4,'d':13}, **{'e':11,'f':8}))

# Lambda functions:
# lambda keyword - represents an anonymous function
# General syntax - lambda argument(s): expression
# convention is to use x for a single argument
# the expression is equivalent of the function body
# No return statement required to produce an output
# Creating a lambda function:
lambda x: sum(x) / len(x) #lambda average function equivalent to the average function above
# To use the lambda function: place inside parenthesis
# Get the average
print((lambda x: sum(x) / len(x))([3,6,9]))
# Store lambda functions as a variable
average = lambda x: sum(x) / len(x)
# Call the average function like a regular function
print(average([3,6,9])) #provide the list that represents x
# Lambda function with two arguments
print((lambda x, y: x**y)(2, 3))
# Lambda functions with iterables
# Use built-in map() function
# map() applies a function to all elements in an iterable
names = ["john", "sally", "leah"]
# Apply a lambda function inside map()
capitalize = map(lambda x: x.capitalize(), names)
print(capitalize) #shows a map object pointing to the memory location where this function is stored.
# To produce an output convert it to a data structure
# Convert to a list
print(list(capitalize))
# NOTE: use lambda functions when the task is simple or needs only to be performed once

# --------------------------------------------------------------------

#MODULES

# Modules are Python scripts (single python file) and contain functions and attributes and, also, can contain other modules
# There are around 200 built-in modules
# Modules help us avoid writing code that already exists
# Full list of modules - https://docs.python.org/3/pymodindex.html

# Common modules include:
# 
# os - for interpreting and interacting with your operating system
# 
# collections - advanced data structure types and functions
# 
# string - performing string operations
# 
# logging - to log information when testing or running software
# 
# subprocess - to run terminal commands

# Import module to use it:
# General syntax - import <module_name>
import os
type(os) # returns <class 'module'>

# Finding a module's functions:
# functions perform a task
# Call help()
# Warning - will return a very large output!
#help(os)
# Or go online to docs.python.org
# example function:
print(os.getcwd())

# Module attributes:
# Attributes have values
# General syntax - <module_name>.attribute

# Importing a single/specific function(s) from a module:
# Importing a whole module can require a lot of memory
# Can import a specific function from a module:
from os import chdir #only imported the chdir function
from os import chdir, getcwd #imported chdir & getcwd only
#when you do this you no longer need to include os when calling the function
print(getcwd())
# this is because we have not imported the os module and therefore doesn't know what it is

# --------------------------------------------------------------------

#PACKAGES

# A collection of modules = PACKAGE
# Can also be referred to as libraries
# Publicly available and free
# Code within is known as source code
# Imported into a script the same way as modules once downloaded

# Download a package from PYPI
# Open terminal/cmd
# type in "python 3 -m pip3 install <package_name>" downloads source code to our local environment

# Can be useful to assign an alias when working with packages
# To do this use "as"
import pandas as pd #here pd is the alias which needs to be used to use the package throughout the script

# --------------------------------------------------------------------

#STRINGS

#Create strings:
# Can be created using single or double quotes
#i.e.
s_str = 'Hello, I am well.'
d_str = "She's too cool for me."
#double quotes must be used when you wish to include an apostrophe
#otherwise you will have syntax issues with single quotes

#methods:
# .replace() - replace values in a str
# replace Hello with Welcome
s_str = s_str.replace('Hello', 'Welcome')
print(s_str)

# .lower() - convert to lowercase
current_top_album = "For All The Dogs"
current_top_album = current_top_album.lower()
print(current_top_album)

# .upper() - convert to uppercase
current_top_album = current_top_album.upper()
print(current_top_album)

#Multi-line strings - use 3 double quotes to open & close
#Create a string variable over multiple lines
harry_potter = """Mr. and Mrs. Dursley,
of number four Privet Drive,
wer proud to say that they were perfectly normal,
thank you very much."""


# --------------------------------------------------------------------

#LIST

#list=store multiple values in a single variable
#create a list:
a_list = [1, 2, 3, 4, 5] #int list
print(a_list)

#lists can hold three types of variables; int or float, str, and bool
f_list = [12.2, 13.5, 15.6] #float list
s_list = ['sup', 'my', 'dude']
bool_list = [True, True, False]
print(f_list, '\n', s_list, '\n', bool_list)

#methods:
# .append() method - add a value to a list
s_list.append('Hey')
print(s_list)

#functions:
#type() to check the data type of a list
print(type(s_list))
print(type(bool_list))
print(type(f_list))
#always will return <class 'list'> regardless of dtype stored in the list

#indexing:
#lists are ordered, with each value receiving an index#
#python counts values starting from zero for the first element
#Subestting/Indexing Syntax = a_list[index#]
print(s_list[0])
print(f_list[2])
print(bool_list[1])
print(s_list[-1])
#slicing for multiple values indexing
#syntax = a_list[starting_index#:ending_index#]
print(s_list[0:2])
print(f_list[-2:]) #leaving it empty after or before the colon makes the slicing go to the end or from the start respectively
#adding a step argument
#syntax = a_list[starting_index#:ending_index#:step_value]
print(s_list[::2]) #returns every 2nd value from the starting_index#
#REMEMBER - slicing in python is exclusive when using index#

# --------------------------------------------------------------------

#DICTIONARIES
#{key:value} pairs separated by a colon, all keys are unique and can only represent one value

#Create an empty dictionary:
#technique 1: empty curly brackets
my_dict = {}
# technique 2: dict function
my_dict = dict()

#Create a dictionary:
ticker_symbols = {'AAPL':'Apple', 'F':'Ford', 'LUV':'Southwest'}
print(ticker_symbols)
#or
ticker_symbols = dict([['APPL','Apple'],['F','Ford'],['LUV','Southwest']])
print(ticker_symbols)

#Adding to dictionaries:
ticker_symbols['XON'] = 'Exxon'
print(ticker_symbols)
#update the value of an existing key
ticker_symbols['XON'] = 'Exxon OLD'

#Accessing values:
#technique 1: indexing
print(ticker_symbols['F'])
#technique 2: .get() method/attribute 
company = ticker_symbols.get('LUV')
print(company)
company = ticker_symbols.get('XOM') #if there is no Key that exists,'None' (or a 2nd arg. str defined by the user) is returned and no error is thrown like in typical indexing
print(company)
company = ticker_symbols.get('XOM','MISSING')
print(company)

#methods:
# .values() - Return all values from a dictionary
print(ticker_symbols.values())

# .keys() - Return all keys from a dictionary
print(ticker_symbols.keys())

# .items() - Return a list of all key, value pairs
# outputs each pair in parentheses known as a tuple
print(ticker_symbols.items())

#functions:
# del() function
# Deleting or removing from a dictionary
del(ticker_symbols['XON'])
print(ticker_symbols) 

# --------------------------------------------------------------------

#SETS

# Contain unique data
# Meaning if we have a set containing a duplicate value, then we will only see one instance of it when we print the set
# Additionally, their values cannot be changed , though values can be added and deleted.
# Searching sets for values in Python is very fast, particularly compared to other data structures such as lists.

# Creating a set:
# Syntax - set = {}
# : = Dictionary
# No : = set
attendees_set = {"John Smith", "Alan Jones", "Roger Thomson",
                 "John Smith", "Brandon Sharp", "Sam Washington"}
print(attendees_set) #John smith only printed once

# functions:
# set() - Converting to a set - Known as Casting
attendees_list = ["John Smith", "Alan Jones", "Roger Thomson",
                 "John Smith", "Brandon Sharp", "Sam Washington"]
# We cast a list as a set
attendees_set = set(attendees_list)
print(type(attendees_set))

# sorted() - Sorting a set
sorted(attendees_set) #Returns a list
print(attendees_set) #Now in alphabetical order

# Limitations of sets:
# - Don't have an index
# - can't subset []

# --------------------------------------------------------------------

#TUPLES

# Immutable - cannot be changed
# Can't add, remove, or change values
# Are ordered and therefore can be subset

# Creating a tuple
# Syntax - tuple = ()
office_locations = ("New York City", "London", "Leuven")

# functions:
# tuple() - convert another data structure to a tuple
attendees = tuple(attendees_list)

# indexing:

# Same as a list with []
print(office_locations[1])

# --------------------------------------------------------------------

#Comparison Operators
# == : equal (test the equality of two values)
# != : not equal
# < : less than
# > : greater than
# <= : equal or less than
# >= : equal or greater than
# You can compare datetimes, numbers, dictionaries, strings, etc. (almost anything)
# Strings are evaluated in alphabetical order.
# Most comparisons can not go across types (int & float one of the exceptions)

# --------------------------------------------------------------------

#BOOLEAN OPERATORS
#3 operators
# AND : logical conjunction (check if mult. cond. are met)
# OR : logical disjunction (check if one or more cond. is met)
# NOT : logical negation
# AND & OR are short circuit operators; AND will check both variables and OR will only check the second if it has to

# --------------------------------------------------------------------

#If STATEMENTS
# Control statement
#   statement 1
#   statement 2
#   statement 3
#       OR
#  Control statement: statement 1; statement 2; statement 3
#
# Control statement (i.e. x<y , x in y , x and y , x)
# if <expression> :
# elif :
# else :

# --------------------------------------------------------------------

#FOR AND WHILE LOOPS
# <control statement> #determines how many times the code block is executed
#   <code block>
#
# for loops control statement:
# for <variable> in <sequence>:
#       <action>
# Read as for each <variable> in a <sequence> perform <action>
# <sequence> is something that can be stepped through (iterable); i.e. list, keys of a dictionary, or a string
# <variable> is an iterator (i.e. index) and can be given any name
# To iterate through a dictionary use the .items() which produces tuples of the keys and values. NOTE: you must provide two iterators (1 for keys and 1 for values)
# If you wish only for the keys or values use the .keys() or .values() methods with a single iterator respectively

# functions:

# range() function
# syntax - range(start, end + 1)
# start = inclusive
# end = not inclusive
# example of use in a for loop
for i in range(1,6):
    print(i)

# while loop control statement:
# while <expression>:
#       <action>
# <expression> should evaluate to True or False
# need to make sure the while loop can end (can use "continue" or "break")
# can use control+c/command-c if code is already running to break

# "in" keyword:
# in = check if a value is in a variable/data structure
products_dict = {"AG32":10,"HT91":20,
                "PL65":30,"OS31":15,
                "KB07":25,"TR48":35}
if "OS31" in products_dict.keys():
    print(True)
else:
    print(False)

# "not" keyword:
# not = check if a conditions is not met
if "OS31" not in products_dict.keys():
    print(False)
else:
    print(True)

# --------------------------------------------------------------------

#ERRORS

# Code that violates one or more rules
# Error = Exception
# Cause our code to terminate!

# Common Errors:
#
# TypeError - incorrect dtype when performing a task
#
# ValueError - the value is not within an acceptable range (i.e. float("Hello") because float("2") does work)
# 

# Error handling:
# anticipating how errors might occur
# 
# Technique:
# try-except
# Avoid errors being produced
# Still execute subsequent code
def average(values):
    try:
        #Code that might cause an error
        average_value = sum(values) / len(values)
        return average_value
    except:
        #Code to run if an error occurs
        print("average() accepts a list or set. Please provide correct data type")

# raise
# Will produce an error
# Avoid executing subsequent code
def average(values):
    #Check data type
    if type(values) in ["list", "set"]:
        #Run if appropriate data type was used
        average_value = sum(values)/len(values)
        return average_value
    else:
        #Run if an Exception occurs
        raise TypeError("average() accepts a list or set, please provide a correct data type")
    