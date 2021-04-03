#Break function example no.1.
x1 = [27, 64, 125, 216, 343]
for z in x1:
    if z > 200:
        break
    print(z)

#Break function example no.2.
for y in range(0,26):
    if y == 25:
        break
    print(y)

#Pass function example no.1.
t = 1728
r = 1331
if t < r:
    pass
else:
    print("r is smaller than t")

#Pass function example no.2.
for w in range(1,57):
    pass

#Continue function ex. no.1.
s1 = [1331, 1728, 2197, 2744, 3375, 4096]
for i in s1:
    if i == 1728 or i == 3375:
        continue
    print(i)

#Continue function ex. no.2.
for g in range(0,1001):
    continue
print(g)
















