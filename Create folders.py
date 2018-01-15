import os

N = input("How mush folder do you need?\n")
name = raw_input("Enter the name of folders: ")
for i in range(1, N + 1):
    os.mkdir("{0}_{1}".format(name, i))

