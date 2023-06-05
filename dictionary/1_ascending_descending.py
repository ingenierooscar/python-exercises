d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print(f"descending: {sorted(d.items(), key=lambda x: x[1], reverse=True)}")
print(f"ascending: {sorted(d.items(), key=lambda x: x[0])}")
print(f"hi {sorted(d.items(), key=lambda x: x[1])}")

#using sort method and lambda to start for the second value of the key 
