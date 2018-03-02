# Assinalando multiplas variáveias a o mesmo valor
a = b = c = d = 10
print(a,b,c)

# Assinalando multiplos valoser a multiplas variáveis
e,f,g = 12,13,14
print(e,f,g)

# Python não usa {} para delimitar blocos de código
# ele usa a identação para fazer isto

#Exemplo de if
# O primeiro passo é pegar um int em vez de string
numero = int(input("Digite um número:"))

if (numero > 100) :
	print("Número maior que 100")

elif numero == 100:
		print("Seu número é 100")

else :
		print ("Número menor que 100")

# Exemplo 2 if

if numero == 69:
	numero2 = int(input("Digite um número:"))
	if (numero2  > 12) and ((numero2 == 24) or (numero2 == 69)):
		print("Oi?")
	else :
		print("What??")

# podemos usar not(alguma coisa) também
print("==============For Exemplo 0===================")
# ---------------------------------------------------------------
# for diferentão
# for variavel in range(primeiro valor que a variavel vai assumir, ultimo valor -1 , (de quanto em quanto você quer incrementar(default = 1)))

for i in range(40,48,2):
	print(i)

print("===============Exponencial==================")
# Exponencial é **
print(3**2)

print("===============For Exemplo 1: continue==================")
# continue
# este comando faz parar o processamento no bloco em que ele se encontra e seguir para o proximo valor do bloco
# Exemplo

carro = ["Roda","volante","banco","capo","vidro","escapamento"]
girl = ["Olho","Mão","Boca","Cabelo","escapamento"]

for char in carro:
	# Com isto excluimos roda do rolê
	if "Roda" in char:
		continue

	print("Componente:" + str(char))

print("================For Exemplo 2:continue=================")
# Exemplo 2
# Só termina no 1 bloco mais dentro
for thot in girl:
	print("Look that:"+thot)

	for char in carro:
		# Com isto excluimos roda do rolê
		if "Roda" in char:
			continue

		print("Ela é {} na {}".format(thot,char))

print("===============Break==================")
# Break
# funciona igual no c
# sai do bloco em que ele esta
for thot in girl:
	print("Look that:"+thot)

	for char in carro:
		# Quando chega em capo para e vai para a proxima parte de girl
		if "capo" in char:
			break

		print("Ela é {} na {}".format(thot,char))

print("===============Operações Basicas==================")
x = 10
# x = x + 10
x += 10
print("x += 10 Result: " + str(x))
# x = x * 4
x *= 4
print("x *= 4 Result: " + str(x))
# x = x / 2
x /= 2
print("x /= 2 Result: " + str(x))
# x = (x ** 2) == (x ^ 2)
x **=2
print("x **=2 Result: " + str(x))

print("===============while==================")
# Quase igual a c
while(x > 1000):
	x -= 100
	print(x)

# outro exemplo com strings
# enquanto não se digitar uma peça de carro vai ficar no loop
inputt = ""
while inputt not in carro:
	inputt = input("Digite uma peça de carro:")


print("===============Else diferentão==================")
# este else vale tanto para o while como para o for
# ele funciona assim
# se entrar em um break não cai nele
# se terminar normal vai cair nele

inputt = ""
while inputt not in carro:
	inputt = input("Digite uma peça de carro:")
	if inputt == "sair":
		break
else:
	print("Boa Op!")