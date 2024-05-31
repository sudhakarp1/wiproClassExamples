
import csv
from prettytable import PrettyTable

with open("Employee.csv", "r") as CSVR:
    emp_details = csv.reader(CSVR)
    # colnames = next(emp_details)
    # print(colnames)

    empTbl = PrettyTable(next(emp_details))

    for row in emp_details:
        # print(*row)
        empTbl.add_row(row)

print(empTbl)


