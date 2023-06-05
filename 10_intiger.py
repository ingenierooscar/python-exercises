n = input()
b = n + (n+n) + (n+n+n)
c = list(b)
print(f"{int(c[0])+int(c[1]+c[2])+int(c[3]+c[4]+c[5])}")
