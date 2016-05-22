import random

loto_stevilke = []

for i in range (0,6):
  stevilka = random.randint(1,50)

  while stevilka in loto_stevilke:

    stevilka = random.randint(1,50)
  

  loto_stevilke.append(stevilka)


loto_stevilke.sort()

print("Danasnje loto stevilke so: ")
print(loto_stevilke)