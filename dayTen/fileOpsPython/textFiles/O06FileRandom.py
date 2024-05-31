
FL = open("data.txt",  "rb")

print(f"position :{FL.tell()}")

pos = FL.seek(85, 0)

print(f"position :{pos}")

FL.read(65)

print(f"position :{FL.tell()}")

pos = FL.seek(50, 1)

print(f"position :{pos}")

pos = FL.seek(200, 2)

print(f"position :{pos}")

pos = FL.seek(-300, 2)

print(f"position :{pos}")

# pos = FL.seek(-50, 0)

FL.close()