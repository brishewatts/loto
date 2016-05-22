import random
# ustvari seznam kjer se shranjujejo stevilke
loto_stevilke = []

for i in range (0,6):
  stevilka = random.randint(1,50)
# preveri ce izbrana stevilka ze obstaja
  while stevilka in loto_stevilke:
# in ce obstaja izberi drugo stevilko
    stevilka = random.randint(1,50)
  
# enkrat ko imamo stevilko katero se ne ponavlja jo dodaj v seznam
  loto_stevilke.append(stevilka)

# pa se sortiraj jih od manjse proti vecji...
loto_stevilke.sort()
# izpisi stevilke
print("Danasnje loto stevilke so: ")
print(loto_stevilke)