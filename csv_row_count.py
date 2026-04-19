import csv

# Take filename from user
filename = input("Enter CSV file name: ")

try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        
        row_count = 0
        
        for row in reader:
            row_count += 1
        
        print("Total number of rows:", row_count)

except FileNotFoundError:
    print("File not found. Please check the file name.")
except PermissionError:
    print("Permission denied to read the file.")
