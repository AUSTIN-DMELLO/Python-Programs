import pandas as pd
file="C:\\Users\\LENOVO\\Downloads\\Diabetes Missing Data.csv"
frame=pd.read_csv(file)
print("CSV File:\n",frame,"\n")
missing_values=frame.isnull().sum()
print("Missing Values:")
print(missing_values)
frame.fillna(frame.mean(),inplace=True)
print("Dataframe after filling the missing values with mean values:\n",frame)