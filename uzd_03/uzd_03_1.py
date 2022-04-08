# Apgriezt pozitīva skaitļa ciparu secību.
#  Piemērs: 12345 => 54321

skaitlis=input("Ievadi pozitīvu skaitli:")

try:
    sk=int(skaitlis)
    if sk>0:
        for i in range(len(skaitlis)-1,-1, -1):
            print(skaitlis[i], end="")
    else:
        print("Nav ievad;its pozitīvs skaitlis!")
except ValueError:
    print("Nav ievadīts skaitlis")
