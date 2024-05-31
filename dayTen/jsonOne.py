import json
from pathlib import Path 

'''
Items = [
        {"Id":101, "Name":"Paint", "Price":100},
        {"Id":102, "Name":"Polish", "Price":200},
        {"Id":103, "Name":"Blush", "Price":300}
]

jsonData = json.dumps(Items)
print(jsonData)

Path('Items.json').write_text(jsonData)
'''

jsonData = Path('Items.json').read_text()
items = json.loads(jsonData)

for i in items:
    for j,k in i.items():
        print(f'j: {j}\t\tk: {k}')


