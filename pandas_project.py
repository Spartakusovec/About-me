# in this project I used pandas to load the data and answer some questions about it
# it probably was even easier than the first project, but I wanted to do it anyway
# Comments r AI generated, i probably wont check this file later, but if i do, its better to have some comments than none


import pandas as pd

# Load the data
sma_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv") 

print(pd.DataFrame(sma_data)) # to get the first 5 rows of the dataset
print(sma_data.info()) # to get the summary statistics

print(sma_data.iloc[9,9]) # to get the value in the 10th row and 10th column
print(sma_data.iloc[-1:,3]) # to get the value in the last row and 4th column

print(sma_data.loc[[1,3,5,7,9,13], ['land_area','work_force','income','region', 'crime_rate']]) # to get the values in the specified rows and columns

print(sma_data[sma_data['region'] == 2]) # to get the rows where the value in the region column is 2


print(sma_data.mean()) # to get the mean of each column
print(sma_data.region.unique()) # to get the unique values in the region column
print(sma_data[['income', 'crime_rate', 'land_area','work_force']].describe()) # to get the summary statistics of the specified columns
print(sma_data['region'].value_counts()) # to get the count of each unique value in the region column

sample_data1 = sma_data[sma_data['region'] == 3] # to get the rows where the value in the region column is 3
print(sample_data1.describe()) # to get the summary statistics of the specified columns
print(sample_data1.isna().sum()) # to get the count of missing values in each column

print(sma_data.sort_values(by='crime_rate', ascending=False)) # to sort the data by the crime_rate column in descending order

titanic = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/titanic_data.csv") 

print(titanic.isna().sum()) # to get the count of missing values in each column
age_mean_before = titanic['Age'].mean() # to get the mean of the Age column
print(age_mean_before) 
age_after = titanic['Age'].fillna(titanic['Age'].mean()) # to fill the missing values in the Age column with the mean of the column
print(age_after.mean())

print(titanic['Embarked'].value_counts()) # to get the count of each unique value in the Embarked column
emb_after = titanic['Embarked'].fillna('S') # to fill the missing values in the Embarked column with 'S'
print(emb_after.value_counts())