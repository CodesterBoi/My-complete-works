#Addition of an element to a set.
R4 = {27, 98.5, "Wes Collins", False}
R4.add("Harry Truman")
print(R4)

#Difference function between sets.
R4 = {27, 98.5, "Wes Collins", False}
R3 = {896, "Dr. Viktor Adler", 98.5}
print(R4.difference(R3))
print(R3.difference(R4))

#Confirmation of subset.
R5 = {896, "Dr. Viktor Adler", 98.5, 27, 98.5, "Wes Collins", False}
R3 = {896, "Dr. Viktor Adler", 98.5}
print(R3.issubset(R5))

#Confirmation of superset.
R5 = {896, "Dr. Viktor Adler", 98.5, 27, 98.5, "Wes Collins", False}
R4 = {27, 98.5, "Wes Collins", False}
print(R5.issuperset(R4))

#Pop() Function.
R5 = {896, "Dr. Viktor Adler", 98.5, 27, 98.5, "Wes Collins", False}
R5.pop()
print(R5)

#Remove() Function.
R2 = {896, "Cole Evans", 76.5, True}
R2.remove(76.5)
print(R2)

#Discard() Function.
R2 = {896, "Cole Evans", 76.5, True}
R2.discard(True)
print(R2)

#Clear() Function.
R1 = {798, "Chazz Princeton", "85x", True}
R1.clear()
print(R1)
R1.add("Eng")
print(R1)

#Disjoint() Function.
R1 = {798, "Chazz Princeton", "85x", True}
R2 = {896, "Cole Evans", 76.5, True}
print(R1.isdisjoint(R2))

#Symmetric Difference() Function
R1 = {798, "Chazz Princeton", "85x", True}
R3 = {896, "Dr. Viktor Adler", 98.5}
print(R3)

#Union() Function.
R2 = {896, "Cole Evans", 76.5, True}
R3 = {896, "Dr. Viktor Adler", 98.5}
print(R2.union(R3))

#Update() Function.
R6 = {995, True, "Bridge Carson", 78, "SPD"}
R1 = {798, "Chazz Princeton", "85x", True}
print(R1.update(R6))

#Intersection() Function.
R6 = {995, True, "Bridge Carson", 78, "SPD"}
R2 = {896, "Cole Evans", 76.5, True}
R7 = R2.intersection(R6)
print(R7)

#Copy() Function.
R6 = {995, True, "Bridge Carson", 78, "SPD"}
R8 = R6
R8.add(False)
R8.remove(True)
print("Old set is:", R6)
print("New set is:", R8)












