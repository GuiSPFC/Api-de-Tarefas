sair = 's'

while sair == 's':
    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Por favor digite um número")

    soma = lambda n1,n2 : n1 + n2
    subtracao = lambda n1,n2 : n1 - n2
    multiplicacao = lambda n1,n2 : n1* n2
    divisao = lambda n1,n2 : n1 / n2

    opcao = (input("Selecione uma opção: \n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n"))

    if opcao == '1':
            print(soma(n1,n2))
            sair = input("\n""Deseja fazer outra operação? (S/N): ")
    elif opcao == '2': 
            print(subtracao(n1,n2))
            sair = input("\n""Deseja fazer outra operação? (S/N): ")
    elif opcao == '3':
            print(multiplicacao(n1,n2))
            sair = input("\n""Deseja fazer outra operação? (S/N): ")
    elif opcao == '4':
            if n2 == 0:
                print("Não é possível dividir por zero")
                n2 = float(input("Escolha outro número: "))
                print(divisao(n1,n2))
                sair = input("\n""Deseja fazer outra operação? (S/N): ")
            else:
                print(divisao(n1,n2))
                sair = input("\n""Deseja fazer outra operação? (S/N): ")
    else:
         print("Opção invalida")

  