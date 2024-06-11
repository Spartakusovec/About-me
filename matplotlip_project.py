# I wanted to practice some more with pandas and matplotlib, so I did this project.
# I used pandas to load the data and matplotlib to visualize it.

import matplotlib.pyplot as plt
import pandas as pd

X = pd.read_csv("https://raw.githubusercontent.com/dphi-official/Datasets/master/Standard_Metropolitan_Areas_Data-data.csv")

plt.scatter(X.crime_rate, X.percent_senior)
plt.show()

plt.plot(X.work_force, X.income)
plt.show()

plt.hist(X.percent_senior)
plt.show()

plt.bar(X.region, X.crime_rate)
plt.show()

print(X.info())
print(X.describe())
print(X.region.value_counts())
print(X.corr())
print(X[X['region'] == 4].head())
# survived_southampton = titanic_data[(titanic_data['Embarked'] == 'S') & (titanic_data['Survived'] == 1)] # just to see how to write similar code
print(X[(X['region'] == 1) & (X['crime_rate'] >= 54.16 )])
print(X[(X['region'] == 3) & (X['land_area'] >= 5000 )].shape)

plt.plot(X['land_area'], X['crime_rate'])
plt.show()

plt.scatter(X['physicians'], X['hospital_beds'])
plt.show()

plt.hist(X['region'])
plt.show()

plt.hist(X['income'])
plt.show()