m=0
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Latvia" and r[3].endswith(".org/")):
            m=m+1

print(m)