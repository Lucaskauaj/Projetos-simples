class ContaBancaria:
    def __init__(self, nome, saldo, cpf, senha,):
        self.nome = nome
        self.saldo = saldo
        self.cpf = cpf
        self.senha = senha


    def atualizar_saldo(self, valor):
        self.saldo += valor

    def excluir_conta(self):
        self.nome = None
        self.saldo = None
        self.cpf = None
        self.senha = None




contas = {}


while True:
    print("Selecione uma opção:")
    print("1 - Criar conta")
    print("2 - Atualizar conta")
    print("3 - Excluir conta")
    print("4 - Ver conta")
    print("5 - Ajuda na criação da conta")
    print("0 - Sair")


    escolha = input("Digite o número da opção desejada: ")


    if escolha == "1":
        while True:
            nome = input("Digite o nome do titular da conta: ")


            if any(char.isdigit() for char in nome):
                print("Nome inválido. O nome não pode conter números.")
                continue


            cpf = input("Digite o CPF do titular da conta (apenas números): ")
            senha = input("Digite a senha da conta: ")
            

            saldo_valido = False
            while not saldo_valido:
                saldo_str = input("Digite o saldo inicial da conta: ")
                if not saldo_str.isdigit():
                    print("Saldo inválido. O saldo deve ser um número.")
                else:
                    saldo = float(saldo_str)
                    saldo_valido = True


            if nome in contas:
                print("Já existe uma conta com o nome informado!")
            elif len(cpf) != 11:
                print("CPF inválido. O CPF deve conter exatamente 11 números.")
            elif len(senha) < 10:
                print("A senha deve conter pelo menos 10 caracteres.")
            else:
                conta = ContaBancaria(nome, saldo, cpf, senha)
                contas[nome] = conta
                print("Conta criada com sucesso!")
                break


    elif escolha == "2":
        nome = input("Digite o nome do titular da conta para atualizar o saldo: ")
        senha = input("Digite a senha da conta: ")


        if nome in contas:
            conta = contas[nome]


            if conta.senha == senha:
                valor = float(input("Digite o valor a ser adicionado ao saldo: "))
                conta.atualizar_saldo(valor)
                print("Saldo atualizado com sucesso!")
            else:
                print("Senha incorreta. Acesso negado!")
        
        
        
        
        
        
        else:
            print("Conta não encontrada!")


    elif escolha == "3":
        nome = input("Digite o nome do titular da conta para excluí-la: ")
        senha = input("Digite a senha da conta: ")


        if nome in contas:
            conta = contas[nome]


            if conta.senha == senha:
                del contas[nome]
                print("Conta excluída com sucesso!")
            else:
                print("Senha incorreta. Acesso negado!")
        else:
            print("Conta não encontrada!")


    elif escolha == "4":
        nome = input("Digite o nome do titular da conta para ver os detalhes: ")
        senha = input("Digite a senha da conta: ")


        if nome in contas:
            conta = contas[nome]


            if conta.senha == senha:
                print(f"Titular da conta: {conta.nome}")
                print(f"CPF do titular: {conta.cpf}")
                print(f"Saldo da conta: {conta.saldo}")
            else:
                print("Senha incorreta. Acesso negado!")
        else:
            print("Conta não encontrada!")

    elif escolha =="5":
          
      print("Para criar uma conta primeiro você deve inserir o nome do titular da conta,depois seu cpf(Cadastro de Pessoas Físicas),logo em seguida crie uma senha com no minimo 10 digitos e logo em seguida um valor a ser botado na conta,desde ja agradeço sua compreensão")
                
                  

          
    elif escolha == "0":
        print("Encerrando o programa")
        break

