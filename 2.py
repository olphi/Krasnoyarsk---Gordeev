import csv

ans = []
ships = input().split(', ')
with open('sailors.csv', encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    for index, row in enumerate(reader):
        if index > 0:
            if 40 <= int(row[3]) <= 60:
                if row[-1] in ships or row[2] == 'pirate':
                    ans.append(row[1])
ans.sort()
for i in ans:
    print(i)