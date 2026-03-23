# 1. Writing to a file (this will create a new file or overwrite existing content)
file = open("File_handling.txt","w")
file.write("Hello, this is the first line.\n")
file.write("File handling in Python is easy.\n")
file.close()  # Closing the file

# 2. Reading from the file
file = open("File_handling.txt", "r")
content = file.read()
print("Reading file content:")
print(content)
file.close()

# 3. Appending to the file (adds content without deleting existing data)
file = open("File_handling.txt", "a")
file.write("This line is added later using append mode.\n")
file.close()