L = ["Leuleu", 25, 1998]
L.extend(["Bruxelles", "python learner"])
L[1] = 26

L.append(["this will be deleted"])

del(L[5])

print(L)