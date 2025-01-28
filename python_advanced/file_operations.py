createFile = open("files\\attention.txt", "w")

createFile.write("In the Write method, all data is overwritten, attention should be paid!")

createFile.close()


fileToAppend = open("files\\students.txt", "r")
#fileToAppend.write("Ross \n")
#fileToAppend.write("Monica \n")
#fileToAppend.write("Rachel \n")

for file in fileToAppend:
    print(file)

fileToAppend.close()


#%%
import os

if os.path.exists("files\\attention.txt"):
    os.remove("files\\attention.txt")
else:
    print("There is no file.")