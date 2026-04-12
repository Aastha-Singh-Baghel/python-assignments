import csv

file = open("student.csv", "r")

reader = csv.reader(file)

count = 0

for row in reader:
    count = count + 1

print(count)

file.close()