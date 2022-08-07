import os
listoffiles = []

dir = input("Input directory: ")
size = input("Input size(MB): ")
sizemb = size # save the mb input for future stuff
moreorless = input(f"Would you like to check if the file is more or less than {size} MB?: ")
if moreorless.lower() == "more":
    moreorless = ">"
elif moreorless.lower() == "less":
    moreorless = "<"
else:
    print("Invalid input! Defaulting to more.")
    moreorless = ">"
includeextra = input("Include extra info? This will put the size of the file next to the filename, y/n: ")
size = int(size) * 1000000 #convert from mb to bytes
files = os.listdir(dir) # creates a list of all of the files in the directory
for i in files:
    if moreorless == ">":
        if os.path.getsize(f"{dir}/{i}") > size: # check if file is more than size in mb
            if includeextra.lower() == "y":
                listoffiles.append(i + " - " + str(round((os.path.getsize(f"{dir}/{i}") / 1000000), 2)) + "MB")
            else:
                listoffiles.append(i)
    else:
        if os.path.getsize(f"{dir}/{i}") < size: # check if file is more than size in mb
            if includeextra.lower() == "y":
                listoffiles.append(i + " - " + str(round((os.path.getsize(f"{dir}/{i}") / 1000000), 2)) + "MB")
            else:
                listoffiles.append(i)
    # made two statements with essentially the same info because you can't dynamically change operators
    # str(round((os.path.getsize(f"{dir}/{i}") / 1000000), 2)) does a couple things:
    # it gets the size of the file in bytes and divides it by a million to turn it into megabytes
    # if rounds that number to two decimal places
    # it converts that number to a string

if len(listoffiles) > 25: # if there's more than 25 files in the list
    listall = input(f"There are {len(listoffiles)} files. List them all? y/n: ")
    if listall.lower() == "y":
        print(listoffiles)
else: # it doesn't matter what you put as long as it isn't y for it to do the "false" output
    print(listoffiles)

addtofile = input("Would you like to save these entries to a file? y/n: ")
if addtofile.lower() == "y":
    txtname = input("Name of the file you would like to write to? Do not include extension: ")
    with open(f"{txtname}.txt", 'w') as f: # defined as f, the file in write mode
        f.write(f"Files {moreorless} {sizemb}MB:\n\n") # adds a fancy little header describing what's being done
        for x in listoffiles:
            f.write(f"{x}\n") # loop through the files to write them line by line
    print(f"Successfully wrote {len(listoffiles)} files to {txtname}.txt!")