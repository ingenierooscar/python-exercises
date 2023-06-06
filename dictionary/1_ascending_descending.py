d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print(f"descending: {sorted(d.items(), key=lambda x: x[1], reverse=True)}")
print(f"ascending: {sorted(d.items(), key=lambda x: x[0])}")
print(f"hi {sorted(d.items(), key=lambda x: x[1])}")

#using sort method and lambda to start for the second value of the key 

#how to print the value of the key
print(d[1])

#how to add key and value
d["z"] = 45
print(d)

#how to check if key exist
if "z" in d:
    print("si se encuentra", d["z"])

#how to check if exist
print(d.get("lala"))

#to add if doesn't exist VALUE
print(d.get("lala", 100))
print(d)

#delete
del (d["z"])
print(d)

#add 
d["z"] = 100

#checks all keys
for valor in d:
    print(valor)

#checks values
for valor in d:
    print(d[valor])

for valor in d.items():
    print(valor)  

#key and values
for llave, valor in d.items():
    print(llave, valor)      