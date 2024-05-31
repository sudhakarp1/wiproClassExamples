
"""
if the mode is read then we can only read the contents of the fie. by default the mode is read mode
"""
FL = open("data.txt", "r")

# st = FL.read(500)
# print(st)

# st = FL.readline()
# print(st)

st = FL.readlines(900)
print(st)

# for line in st:
#     print(line)

FL.close()

