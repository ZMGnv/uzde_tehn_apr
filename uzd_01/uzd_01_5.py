# Zemniekam ir govis, c�kas un vistas. Gov�m un c�k�m ir 
# pa 4 k�j�m, vist�m � 2. 
# Izveidot programmu, kas prasa lietot�jam ievad�t c�ku, 
# govju un vistu skaitu. 
# Tiek apr��in�ts kop�jais k�ju daudzums. 
# Rezult�ts tiek izvad�ts konsol�.

pigs = int(input("Amount of pigs: "))
cows = int(input("Amount of cows: "))
chicks = int(input("Amount of chickens: "))
print("Amount of legs: ", pigs*4 + cows*4 + chicks*2)