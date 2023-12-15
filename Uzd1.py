s=[]
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Oman"):
            s.append(int(r[6]))
s.sort()
print(s[0])