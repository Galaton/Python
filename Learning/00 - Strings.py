print('Hello world!')

# não precisa declarar variaveis para usa-las
# pode se usar tanto '' como "" para strings
objeto1 = "Juca"
objeto2 = 'Manduca'
print(objeto1 + " "+ objeto2)

#Comando para pegar o que o usuario digita é o input
#podemos digitar uma menssagem para aparecer antes dele

digitado = input("digita:")

print("O que tu digitou foi:" + digitado)

#----------------------------------------------
# Strings funcionam de forma semelhante a c
string = "feliz"
print(string[1])
# Vai printar e

# Porém temos alguns truques
# Podemos escolher a posição da letra de traz para frente
# no exemplo -1 seria "z" e -2 seria "i"

print(string[-1])

# Também podemos definir um range da string
# Aqui queremos da posição 2 a 3
print(string[2:4])

# ----------------------------------------
# Convertendo variáveis para strings

idade = 20

print("\n\n Minha idade é:" + str(idade) + " anos!")

# outro meio de fazer isto com muitos parametros é

print("\n\n Minha idade é {0} anos e tenho {1} irmã e {2} tios legal né !".format(20,1,5))

# Podemos fazer como em c

print("\n\n Tenho %d anos meu nome é %s e meus pais %s são !!" %(idade,"Gabriel","Angelo e Eda"))

