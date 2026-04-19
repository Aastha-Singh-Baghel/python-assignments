# Take filename from user
filename = input("Enter CSV file name: ")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
        print("Total number of rows:", len(lines))

except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
