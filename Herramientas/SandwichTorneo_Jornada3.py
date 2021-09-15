#Sándwich torneo semana 3

#*** CONFIG *****************

upper = "BCDEFGHILNOPQTUV"
lower = "abcdefghilmnoopqrvw"
nums  = "0123456789"
punct = ".:,!¡?¿)[)]"

#*** FUNCIONES *************

def letterSandwicher(letters, bread):
    sandwich = bread
    for letter in letters:
        sandwich += letter + bread
    return sandwich
    
#*************#*************

#***Mayúsculas***
print(letterSandwicher(upper,"H"))
print(letterSandwicher(upper,"O"))
print("")

for i in upper:
    print(f"HHH{i}HHOO{i}OOO")
print("")

#***Minúsculas***
print(letterSandwicher(lower,"n"))
print(letterSandwicher(lower,"o"))
print("")

print("""nnnnnnnnnnnnnnnnnnnnn
nunununununununununun
niuiniuiniuiniuiniuin
bqbqbqbqbqbqbqbqbqbqbq
bdpqbdpqbdpqbdpqbdpqbdpq
niupdniubqniupdniubqniupd
uinpduinbquinpduinbquinpd
uonipodiuoniboqiuonipodiu
nouiqobinouiqobinouiqobin
nnnnnoonoo nnonnooooo""")
print("")

for i in lower:
    print(f"nnn{i}nnoo{i}ooo")
print("")

#***Números***
print(letterSandwicher(nums,"0"))
print(letterSandwicher(nums,"1"))
print("")


#>>>Escojan el/los que más les convenga:
#Si van a usar varios, hagan otro loop para que no se repitan intercalados
for i in nums:
#    print(f"nnnn{i}nnnooo{i}oooo")
    print(f"HHH{i}HHOO{i}OOO")
#    print(f"1111{i}111000{i}0000")
print("")

#***Puntuación***
print(letterSandwicher(punct,"n"))
print(letterSandwicher(punct,"o"))
print(letterSandwicher(punct,"H"))
print(letterSandwicher(punct,"O"))