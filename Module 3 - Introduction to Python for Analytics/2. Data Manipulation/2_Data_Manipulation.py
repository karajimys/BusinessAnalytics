"""
Introduction to Python for Analytics: Data Manipulation

In this file we will see:

1. An Introduction to Pandas
2. Reading Data with Pandas
3.Data Manipulation with Pandas
4. Data Cleaning with Pandas
"""

##############################################################################
# 1. An Introduction to Pandas
##############################################################################
# https://pandas.pydata.org/
# https://pandas.pydata.org/pandas-docs/stable/
# https://pandas.pydata.org/docs/reference/frame.html
# https://ajgoldstein.com/podcast/ep23/

# Import the module called Pandas
import pandas as pd


##############################################################################
# 2. Reading Data with Pandas
##############################################################################
# Let's first read our the Sample Superstore Excel file and specifically the first sheet of Orders
pd.read_excel("data/Sample Superstore.xls", sheet_name='Orders')

#read the dataset from the folder
df = pd.read_csv("data/iris.csv")
type(df)

#see the dataset
df

#see the first rows of the dataset
df.head()

#see the last rows of the dataset
df.tail(10)

#see some random rows
df.sample(5)

##############################################################################
# 3. Data Manipulation with Pandas
##############################################################################

#Selecting and Subsetting Data
#see the first rows of a specific column
df['class'].head()

#choose specific columns - version 1
cols = ['sepal_length', 'sepal_width', 'class']
df[cols].head()

#choose specific columns - version 2
df[['sepal_length', 'sepal_width', 'class']].head()

# iloc is a purely integer-location based indexing for selection by position.
#It is primarily integer position based (from 0 to length-1 of the axis)
df.iloc[:,:]

# Here we select the five first rows of the dataset (from index 0 to index 4)
df.iloc[0:5,:]

# Here we select the shell in the 
# first row (0:1->that means the index 0 or first row) &
# forth column (3:4-> that means the index 3 or the forth column)
df.iloc[0:1,3:4]

# Here we select the shells in the 
# first & second rows (0:2->that means the index 0 & 1 or first & second rows) &
# second & third column (1:3-> that means the index 1 & 2 or the second & third column)
df.iloc[0:2,1:3]

# Here we select the shells in the 
# second & third rows (1:3-> that means the index 1 & 2 or the second & third rows) &
# first & second columns  (0:2->that means the index 0 & 1 or first & second columns) 
df.iloc[1:3,0:2]

# The concept of mask in Python
# The mask() method replaces the values of the rows where the condition evaluates to True
bool_mask = df['class'] == 'Iris-virginica'
bool_mask

# here we actually select all rows where the mask is true, or in our case where df['class'] == 'Iris-virginica'
df[bool_mask]

# Here we select the rows where the above mask is true & the petal_length is above 6.0
df[ bool_mask & (df['petal_length'] > 6.0) ]

# The same as above with other words
df[ (df['class']=='Iris-virginica') & (df['petal_length'] > 6.0) ]



#Grouping, Transforming Data
# aggregation functions - sum 
df.groupby('class').sum()

# aggregation functions - mean 
df.groupby('class').mean()

# creating new columns
df['sepal_area'] = df['sepal_length']*df['sepal_width']
df['petal_area'] = df['petal_length']*df['petal_width']

df.head()


# single column calculations
mean_petal_area = df['petal_area'].mean()
mean_petal_area

# Describe the numerical column
df['petal_area'].describe()


# apply a function that you define
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.apply.html
def large_petal_area(petal_area):
    if petal_area > mean_petal_area:
        return "large"
    else:
        return "not_large"
    
df['petal_area'].apply(large_petal_area)

# Create a new column with the apply function
df['large_petal_area'] = df['petal_area'].apply(large_petal_area)
df.head()

# pivot table
# Find mean (or other aggregates) values of columns/variables per class(another variable)
# values  = columns to aggregate
# index   = column, Grouper
# aggfunc = function, list of functions, dict, default numpy.mean
df.pivot_table(values=['petal_area', 'petal_length'], index='class', aggfunc='mean')

# pivot table
# Count number of cases per column large_petal_area and class
# fill_value = Value to replace missing values with, (in the resulting pivot table, after aggregation). default None
table1=df.pivot_table(columns='large_petal_area', index='class', values='petal_area', aggfunc='count' )
table2=df.pivot_table(columns='large_petal_area', index='class', values='petal_area', aggfunc='count', fill_value=0)

print(table1)
print(" ")
print(table2)

# pivot table
# mean values for all numerical columns
df.pivot_table( index=['class'], aggfunc='mean') 

##############################################################################
# 4. Data Cleaning with Pandas
##############################################################################
"""
Below we give examples of cleaning data in Pandas:

 -How do we treat outliers?

 -How do we treat missing data?

There is not a unique answer!

For example here:

-We drop the top 5% and low 5% of observations as outliers

-We fill (impute) missing data with mean values of the variables
"""
# Import the module called Numpy
import numpy as np

# Define the function for finding the IQR (ενδοτεταρτημοριακό εύρος)
def find_IQR(series):
    Q75, Q25 = np.percentile(series, [75 ,25])
    IQR = Q75 - Q25
    
    return IQR

# Show the IQR of the column sepal_length
find_IQR(df['sepal_length'])

# Define a function to find the values that define the IQR
def find_Q25_Q75(series):
    Q75, Q25 = np.percentile(series, [75 ,25])
    return Q25, Q75


# Values of the 25th and 75th percintiles of variable sepal_length
find_Q25_Q75(df['sepal_length'])

# Value of the 25th percentile
print(find_Q25_Q75(df['sepal_length'])[0])

#Value of the 75th percentile
print(find_Q25_Q75(df['sepal_length'])[1])

# With the same way we defince the 5th and 95th percentiles
def find_Q5_Q95(series):
    Q95, Q5 = np.percentile(series, [95 ,5])
    return Q5, Q95

# Values of the 5th and 95th percintiles of variable sepal_length
print(find_Q5_Q95(df['sepal_length'])[0], find_Q5_Q95(df['sepal_length'])[1])

# We find the outliers for the variable sepal_length in our dataset 
# by using the above values as the cut-offs for the top 5% & low 5% of the values 
outliers = df[(df['sepal_length'] < 4.6) | (df['sepal_length'] > 7.25)]
outliers

# keep only the no-outliers according to our definition 
not_outliers = df[(df['sepal_length'] >= 4.6) & (df['sepal_length'] <= 7.25)]
not_outliers

##FILLING MISSING DATA
# Now we will fill some missing data with the mean values of the variables
df = pd.read_csv("C:/Users/Dimitris/Google Drive/Work/5. ΠΑΠΕΙ/1. HY-III 2022-23/Module 3 - Introduction to Python for Analytics/intro-to-python-for-data-analysis-master/data/iris_messy.csv")
df

# Let's see some missing data
df.head(10)

# see all missing data by variable
df.isna().sum()

# Find the rows were any of the variables have missing data
na_indexes = df[df.isna().any(axis=1)].index
na_indexes

# See those rows
df[df.isna().any(axis=1)]

# imputing with the mean
# First we create a Dictionary linking the name of each variable with their mean value
values = {'sepal_length': df['sepal_length'].mean(), 
          'sepal_width': df['sepal_width'].mean(), 
          'petal_length': df['petal_length'].mean(), 
          'petal_width': df['petal_width'].mean()}

df.fillna(value=values, inplace = True)

# See the rows by using the indexes where we had rows with missing data
df.iloc[na_indexes,:]

# write the new file to disk 
df.to_csv("data/iris_cleaned.csv")




