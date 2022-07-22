f = open("d/scores.csv", "r")
scores = f.readlines()[2:]

max = 0
for record in scores:
    fields = record.split(",")
    if int((fields[8])) > max:
        max = int((fields[8]))
print(max)