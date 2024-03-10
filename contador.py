comment = "Hoy es un dia hermoso para caminar con amigos"

counter = 0

vowels = ['a', 'e', 'i', 'o', 'u']

for a in comment:
    if a in vowels:
        counter += 1

print(counter)