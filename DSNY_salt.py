
#Samantha Michelle Garcia

about = """DSNY Salt Usage
This dataset aims to record the amount of salt used by each borough on a given day during or after a storm from 2016-2018.
The storms are identified by the order in which they occur in each year.
Each record has a date, which, at first glance, appears to be unique and increasing, and a timestamp which seems to only be 12am.
The DSNY notes that the data is based on the number of times that a piece of salt-spreading equipment reloads.
The capacity of a piece of salt-spreading equipment is 16 tons.
So the numbers in the data set are the number of times reloaded multiplied by 16 tons."""

print(about)

print("\n"*2)

import numpy as np
import matplotlib.pyplot as plt

file_name = "DSNY_Salt_Usage.csv"

try:
	my_file = open(file_name, "r")

except:
	print("File not found")

else: #print first five lines
	print("First five records")
	print(my_file.readline())
	print(my_file.readline())
	print(my_file.readline())
	print(my_file.readline())
	print(my_file.readline())

	my_file.close()

print("\n"*2)

print(""" The fields of this dataset are "DSNY Storm #" "Date of Report" "Manhattan" "Bronx" "Brooklyn" "Queens" "Staten Island" "Total Tons"
The first column is a string, the second column should be a datetime object, and the other six columns should be numeric, but are actually strings.
Each record is a day of a storm/weather condition.
""")

print("Some questions I want to answer:")
print("- On averge, which borough uses the greatest amount of salt?")
print("- On average, which borough uses the least amount of salt?")
print("- Is it consistently the same borough that uses the greatest/least amount of salt?")
print("- What percentage of the total amount of salt used does each individual borough use?")

print("\n"*2)


f = open("DSNY_Salt_Usage.csv", "r")
h = f.readline()

print("Original Header")
print(h)
#print(type(h))

header = h.split(",")
header = [header[i].strip() for i in range(len(header))]

#renaming headers bc spaces make indexing difficult
for i in range(len(header)):
    h_split = header[i].split(" ")
    if len(h_split) > 1:
        new_h = h_split[0] + h_split[1]
        header[i] = new_h

print("\n")

print("Updated Header")
print(header)

print("\n"*2)


all = np.genfromtxt("DSNY_Salt_Usage.csv", delimiter=",", skip_header=1, names=header, dtype=None) #, encoding='UTF-8')

all = np.reshape(all, (106, 1))

max_total = all["TotalTons"].max()
min_total = all["TotalTons"].min()
mean_total = all["TotalTons"].mean()

print("Maximum amount of salt used in NYC in tons: " + str(max_total))
print("Minimum amount of salt used in NYC in tons: " + str(min_total))
print("Mean amount of salt used in NYC in tons: " + str(mean_total))

print("\n"*2)

max_manhattan = all["Manhattan"].max()
min_manhattan = all["Manhattan"].min()
mean_manhattan = all["Manhattan"].mean()


print("Maximum amount of salt used in Manhattan in tons: " + str(max_manhattan))
print("Minimum amount of salt used in Manhattan in tons: " + str(min_manhattan))
print("Mean amount of salt used in Manhattan in tons: "+ str(mean_manhattan))

print("\n"*2)

print("Descriptive Statistics")

print("\n")

var_total = all["TotalTons"].var()
std_total = all["TotalTons"].std()

var_manhattan = all["Manhattan"].var()
std_manhattan = all["Manhattan"].std()


print("NYC Variance \t\t\t\t" + str(var_total))
print("NYC Standard Deviation \t\t\t" + str(std_total))

print("\n"*2)

print("Manhattan Variance \t\t\t" + str(var_manhattan))
print("Manhattan Standard Deviation \t\t" + str(std_manhattan))

#interquartile range for manhattan
m_25 = np.percentile(all["Manhattan"], 25)
m_75 = np.percentile(all["Manhattan"], 75)
m_iqr = m_75 - m_25

#interquartile range for nyc
t_25 = np.percentile(all["TotalTons"], 25)
t_75 = np.percentile(all["TotalTons"], 75)
t_iqr = t_75 - t_25

print("\n"*2)

print("Interquartile Range NYC \t\t " + str(t_iqr))
print("Interquartile Range Manhattan \t\t " + str(m_iqr))

mean_si = all["StatenIsland"].mean()
mean_bk = all["Brooklyn"].mean()
mean_bx = all["Bronx"].mean()
mean_q = all["Queens"].mean()
#mean_manhattan
#mean_total

print("\n"*2)

print("Staten Island Mean \t" + str(mean_si))
print("Brooklyn Mean \t\t" + str(mean_bk))
print("Bronx Mean \t\t" + str(mean_bx))
print("Queens Mean \t\t" + str(mean_q))

print("\n"*2)


print("Bar Chart")

plt.title("Amount of Salt Used by Borough")
labels = ["Manhattan", "Bronx", "Brooklyn", "Queens", "Staten Island"]
amt = [mean_manhattan, mean_bx, mean_bk, mean_q, mean_si]
y = np.arange(len(labels))
plt.xticks(y, labels)
plt.ylabel("Tons of Salt")
plt.bar(y, amt)

plt.show()

print("\n"*2)

print("Pie Charts which represent the percentage of the total salt each borough uses")

#Manhattan
plt.subplot()
label = ["Manhattan", "NYC"]
amounts = [mean_manhattan, mean_total]
explode = (0.1, 0.0)
colors = ["lightblue", "darkblue"]
plt.pie(amounts, explode, labels=label, colors=colors)
plt.show()

#Bronx
plt.subplot()
label = ["Bronx", "NYC"]
amounts = [mean_bx, mean_total]
explode = (0.1, 0.0)
colors = ["darkgreen", "darkblue"]
plt.pie(amounts, explode, labels=label, colors=colors)
plt.show()

#Brooklyn
plt.subplot()
label = ["Brooklyn", "NYC"]
amounts = [mean_manhattan, mean_total]
explode = (0.1, 0.0)
colors = ["lightgreen", "darkblue"]
plt.pie(amounts, explode, labels=label, colors=colors)
plt.show()

#Queens
plt.subplot()
label = ["Queens", "NYC"]
amounts = [mean_q, mean_total]
explode = (0.1, 0.0)
colors = ["darkred", "darkblue"]
plt.pie(amounts, explode, labels=label, colors=colors)
plt.show()

#Staten Island
plt.subplot()
label = ["Staten Island", "NYC"]
amounts = [mean_si, mean_total]
explode = (0.1, 0.0)
colors = ["pink", "darkblue"]
plt.pie(amounts, explode, labels=label, colors=colors)
plt.show()

print("\n"*2)

print("""On average, Queens uses the most salt during storms. \nI think this makes sense because Queens is the largest borough. \nManhattan uses the least amount of salt, on average. \nManhattan is the smallest borough so this also makes sense.""")

print("\n"*2)

