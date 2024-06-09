# First project I did in a long time. I was given a dataset and I had to answer some questions about it.
# Maybe there r some mistakes, but I wanted to refresh my memory and learn something new.
# Obviously ill have to do some more projects to get better at this.
# Anyway.. 
# ENJOY!

import numpy as np;
import pandas as pd;
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

titanic_data = pd.read_csv("https://raw.githubusercontent.com/dphi-official/First_ML_Model/master/titanic.csv", sep=",")
print(titanic_data.head()) # to get the first 5 rows of the dataset
print(titanic_data.shape) # to get the shape of the dataset
print(titanic_data.info()) # to get the summary statistics
print(titanic_data.Sex.value_counts()) # to get the unique values in the quality column
print(titanic_data.isna().sum()) # to get the count of missing values in each column

# Ratio of survived

print(titanic_data.Survived.value_counts()) # to get the count of each unique value in the quality column
ratio_co_prezili = titanic_data.Survived.value_counts()[1]/titanic_data.Survived.value_counts().sum()
print(f"Ratio co prezili: {ratio_co_prezili}")

# Woman who survived

print(titanic_data.describe()) # to get the summary statistics
number_of_female = titanic_data[titanic_data['Sex'] == 'female']
number_of_survived = number_of_female[number_of_female['Survived'] == 1].shape
print(number_of_female)
print(number_of_survived)

# Ratio of survived from first, second and third class

celkem_z_tridy = titanic_data['Pclass'].value_counts()
pocet_z_prvni_tridy = titanic_data[titanic_data['Pclass'] == 1]
pocet_z_druhe_tridy = titanic_data[titanic_data['Pclass'] == 2]
pocet_z_treti_tridy = titanic_data[titanic_data['Pclass'] == 3]
pocet_z_prvni_tridy_survived = pocet_z_prvni_tridy[pocet_z_prvni_tridy['Survived'] == 1].shape
pocet_z_druhe_tridy_survived = pocet_z_druhe_tridy[pocet_z_druhe_tridy['Survived'] == 1].shape
pocet_z_treti_tridy_survived = pocet_z_treti_tridy[pocet_z_treti_tridy['Survived'] == 1].shape

print(f"Prvni trida: {pocet_z_prvni_tridy.shape[0]}, z toho prezilo: {pocet_z_prvni_tridy_survived[0]}")
print(f"Druha trida: {pocet_z_druhe_tridy.shape[0]}, z toho prezilo: {pocet_z_druhe_tridy_survived[0]}")
print(f"Treti trida: {pocet_z_treti_tridy.shape[0]}, z toho prezilo: {pocet_z_treti_tridy_survived[0]}")
ratio_prvni_trida = pocet_z_prvni_tridy_survived[0]/pocet_z_prvni_tridy.shape[0]
ratio_druda_trida = pocet_z_druhe_tridy_survived[0]/pocet_z_druhe_tridy.shape[0]
ratio_treti_trida = pocet_z_treti_tridy_survived[0]/pocet_z_treti_tridy.shape[0]
print(f"Ratio prvni trida: {ratio_prvni_trida}")
print(f"Ratio druha trida: {ratio_druda_trida}")
print(f"Ratio treti trida: {ratio_treti_trida}")
ratio_prvni_celkem = pocet_z_prvni_tridy_survived[0] / titanic_data[titanic_data['Survived'] == 1].shape[0] 
ratio_druhe_celkem = pocet_z_druhe_tridy_survived[0] / titanic_data[titanic_data['Survived'] == 1].shape[0]
ratio_treti_celkem = pocet_z_treti_tridy_survived[0] / titanic_data[titanic_data['Survived'] == 1].shape[0]

print(f"Ratio prvni trida celkem: {ratio_prvni_celkem}")
print(f"Ratio druha trida celkem: {ratio_druhe_celkem}")
print(f"Ratio treti trida celkem: {ratio_treti_celkem}")
print(ratio_prvni_celkem + ratio_druhe_celkem + ratio_treti_celkem)

### survived children and adults

deti_co_prezili = titanic_data[(titanic_data['Age'] < 18) & (titanic_data['Survived'] == 1)].shape[0]
deti_celkem = titanic_data[titanic_data['Age'] < 18].shape[0]
ratio_deti = deti_co_prezili / deti_celkem
print(f"Deti co prezily: {deti_co_prezili}, deti celkem: {deti_celkem}, ratio: {ratio_deti}")
dospeli_co_prezili = titanic_data[(titanic_data['Age'] >= 18) & (titanic_data['Survived'] == 1)].shape[0]
dospeli_celkem = titanic_data[titanic_data['Age'] >= 18].shape[0]
ratio_dospeli = dospeli_co_prezili / dospeli_celkem
print(f"Dospeli co prezili: {dospeli_co_prezili}, dospeli celkem: {dospeli_celkem}, ratio: {ratio_dospeli}")

### survived passangers from southampton
survived_southampton = titanic_data[(titanic_data['Embarked'] == 'S') & (titanic_data['Survived'] == 1)].shape[0]
print(f"Survived from Southampton: {survived_southampton}")

### five highest fares
five_highest_fares = titanic_data.sort_values(by='Fare', ascending=False).head(5)
print(five_highest_fares)

### median age
median_age = titanic_data['Age'].median()
print(f"Median age: {median_age}")

### uniqie values in name column
unique_names = titanic_data['Name'].unique().shape[0]
print(f"Unique names: {unique_names}")

### most of the passenger have ??? siblings
sib_count = titanic_data['SibSp'].value_counts()
most_siblings = titanic_data['SibSp'].mode()
print(f"Most siblings: {most_siblings}")

### Which of the following feature plays an important role in the survival of the passengers?

# median fare
median_fare = titanic_data['Fare'].median()
print(f"Median fare: {median_fare}")