
"""
if the file is opened for writing and if the file does not exist then creates a new file and adds the content.  if the file already exists with the same name then deletes the content of the file and writes newly into the file
"""
FW = open("myfile.txt",  "w")

# st = input("Enter the contents of the file :")

# FW.write(st)

l1 = "This is the first line.\n"
l2 = "This is the second line.\n"
l3 = "This is the third line.\n"
FW.writelines([l1, l2, l3])

FW.close()


