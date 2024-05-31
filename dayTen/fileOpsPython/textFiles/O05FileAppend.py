
FA = open("myfile.txt", "a")

st = input("Enter the contents of the file :")
FA.write(st + "\n")

FA.close()