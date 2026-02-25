dicionario = {}
dicionario2 = {}

def adicionar_produto():
      continuar = "s"
      while continuar == "s":
            
        nomeproduto = input("Qual o nome do produto que você deseja adicionar ?(Digite 'sair' para sair): \n")
        if nomeproduto == "sair":
             break
        elif nomeproduto in dicionario:
             print("Produto já cadastrado")
             
        else:
             precoproduto = (input(f"Qual o valor do {nomeproduto} ?: "))
             quantidadeproduto = (input(f"Qual a quantidade do {nomeproduto} a ser adicionada ?: "))
             dicionario[nomeproduto] = dicionario2
             dicionario2[precoproduto] = quantidadeproduto
             continuar = input("Deseja adicionar mais itens ? (s/n): \n")
        
def remover_produto():
      continuar = "s"
      while continuar == "s":
        nomeproduto = input("Qual produto você deseja remover ? (Digite 'sair' para sair): \n")
        if nomeproduto == "sair":
             break
        elif nomeproduto in dicionario:
             del dicionario[nomeproduto]
             precoproduto = input("Digite o valor do produto para remover do sistema: ")
             if precoproduto in dicionario2:
                del dicionario2[precoproduto]
                print(f"{nomeproduto} removido.")
                continuar = input("Deseja remover mais itens ? (s/n): ")
        else:
             print(f"{nomeproduto} não existe no sistema")
        
def listar_produto():
      for chave in dicionario:
           print(f"Produto: {chave}")
      for chave, valor in dicionario2.items():
           print(f"Valor: {chave}\nQuantitade em estoque: {valor}")
      if not dicionario:
           print("Vazio.....\n")
      
def atualizar_quantidade():
      continuar = "s"
      while continuar == "s":
        nomeproduto = input("Qual produto você deseja atualizar a quantidade ? (Digite 'sair' para sair): \n")
        if nomeproduto == "sair":
             break
        elif nomeproduto in dicionario:
             quantidade = input(f"Qual o valor do item {nomeproduto} a ser alterada?: ")
             if quantidade in dicionario2:
                  novaquantidade = input(f"Digite a nova quantidade do item {nomeproduto}: ")
                  dicionario2[quantidade] = novaquantidade
                  print(f"{nomeproduto} atualizado, nova quantidade: {novaquantidade}")
                  continuar = input("Deseja atualizar mais itens ? (s/n): ")
        else:
             print("Produto não encontrado")
 
while True:
            opcao = input("Selecione uma opção: \n"
"1 - Adicionar produto \n2 - Listar produtos \n3 - Remover produtos \n4 - Atualizar a quantidade de produtos \n5 - Sair \n")

            if opcao == '1':
                adicionar_produto()

            elif opcao == '2':
                listar_produto()
        
            elif opcao == '3':
                remover_produto()
                
            elif opcao == '4':
                atualizar_quantidade()

            elif opcao == '5':
                print("\nSaindo.....")
                break
            else :
                  print("\nErro, opção invalida\n")