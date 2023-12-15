n=0
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Latvia" and r[3].startswith("https://")):
            n=n+1

print(n)