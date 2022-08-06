import os

dir = input("Input directory: ")
size = input("Input size(MB): ")
moreorless = input(f"Would you like to check if the file is more or less than {size} MB?: ")
if moreorless.lower() == "more":
    moreorless = ">"
elif moreorless.lower() == "less":
    moreorless = "<"
else:
    print("Invalid input! Defaulting to more.")
    moreorless = ">"
size = int(size) * 1000000
files = os.listdir(dir)
for i in files:
    if moreorless == ">":
        if os.path.getsize(f"{dir}/{i}") > size: # check if file is more than size in mb
            print(i + " - " + str(round((os.path.getsize(f"{dir}/{i}") / 1000000), 2)) + "MB")
    else:
        if os.path.getsize(f"{dir}/{i}") < size: # check if file is more than size in mb
            print(i + " - " + str(round((os.path.getsize(f"{dir}/{i}") / 1000000), 2)) + "MB")