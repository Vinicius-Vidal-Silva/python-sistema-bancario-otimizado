#Sistema bancário otimizado
import cadastroCliente

def realizarDeposito(saldo, lista_deposito, numero_deposito):
    continuar = True
    while continuar:
        deposito = input("Por favor, entre com o valor do deposito: ")
        deposito_num = int(deposito)
        if deposito_num < 0:
            print("Valor invalido. Tente novamente!")
        elif deposito_num > 0:
            saida = True
            saldo = saldo + deposito_num
            lista_deposito.append(deposito_num)
            numero_deposito = numero_deposito + 1
            print("Deposito realizado com sucesso!")
            while saida:   
                print("Deseja realizar novo deposito?")
                novo_deposito = input("1 - SIM\n2 - NAO\nEntre com a opcao desejada: ")
                novo_deposito_num = int(novo_deposito)
                if novo_deposito_num == 1:
                    continuar = True
                    saida = False
                elif novo_deposito_num == 2:
                    continuar = False
                    saida = False
                else:
                    print("opcao invalida!")
        else:
            print("Entre com um valor numerico!")
    print(f"novo saldo: R$ {saldo}")
    return saldo, numero_deposito

def realizarSaque(saldo, LIMITE_SAQUE, lista_saque, numero_saque):
    for i in range(4):
        continuar = True
        while continuar:
            if i == LIMITE_SAQUE:
                print("Limite diario de saques atingido. Tente novamente amanha!")
                break
            saque = input("Informe a quantidade que deseja sacar: ")
            saque_num = int(saque)
            if saque_num <= 0:
                print("Valor invalido. Tente novamente!")
            elif saque_num > saldo:
                print("Saque não realizado.\nMotivo: Valor maior do que saldo disponivel.")
            elif saque_num > 500:
                print("Saque nao relizado.\nMotivo: Valor maximo ultrapassado.")
            else:
                saldo = saldo - saque_num
                lista_saque.append(saque_num)
                numero_saque = numero_saque + 1
                print("Saque realizado com sucesso!")
                continuar = False
        try:
            print("Deseja realizar novo saque?")    
            print("1 - Novo saque\n2 - Voltar ao menu inicial")
            escolha = input("Escolha a opcao desejada: ")
            escolha_num = int(escolha) #tranformando a entrada em número
            if escolha_num == 1:
                continue
            elif escolha_num == 2:
                break
            else:
                print("Opcao invalida!")
        except ValueError:
            print("Por favor insíra um número")
    print(f"Saldo atual: R$ {saldo}")
    return saldo, numero_saque

def mostrarExtrato(numero_deposito, lista_deposito, numero_saque, lista_saque, saldo):
    print("**************************************************************************\n")
    print("***********************************EXTRATO********************************\n")
    print(f"Foram realizados: {numero_deposito} deposito(s) no(s) valor(es) de:")
    for dep in lista_deposito:
        print(f"Valor do deposito: R$ {dep}")
    print("\n")
    print(f"Foram realizados: {numero_saque} saque(s) no(s) valor(es) de:")
    for saq in lista_saque:
        print(f"Valor do saque: R$ {saq}")
    print("\n")
    print(f"O saldo atual e de: R$ {saldo}\n")
    print("**************************************************************************")
    print("**************************************************************************\n")

def cadastrarCliente():
   cadastroCliente.main()

def cadastrarContaCorrente():
    pass

sair = True
saldo = 10000
lista_deposito =[]
numero_deposito = 0
LIMITE_SAQUE = 3
lista_saque = []
numero_saque = 0
print("Bem vindo ao banco Quero Tudo O Que E Seu!")
while sair:
    print("1 - Deposito\n2 - Saque\n3 - Extrato\n4 - Cadastrar Cliente\n5 - Sair")
    opcao = input("Entre com a opcao desejada: ")
    opcao_num = int(opcao)
    if opcao_num == 1:
        saldo, numero_deposito = realizarDeposito(saldo, lista_deposito, numero_deposito)
    elif opcao_num == 2:
        saldo, numero_saque = realizarSaque(saldo, LIMITE_SAQUE, lista_saque, numero_saque)
    elif opcao_num == 3:
        mostrarExtrato(numero_deposito, lista_deposito, numero_saque, lista_saque, saldo)
    elif opcao_num == 4:
        cadastrarCliente()
    elif opcao_num == 5:
        controle_saida = True
        while controle_saida:
            print("Tem certeza que deseja sair?\n1 - SIM\n2 - NAO")
            confirmacao = input("Entre com a opcao desejada: ")
            confirmacao_number = int(confirmacao)
            if confirmacao_number == 2:
                sair = True
                controle_saida = False
            elif confirmacao_number == 1:
                print("Saindo...")
                controle_saida = False
                sair = False
            else:
                print("opcao invalida!")
                controle_saida = True
    else:
        print("opcao invalida!")