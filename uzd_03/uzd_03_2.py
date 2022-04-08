# Atrast cik skaitļi norādītajā intervālā dalās ar lietotāja norādīto dalītāju.

sakt=int(input("Sākuma skaitlis:"))
beigt=int(input("Beigu skaitlis:"))
dal=int(input("Dalītājs:"))

cik=0
for i in range(sakt,beigt+1):
    if i%dal==0:
        cik+=1 # cik=cik+1
print(f"Robežās starp {sakt} un {beigt} -  {cik} skaitļi dalās ar {dal}")