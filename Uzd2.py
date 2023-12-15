s = []
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Latvia"):
            s.append(int(r[8]))

print(sum(s))