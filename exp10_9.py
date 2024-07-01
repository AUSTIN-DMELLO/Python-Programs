import pandas as pd
file="C:\\Users\\LENOVO\\Downloads\\Diabetes Missing Data.csv"
frame=pd.read_csv(file)
print("CSV File:\n",frame,"\n")
print("First five rows:\n",frame.head(),"\n")
print("Last five rows:\n",frame.tail(),"\n")
print("Summary statistics:\n",frame.describe())