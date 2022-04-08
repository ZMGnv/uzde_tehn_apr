# Izveidot programmu, kura prasa lietot�jam sekun�u skaitu. 
# Sekundes tiek p�rveidotas par �x hours y minutes z seconds�
#  tipa tekstu. Rezult�ts tiek par�d�ts konsol�.


# 120 sec .....0 stundas 2 min 0 sec


sec = int(input("Ievadi sekundes: "))
h=sec//(60*60)
min=(sec-(h*60*60))//60
sec2=sec-(h*60*60)-(min*60)

print(f"{sec} sekundes ir {h} stundas, {min} minūtes un {sec2} sekundes.")