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

# --------------------------------------------------------------------

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

# --------------------------------------------------------------------

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

# --------------------------------------------------------------------

#AGGREGATING AND SUMMARIZING

#DataFrame Methods
# .count()
# .min()
# .max()
# .first()
# .last()
# .sum()
# .prod() #product 
# .mean()
# .median()
# .std()
# .var() #variance

#All methods can be run on rows or colums
#Rows - default, axis=0, axis='rows'
#Columns - axis=1, axis='columns'
#To use on a single column or row use the loc and iloc functions

# --------------------------------------------------------------------

#ADDING AND REMOVING COLUMNS

#Adding
data = {'DATE':['1929-01-01','1930-01-01','1931-01-01','1932-01-01'],
        'PCDGA':[9.829,7.661,5.911,3.959],
        }
pce = pd.DataFrame(data)
pce.set_index('DATE',inplace=True)
print(pce)
#method 1: Via a list
pce['PCND'] = [33.941, 30.503,25.798000000000002,20.169]
print(pce)
#method 2: Via a Series DataFrame
pcesv = pd.DataFrame({'DATE':['1929-01-01','1930-01-01','1931-01-01','1932-01-01'],
                      'PCESV':[33.613,31.972,28.963,24.587]})
pcesv.set_index('DATE', inplace=True)
pce['PCESV'] = pcesv
print(pce)
#method 3: Via other columns
pce['PCE'] = pce['PCDGA'] + pce['PCND'] + pce['PCESV']
print(pce)
#method 4: Via a CSV or data file using the .read_** methods

#Removing
pce.drop(columns=['PCDGA', 'PCND', 'PCESV'],
         axis=1,
         inplace=True) #inplace arg. changes current DF instead of prdoucing a new one
print(pce)

# --------------------------------------------------------------------

#ADDING AND REMOVING ROWS

#Adding
#method 1: concat method (append is depreciated)
data = {'PCE':[45.945]}
new_row = pd.DataFrame(data,index=['1933-01-01'])
print(new_row)
pce = pd.concat([pce, new_row],) #add more DFs to append multiple
print(pce)

#Removing
#drop method, axis=0 or default
pce.drop(['1929-01-01',
          '1930-01-01'],
        inplace=True)
print(pce)

# --------------------------------------------------------------------

#OPERATIONS ON DATAFRAMES
#you can multiply an entire DataFrame by a value
#ec = 0.88
#pce * ec
#print(pce)
#you can use the map function to create a new column
def convert_to_euro(x):
    return x * 0.88

pce['EURO'] = pce['PCE'].map(convert_to_euro)
print(pce)
#map - elements ina column (series)
#apply - Across rows or columns
data = {'GCE':[9.622,10.273,10.169,8.946],
        'GPDI':[17.170,11.428,6.549,1.819],
        'NE':[0.383,0.323,0.001,0.043],
        'PCE':[77.383,70.136,60.672,48.715]}
gdp = pd.DataFrame(data, index=['1929-01-01',
                                '1930-01-01',
                                '1931-01-01',
                                '1932-01-01'])
print(gdp)
#Calculate gdp by summing up the rows using the apply method
import numpy as np
gdp['GDP'] = gdp.apply(np.sum, axis=1)
print(gdp)

# --------------------------------------------------------------------

#HEAD method
# df.head() shows the first 5 rows of the DataFrame
# We can specify the # of rows to show by entering a integer
# df.head(3) for the first 3 rows

#TAIL method
# df.tail() shows the last 5 rows of the DataFrame
#df.tail(3) shows the last 3 rows

#DESCRIBE method
# df.describe()
# outputs a statistical summary of the DataFrame
# By default it will return summary statistics on all numerical columns
# Count of the rows, the mean value across the rows, std, the min. value, percentiles (25%, 50%, 75%), and the max value
# describe takes 3 optional arguments:
# 1. include= specify the cols. you wish to be included in the statistics or 'all' for all cols or the dtypes you wish to include (i.e. ['float', 'object'])
# 2. exclude= works in the opposite way of include
# 3. percentiles= takes a list of the percentiles you wish to see (i.e. [.1, .5, .9] for the 10%,50%,90%)

# --------------------------------------------------------------------

#FILTERING DATA
# 
# Column Comparison
# prices is a DF
# Ex 1:
# prices.high > 2160 or prices['high'] > 2160
# The output is a sequence of boolean values
# True for whose value is true for the comparison, and false for the rest
# Ex 2:
# prices.Symbol == 'AAPL' or prices['Symbol'] == 'AAPL'
# Again outputs a sequence of boolean values based on the comparison
# Ex 3:
# mask_symbol = prices.Symbol == 'AAPL'
# aapl = prices.loc[mask_symbol]
# Placing the boolean values into the loc method will return a DataFrame with only the rows that reported True based on the comparison

#Pandas Boolean Operators
# And = &
# Or = |
# Not = ~

#Combining Comparison Conditions
# Ex:
# mask_prices = prices['Symbol'] != 'AMZN'
# mask_date = historical_highs['Date'] > datetime(2020, 4, 1)
# mask_amzn = mask_prices & mask_date
# prices.loc[mask_amzn]
# Resulting DataFrame has only rows that match both conditions\

# --------------------------------------------------------------------

#PLOTTING DATA
# pandas DataFrames can plot to matplotlib using the .plot() method
# simply supply the columns to use for the x and y axises as arguments
# df.plot(x= ,y= )
# plot method offers a lot of argument options
# leaving out the x argument defaults to the index
# 
# default plot type is the 'line' plot other plot types include:
# bar
# barh
# hist
# box
# kde - kernel density estimation
# density
# area
# pie
# scatter
# hexbin
# (Use the kind='line' arg. to change the type of plot)
#  