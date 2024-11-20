import pandas as pd

#Pandas DataFrame
#Create an empty dataframe
pd.DataFrame()

#Columns run along the top and the index is the numbers on the left

#Create DataFrame FROM DICT
data = {'Bank Code': ['BA', 'AAD', 'BA'],
        'Account#': ['ajfdk2', '1234nmk', 'mm3d90'],
        'Balance': [1222.00, 390789.11, 13.02]}

df = pd.DataFrame(data=data)
print(df) #here the keys of the dict are columns
 
 #Create DataFrame FROM LIST OF DICTS
data = [{'Bank Code': 'BA', 'Account#': 'ajfdk2', 'Balance': 1222.00},
         {'Bank Code': 'AAD', 'Account#': '1234nmk', 'Balance': 3970789.11},
         {'Bank Code': 'BA', 'Account#': 'mm3d90', 'Balance': 13.02}]

df = pd.DataFrame(data=data)
print(df) #here each dict is a row

#Create DataFrame FROM LIST OF LISTS
data = [['BA', 'ajfdk2', 1222.00],
        ['AAD', '1234nmk', 390789.11],
        ['BA', 'mm3d90', 13.02]]

df = pd.DataFrame(data=data)
print(df) #the columns in this case will  be given numbers identifiers
#you can specify columns using the column argument
columns = ['Bank Code', 'Account#', 'Balance']
df = pd.DataFrame(data=data, columns=columns)
print(df)

#Create DataFrame FROM EXISTING FILR OR DATABASE
#Reading Data
# Excel : pd.read_excel
# JSON : pd.read_json
# HTML : pd.read_html
# Pickle : pd.read_pickle
# SQL : pd.read_sql
# CSV : pd.read_csv('<path.filename.csv>', sep=<separator symbol(i.e. '|')>)
#For a non-comma separated file, 
# supply the separator of the the data in the "sep" arg.

#Accessing Data in DataFrames
accounts = df

#COLUMNS
#Access column using brackets indexing
print(accounts['Balance'])
#Access column using dot-syntax 
# if the column name has no white space or dashes it is added as an attribute to the DataFrame
print(accounts.Balance)
#Access multiple columns 
print(accounts[['Bank Code', 'Account#']])

#ROWS
#Access rows using brackets
#method 1: slice argument
print(accounts[0:2])
#method 2: list of booleans
print(accounts[[True, False, True]])

#loc and iloc functions (recommended especially for large datasets)
# loc : access by name
# iloc : access by position

#LOC (df.loc[rows, columns])
#rows
print(accounts.loc[[0, 2]])
print(df.loc[[True, False, True]])
#columns (column name, list of column names, slice base on column names, or boolean list)
print(accounts.loc[0:2, 'Balance'])
print(accounts.loc[0:2, ['Balance', 'Account#']])
print(accounts.loc[0:2, 'Bank Code':'Balance']) #with names python is inclusive
print(accounts.loc[0:2, [True, False, True]])

#ILOC (df.iloc[rows, columns])
#works with index and column positions rather than names
print(accounts.iloc[0:2, [0,2]])

#You can also use this method to set values (single or multiple)
#single
accounts.loc[0, 'Balance'] = 0
print(accounts) #first row last column value set to 0
#multiple (to the same value)
accounts.iloc[:2, 1:] = 'NA' #setting the first two rows, last two columns to 'NA'
print(accounts)

#TIP: place a colon in the column or row argument to select all



