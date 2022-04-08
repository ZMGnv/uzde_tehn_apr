# Izveidot programmu, kas prasa lietotājam 
# ievad�t skaitli n, tad programma apr��ina n+nn+nnn.
#  Rezult�ts tiek par�d�ts konsol�.

#  1  1+11+111   12...12+1212+121212

skaitlis= input("Ievadi skaitli:")
sum=int(skaitlis)+int(skaitlis*2)+int(skaitlis*3)
#print(sum)
print(skaitlis,"+",skaitlis*2,"+",skaitlis*3,"=",sum)