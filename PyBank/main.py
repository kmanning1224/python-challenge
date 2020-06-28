import os
import csv


date = []
prof_loss = []
average = []
greatest = []
least = []

budget_csv_path = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

with open(budget_csv_path, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    next(csvreader)
    
    month = 0
    for row in csvreader:
        date.append(row[0])
        prof_loss.append(row[1])
        month += 1

greatest = prof_loss[0]
least = prof_loss[0]
totalprof = 0

for _ in prof_loss:
    totalprof += int(_)

for i in range(len(prof_loss)):
    if prof_loss[i] >= greatest:
        greatest = prof_loss[i]
        greatestd = date[i]
    elif prof_loss[i] <= least:
        least = prof_loss[i]
        leastd = date[i]

average = round(totalprof / month, 2)

print("Total Months= " + str(month))
print("Total Profit/Loss= " + str(totalprof))
print("Average Change= " + str(average))
print("Greastest Increase= " + str(greatestd) +'$' + str(greatest))
print("Biggest Decrease= " + str(leastd) +'$' + str(least))

print("Total Months= " + str(month), file=open('../PyBank/Summary.txt', 'w'))
print("Total Profit/Loss= " + str(totalprof), file=open('../PyBank/Summary.txt', 'a'))
print("Average Change= " + str(average), file=open('../PyBank/Summary.txt', 'a'))
print("Greastest Increase= " + str(greatestd) +'$' + str(greatest), file=open('../PyBank/Summary.txt', 'a'))
print("Biggest Decrease= " + str(leastd) +'$' + str(least), file=open('../PyBank/Summary.txt', 'a'))


