import pandas as pd





filename_2 = 'https://raw.githubusercontent.com/data-to-insight/ERN-sessions/main/data/ChildIdentifiers.csv'
df = pd.read_csv(filename_2)

df['PersonBirthDate'] = pd.to_datetime(df['PersonBirthDate'], format="%Y-%m-%d", errors='coerce')

df['Age'] = pd.to_datetime('today').normalize() - df['PersonBirthDate']

df['Age'] = df['Age'] / pd.Timedelta('365 Days')

df['Age'] = df['Age'].astype('int')

print(df)

max = df['Age'].max()
min = df['Age'].min()
mean = df['Age'].mean()

print(f'max: {max}, min:{min}, mean: {mean}')
under_15_condition = df['Age'] <=m15

print(df[under_15_condition])

condition = df['GenderCurrent'].isin([1, 2])

sliced_df = df
