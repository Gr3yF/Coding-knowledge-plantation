#LIST

#create a list
a_list = [1, 2, 3, 4, 5] #int list
print(a_list)

#lists can hold three types of variables; int or float, str, and bool
f_list = [12.2, 13.5, 15.6] #float list
s_list = ['sup', 'my', 'dude']
bool_list = [True, True, False]
print(f_list, '\n', s_list, '\n', bool_list)

#methods

#functions

#indexing

# --------------------------------------------------------------------

#DICTIONARIES
#{key:value} pairs separated by a colon, all keys are unique and can only represent one value

#Create an empty dictionary
#method #1: empty curly brackets
my_dict = {}
# method #2: dict function
my_dict = dict()

#Create a dictionary
ticker_symbols = {'AAPL':'Apple', 'F':'Ford', 'LUV':'Southwest'}
print(ticker_symbols)
#or
ticker_symbols = dict([['APPL','Apple'],['F','Ford'],['LUV','Southwest']])
print(ticker_symbols)

#Adding to dictionaries
ticker_symbols['XON'] = 'Exxon'
print(ticker_symbols)
#update the value of an existing key
ticker_symbols['XON'] = 'Exxon OLD'

#Accessing values
#method: indexing
print(ticker_symbols['F'])
#method: get attribute 
company = ticker_symbols.get('LUV')
print(company)
company = ticker_symbols.get('XOM') #if there is no Key that exists,'None' (or a 2nd arg. str defined by the user) is returned and no error is thrown like in typical indexing
print(company)
company = ticker_symbols.get('XOM','MISSING')
print(company)

#Deleting or removing from a dictionary
#Use del() function
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