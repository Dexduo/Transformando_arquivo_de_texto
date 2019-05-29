#esse programa serve para remover os "\n" dos nomes do arquivo de texto após transformá-los em lista
banco_de_nomes = open("teste.txt", "w")
for i in range(0, 4):
	nome = input("escreva um nome: ")
	banco_de_nomes.write(nome+"\n")
banco_de_nomes.close()



l = []
aux = []
banco_de_nomes = open("teste.txt", "r")
for line in banco_de_nomes:
	l = l+[line]

for i in range(0, len(l)):
 	for j in range(0, len(l[i])-1):
  		aux+=l[i][j]

final = [""]*len(l)

cont = 0
cont_anterior = 0

for i in range(0, len(l)):
	cont += len(l[i])-1
	for j in range(cont_anterior, cont):
		final[i] += aux[j]
	cont_anterior += len(l[i])-1



print(final)
print(aux)
print(l)
