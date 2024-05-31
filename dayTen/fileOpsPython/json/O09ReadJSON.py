
import json

JFR = open("books.json", "r")
jsonFile = json.load((JFR))

for book in jsonFile['books']:
    print(book['name'])
    print("-" * len(book['name']))
    for k, v in book.items():
        print(k, "=>", v)
    print("*" * 60)

