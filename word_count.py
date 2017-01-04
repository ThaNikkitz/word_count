happy = input("Escribe algo aquí para contar el número de palabras: ")

words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
print("La cantidad de palabras del input es: ")
print(counts)
