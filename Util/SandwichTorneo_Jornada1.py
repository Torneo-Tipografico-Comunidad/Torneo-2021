#Sándwich torneo semana 1

upper = "EHIOPT"
lower = "beilnoóqv"
nums  = ""
punct = ""

def letterSandwicher(letters, bread):
    sandwich = bread
    for letter in letters:
        sandwich += letter + bread
    return sandwich
    
print(letterSandwicher(upper,"H"))
print(letterSandwicher(upper,"O"))
print("")

for i in upper:
    print(f"HHHH{i}HHHOOO{i}OOOO")
print("")

print(letterSandwicher(lower,"n"))
print(letterSandwicher(lower,"o"))
print("")

for i in lower:
    print(f"nnnn{i}nnnooo{i}oooo")
print("")

# print(letterSandwicher(nums,"H"))
# print(letterSandwicher(nums,"O"))

# print(letterSandwicher(punct,"H"))
# print(letterSandwicher(punct,"O"))
