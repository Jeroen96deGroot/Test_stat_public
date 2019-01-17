import numpy as np
import pandas as pd

#reading csv file and storing it as a Pandas dataframe
nba = pd.read_csv('nba.csv', delimiter = ";")

df = pd.DataFrame(nba, columns=['Name', 'Age', 'Shot%', 'Salary', 'Yrs Experience', 'Height', 'Weight', 'Team', 'Year'])

#dropping unwanted observations
df = df.dropna()
df = df[(df != 0).all(1)]

# descriptive statistic for variable: Age and changing data type
youngest = df.loc[:,"Age"].min()
oldest = df.loc[:,"Age"].max()
average_age = int(df.loc[:,"Age"].mean())

# descriptive statistic for variable: Height and changing data type
shortest = int(df.loc[:,"Height"].min())
tallest = int(df.loc[:,"Height"].max())
average_lenght = int(df.loc[:,"Height"].mean())

# descriptive statistic for variable: Weight and changing data type
lightest = int(df.loc[:,"Weight"].min())
heaviest = int(df.loc[:,"Weight"].max())
average_weight = int(df.loc[:,"Weight"].mean())

#printing output below
print(df)

print('')
print("Please find descriptive statistics for the age, height, and weight of NBA players below:")
print('')

print('Age:')
print('- The youngest player is', youngest, 'years old')
print('- The oldest player is', oldest, 'years old')
print('- On average a NBA player is', average_age, 'years old')
print('')

print('Height:')
print('- The shortest player is', shortest, 'inches tall')
print('- The tallest player is', tallest), 'inches tall'
print('- On average a NBA player is', average_lenght, 'inches tall')
print('')

print('Weight:')
print('- The lightest player is', lightest, 'ounces')
print('- The heaviest player is', heaviest, 'ounces')
print('- On average a NBA player is', average_weight, 'ounces')
#untill here

#export dataframe as CSV file
export_csv = df.to_csv('nba_stats_analyzed.csv')

#correlation analysis
corr_a_s = df['Yrs Experience'].corr(df['Salary'])
corr_h_s = df['Height'].corr(df['Salary'])
corr_sp_s = df['Shot%'].corr(df['Salary'])

print('')
print("Please find a correlation analysis between characteristics of NBA players and their salary below:")
print('')
print("- The correlation between the number of years of experience and his salary is", "{0:.0%}".format(corr_a_s))
print("- The correlation between the lenght of a player and his salary is", "{0:.0%}".format(corr_h_s))
print("- The correlation between the shot accuracy of a player and his salary is", "{0:.0%}".format(corr_sp_s))
print('')
print("The shot accuracy variable has the strongest correlation with a NBA player's salary ")
