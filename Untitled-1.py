#n1, n2, n3 = map(int, input("Digite os numeros: ").split())

#array = [n1, n2, n3]

#arrey = array
#arrey.sort()

#print(arrey[1])

#################################################################

#numero = int(input("Digite um numero: "))

#soma = 0

#for i in range(1, numero + 1):
    #soma += i

#print(soma)

#nome = input("Nome: ")

#[::-1 inverte a palavra]
#print(nome[::-1])

#################################################################

#array = []
#for i in range(1,6):
    #palavra = (input("Digita palavra: "))
    #array.append(palavra)

#sort organiza em ordem alfabetica
#array.sort()

#print(array)

##################################################################

#numero = int(input("Digite: "))

#transforma um numero inteiro em uma string, converte
#string = str(numero)

#if string == string [::-1]:
    #print("é um palindromo")
#else:
    #print("nao é um palindromo")

#################################################################

#array = {"12","345","2","6","5213"}
#contador = 0

#len pega o tamanho do digito de uma informacao
#for i in array:
    #if len(i) % 2 == 0:
       #contador += 1

#print(contador)

#################################################################

#array = [1,2,3,3,2,4,5,5]

#dicionario = {}

#for i in array:
    #if i not in dicionario:
        #dicionario[i] = 1
    #else:
        #dicionario[i] +=1

#soma = 0

#for chave, valor in dicionario.items():
    #if valor == 1:
        #soma += chave

#print(chave)

#################################################################

#array = [1,1,2,2,3,3,4,4,5,5,6]
#dicionario = {}

#for i in array:
   # if i not in dicionario:
    #    dicionario[i] = 1
   # else:
     #   dicionario[i] +=1

#for chave, valor in dicionario.items():
   # if valor == 1:
       # print(chave)

#################################################################

#array = [22,33,4,5,312,22,55,11,22,55,88,98]

#array.sort()

#n1 = array[0]
#n2 = array[-1]

#print(n1+n2)

#################################################################

#array = [1,1,2,3,4,5,5,5,6,6,7,7,7,7,7,1,2,4]

#dicionario = {}

#for i in array:
    #if i not in dicionario:
        #dicionario[i] = 1
    #else:
       # dicionario[i] += 1

#chave e valor faz um loop no dicionario
#for chave, valor in dicionario.items():
   # if chave == valor:
    #    print(chave)

#################################################################

#class pokemon:
    #def __init__(self, nome, altura, peso, hp, ataque, tipo):
       # self.nome = nome
       # self.altura = altura
       # self.peso = peso
       # self. hp = hp
       # self.ataque = ataque
       # self.tipo = tipo

   # def mostrarnome(self):
      #  print(f"O nome é: {self.nome}")

    #def mostraraltura(self):
      #  print(f"A altura é {self.altura}")

#pica = pokemon("Pica", 50, 15, 400, "Raio", "choque")
#dragao = pokemon("dragao", 500, 105, 4000, "ovo", "ovo2")

#pica.mostrarnome()
#dragao.mostrarnome()

###############################################################

#class Animal:
    #def __init__(self, nome):
        #self.nome = nome

    #def comer(self):
        #
#class Cachorro(Animal):
    #def latir(self):
        #print(f"{self.nome} está latindo")

#dog = Cachorro("Douglas")

#dog.comer()
#dog.latir()

###############################################################

#def funcition():
    #yield 1

##contador = funcition()

#print(next(contador))

###############################################################

#except ValueError:
#except ZeroDivisionError:

###############################################################

