import csv
f=open("D:\specific\sessioncolumn.csv",'r')
content=csv.reader(f)
for x in content:
    print(x)