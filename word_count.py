def word_count(happy):

	happy = input("Escribe algo para contar el número de palabras: ")

	words = happy.split()

	counts = {}
	for word in words:
	    counts[word] = counts.get(word, 0) + 1
	print("La cantidad de palabras de lo que escribió el usuario es: ")
	print(counts)
def main():
	return word_count(happy)

main()
