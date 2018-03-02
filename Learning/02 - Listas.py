# Podemos contar o número de uma string especifica
# Exemplo o número de letras a na palavra avacalhar
print("------------------Contando---------------------")
avacalhar = "avacalhar"
print("Número de a's:"+str(avacalhar.count("a")))

# Adicionando um elemento a uma lista já decladara
print("------------------Adicionando---------------------\n\n")

lista = ["joão","Julberto","gilmar","joenir"]
print("Lista inicial:"+str(lista))

lista.append("Juca!")
print("Lista pós adição:"+str(lista))

# concatenando duas listas
print("\n\n------------------Concatenando---------------------\n\n")

lista0 = [1,2,3,4,5]
lista1 = [6,7,8]

# Vai inserir a lista1 no final da lista0
lista2 = lista0 + lista1
print(lista2)

print("Com strings")
lista3 = lista + lista2
print(str(lista3))

# podemos usar a função sort para ordenar uma lista
print("\n\n ------------------Sort---------------------\n\n")
lista4 = [5,4,3,2,7,8,9,9,0,22,2]
lista4.sort()
print(str(lista4))
# também podemos querer ordenar uma lista porém mantendo a lista original
# para isto usamos a função sorted
lista5 = [0,9,8,7,6,5,4,6,8,9,5,3,22,45,6,6]
lista6 = sorted(lista5)
print("\n Lista5 = {} \n lista6 = {}".format(lista5,lista6))

# Criando listas vazias(2 modos)
list_1 = []
list_2 = list()

print("\n\n ------------------Code challenge---------------------\n\n")
# Code challenge
menu = []
menu.append(["arroz","feijão","batata","spam"])
menu.append(["arroz","feijão","batata","queijo"])
menu.append(["arroz","feijão","maionese","spam"])
menu.append(["arroz","jujubas","batata","spam"])
menu.append(["milho","feijão","batata","spam"])

# achar uma lista sem spam e printar cada ingrediente

for i in menu:
	if "spam" not in i:
		for j in i:
			print(j)

print("\n\n ------------------Ponteiros/Iterators---------------------\n\n")
# Interators são como ponteiros, apontam para o local da memória em que se encontra a variável
# Exemplo

string = "juca";

ponteiro = iter(string)

# Mostra a posição de memória que se encontra
print("Posição de memória:"+str(ponteiro))

# Função para percorrer a palavra, sempre apontando para o proximo
print("Proximo:"+str(next(ponteiro)))
print("Proximo:"+str(next(ponteiro)))

print("\n\n ------------------Code challenge---------------------\n\n")

theList = ["arroz","amor",54,"kkk","nazi","sarara",76]

PontToTheList = iter(theList)

for n in range(0,len(theList)):
	print("Item {} : {}".format(n,next(PontToTheList)))

# ------------------Função range---------------------
# Usamos se quisermos criar uma sequencia
range(0,10)#0,1,2,3,4,5,6,7,8,9
range(0,10,2)#0,2,4,6,8

print("\n\n ------------------Tuplas---------------------\n\n")

tupla = "Yug","yoh",2005,"TvGlobinho"

# Posso printar todos os elementos de uma tupla
print(tupla)

# Ou posso printar individualmente, como um array
print(tupla[2])

# Em tuplas não podemos mudar um valor previamente indexado
# Exemplo: queremos mudar yoh para yohh
# tupla[1] = yohh # não podemos fazer isto
# para fazermos esta mudança temos que fazer uma semi gambiarra
# estamos recriando a tupla e não mudando seu item
tupla = tupla[0],"yohh",tupla[2],tupla[3]
print(tupla)
# E esta é uma das principais diferenças entre listas e tuplas
# Tuplas são imutaveis
lista_exemplo = ["um","dois","tres","quatro","tomates"]
lista_exemplo[2] = "três"
print(lista_exemplo)

print("\n\n ------------------Join---------------------\n\n")
# Podemos usar metodo join para juntar uma lista e uma string, acrecentado no final de toda palavra da lista esta nova string
comidas = ["arroz","feijão","batata","macarrão"]
print("Comidas lista:"+str(comidas))
print("Comidas join ',' :"+str(",".join(comidas)))
print("Comidas join '1' :"+str("1".join(comidas)))


