d = []
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Latvia" and r[7] == "Telecommunications"):
            d.append(int(r[8]))

print(sum(d))