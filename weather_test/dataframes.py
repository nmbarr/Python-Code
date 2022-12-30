#This code is for all dataframe examples

import numpy as np
import pandas as pd

#Display message above data
def header(msg):
    print('-' * 50)
    print('[ ' + msg + ' ]')

#######################

header("1.  Load hard coded data into dataframe")
df = pd.DataFrame(
    [['Jan',58,42,74,22,2.95],
	['Feb',61,45,78,26,3.02],
	['Mar',65,48,84,25,2.34],
	['Apr',67,50,92,28,1.02],
	['May',71,53,98,35,0.48],
	['Jun',75,56,107,41,0.11],
	['Jul',77,58,105,44,0.0],
	['Aug',77,59,102,43,0.03],
	['Sep',77,57,103,40,0.17],
	['Oct',73,54,96,34,0.81],
	['Nov',64,48,84,30,1.7],
	['Dec',58,42,73,21,2.56]],
	index = [0,1,2,3,4,5,6,7,8,9,10,11],
	columns = ['month','avg_high','avg_low','record_high','record_low','avg_precipitation'])
print(df)

#######################

header("2.  Read text file with data")
text_file = "Fremont weather.txt"
df = pd.read_csv(text_file)
print(df)

#######################

header("3.  First 5 rows of dataframe")
print(df.head())

#######################

header("4.  Last 3 rows of dataframe")
print(df.tail(3))

#######################

header("5.  Get data types, index, columns, values\n")
header("Data Types")
print(df.dtypes)

header("Index")
print(df.index)

header("Columns")
print(df.columns)

header("Values")
print(df.values)

#######################

header("Statistical summary of data")
print(df.describe())

#######################

header("Sort by column")
print(df.sort_values("avg_precipitation", ascending=True))

#######################

header("Slicing records")
print(df.avg_low)
print(df[2:4])
