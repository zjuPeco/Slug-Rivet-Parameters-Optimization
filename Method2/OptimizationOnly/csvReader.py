import csv
import os
import json

os.chdir('D:\MasterMe\python\code\Regression and optimization for Slug Rivet\Squeezing Force 38000N')

x = []
y = []
d = {}
# with open('collectedData.csv', 'rb') as f:
with open('collectedData.csv', 'r') as f:
    reader = csv.reader(f)
    # reader.next()
    reader.__next__()
    for row in reader:
        x.append([float(val) for val in row[1:-1]])
        y.append(float(row[-1]))
        item = "-".join(row[1:-1])
        if item not in d:
            d[item] = float(row[-1])

with open('test2.json', 'w') as f:
    json.dump(d, f)
            