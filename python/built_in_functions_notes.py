#METHODS

# method=a function that is only available to a specific data type
# syntax = variable.method()

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

#Comparison Operators
# == : equal (test the equality of two values)
# != : not equal
# < : less than
# > : greater than
# <= : equal or less than
# >= : equal or greater than
#You can compare datetimes, numbers, dictionaries, strings, etc. (almost anything)
# Most comparisons can not go across types (int & float one of the exceptions)

# --------------------------------------------------------------------

#BOOLEAN OPERATORS
#3 operators
# AND : logical conjunction
# OR : logical disjunction
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
#<sequence> is something that can be stepped through; i.e. list, keys of a dictionary, or a string
#
# while loop control statement:
# while <expression>:
# <expression> should evaluate to True or False
# need to make sure the while loop can end (can use "continue" or "break")

# --------------------------------------------------------------------