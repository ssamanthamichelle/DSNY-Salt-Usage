
#Samantha Michelle Garcia

about = "Cleaning the dataset before creating tables using PostgreSQL"

print(about)

#noticed that the original dataset doesn't have an index and there isn't really a key for each record
#so in postgres i'll just create a surrogate key in postgres


import pandas as pd

file = "DSNY_Salt_Usage.csv"
df = pd.read_csv(file)


#Change the column names so that they are all lowercase with no spaces

df.columns = ['stormnumber', 'date', 'manhattan', 'bronx', 'brooklyn', 'queens', 'statenisland', 'totaltons']

#all of the times in the 'date' column are 12am, so probably not important to keep
#make date just mm/dd/yyyy

df['date'] = df['date'].apply(lambda x: str(x).split(" ")[0])

#create new csv
df.to_csv("DSNY_Salt_CLEAN.csv", encoding='utf-8', index=False)

print("New file successfully created: 'DSNY_Salt_CLEAN.csv'")

