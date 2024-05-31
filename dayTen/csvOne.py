'''
    comma separated values 
'''

import csv
'''
with open("abc.csv", "w") as file:
    # with open("abc1.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Id", "Name", "Price"])
    writer.writerow([101, "Paint", 100])
    writer.writerow([102, "Polish", 200])
    writer.writerow([103, "Blush", 300])
'''
with open("abc.csv", "r") as file:
    reader = csv.reader(file)
    for r in reader:
        if r:
            print(r)
