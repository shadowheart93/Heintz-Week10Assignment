import os

# Prompt user for directory
directory = input('Enter Directory to save file: ')

# default directory if blank
if directory == "":
    directory =  os.path.dirname(os.path.realpath(__file__))

# prompt user for filename
fileName = input('Enter filename: ')

# prompt for user info
name = input('Enter name: ')
address = input('Enter address: ')
phone = input('Enter phone number: ')

# create file
with open("{}/{}.csv".format(directory, fileName), 'w') as file:
    file.write(",".join([name, address, phone]) + "\n")

# display file
with open("{}/{}.csv".format(directory, fileName), 'r') as file:
    print("{}/{}.csv contents".format(directory, fileName))

    for line in file:
        print(line)