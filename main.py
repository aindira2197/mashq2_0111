#1-misol
tupl = (1, 8, 4, 1, 8, 0)

for i in tupl:
    print(f"{i} - {tupl.count(i)} ta bor")

#2-misol
tuplee = (1, 8, 6, 3, 9)
print(tuplee)

kvadrat = tuple(map(lambda a: a*a, tuplee))
print(kvadrat)

#3-misol
tup1 = (1, 8, 6, 3, 9)
tup2 = (7, 8, 4, 1, 8)
print(tup1)
print(tup2)

umumiy = list()

for i in tup1:
    if i in tup2:
        umumiy.append(i)

print(umumiy)

