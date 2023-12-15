#1
s=[]
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Oman"):
            s.append(int(r[6]))
s.sort()
print(s[0])

#2
s = []
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Latvia"):
            s.append(int(r[8]))

print(sum(s))
#3
d = []
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Latvia" and r[7] == "Telecommunications"):
            d.append(int(r[8]))

print(sum(d))

#4
n=0
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Latvia" and r[3].startswith("https://")):
            n=n+1

print(n)
#5
m=0
with open("data.txt") as f:
    next(f)
    for line in f:
        r = line.rstrip().split(",")
        if(r[4] == "Latvia" and r[3].endswith(".org/")):
            m=m+1

print(m)