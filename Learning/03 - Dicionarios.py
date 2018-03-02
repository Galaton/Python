# São como listas, porém não os acessamos pelo index
frutas = {
	"laranja" : "uma fruta da cor laranja que é citrica",
	"maça" : "uma fruta vermelha ou verde doce",
	"melancia" : "uma grande fruta verde",
	"limão" : "verde pequeno e citrico",
	"mamão" : "mamãe come"
	}

print(frutas)

print("\n---------------------------\n")
# E para acessar um item especifico
print(frutas["laranja"])

print("\n------------Adicionando---------------\n")
# Adicionando elementos a dicionarios
frutas["Nome do que quero adicionar"] = "descrição"
print(frutas)

print("\n------------Mudar valor---------------\n")
# E se quisermos mudar um valor
frutas["limão"] = "é uma dlicia"
print(frutas["limão"])

print("\n-------------Deletando Campo--------------\n")
# Deletando um campo
del frutas["Nome do que quero adicionar"]
print(frutas)

print("\n------------Deletando dicionario---------------\n")
# Deletando um dicionario
#frutas.clear()
#print(frutas)

print("\n------------Função get---------------\n")
# A função get retorna o elemento,porém com a vantagem de se o elemento não existir retornar none
print(frutas.get("limão"))
print(frutas.get("limaaaaa"))

# Também com a função get podemos assimilar um valor caso não tenhamos aquele campo
# salva = frutas.get(input("Digite uma Fruta:"),"Não temos a fruta")
# print(salva)

print("\n------------Lista com index dos dicionarios---------------\n")
# Fazer uma lista com os index do dicionario
listaFrutas = list(frutas.keys())
print(listaFrutas)

print("\n------------Função val---------------\n")
# Pega só o valor do dicionario e os retorna em uma lista
print(frutas.values())
