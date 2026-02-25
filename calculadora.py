print("Escolha a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

sair = "S"

while sair == "S":

 opcao = input("Digite o número da operação desejada: ")
 num1 = float(input("Digite o primeiro número: "))
 num2 = float(input("Digite o segundo número: "))

 if opcao == "1":
    print("Resultado:", num1 + num2)
    sair = input("Deseja fazer outra operação?(S/N): ")

 if opcao == "2":
    print("Resultado: ", num1-num2)
    sair = input("Deseja fazer outra operação?(S/N): ")

 if opcao == "3":
   print("Resultado: ",num1*num2)
   sair = input("Deseja fazer outra operação?(S/N): ")

 if opcao == "4":
    if num2==0:
     print("Erro")
     sair = input("Deseja fazer outra operação?(S/N): ")
    else:
       print ("Resultado: ",num1/num2)
       sair = input("Deseja fazer outra operação?(S/N): ")
 else:
   print("Opção invalida!")
   sair = input("Deseja fazer outra operação?(S/N): ")
   
print ("Obrigado, até logo")