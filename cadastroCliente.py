import datetime
import json
import cadastroConta

def cadastrar_usuario():
    usuario = {
        "nome": "",
        "data_nascimento": "",
        "cpf": "",
        "endereco": {
            "rua": "",
            "numero": "",
            "cidade": "",
            "estado": ""
        },
        "numero_conta": ""
    }

    print("Entre com os dados do cliente")

    nome = input("Nome: ")
    usuario["nome"] = nome

    # Data de nascimento
    while True:
        data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
        if verificar_data(data_nascimento):
            usuario["data_nascimento"] = data_nascimento
            break
        else:
            print("Digite uma data válida.")
    
    # CPF
    while True:
        cpf = input("CPF (Apenas números): ")
        if verificar_cpf(cpf):
            if not cpf_existe(cpf):
                usuario["cpf"] = cpf
                break
            else:
                print("CPF já cadastrado no arquivo JSON. Cadastro interrompido.")
                return None  # Interrompe o cadastro
        else:
            print("Digite um CPF válido.")

    # Endereço
    usuario["endereco"]["rua"] = input("Rua: ")

    while True:
        endereco_numero = input("Número: ")
        if verifica_num_endereco(endereco_numero):
            usuario["endereco"]["numero"] = endereco_numero
            break
        else:
            print("Digite apenas números.")
    
    usuario["endereco"]["cidade"] = input("Cidade: ")

    while True:
        endereco_estado = input("Estado (EX: SP): ")
        if verifica_estado(endereco_estado):
            usuario["endereco"]["estado"] = endereco_estado
            break
        else:
            print("Digite um estado válido.")

    numero_conta = gerar_numero_conta_sequencial()
    usuario["numero_conta"] = numero_conta

    return usuario

def verificar_data(data_nascimento):
    ### Tenta converter a data em data
    try:
      data_obj = datetime.datetime.strptime(data_nascimento, "%d/%m/%Y")
    except:
        return False
    
    ### verifica se a data é maior do que a atual
    if data_obj > datetime.datetime.now():
       return False
    
    ### extrai dia, mês e ano
    dia, mes, ano = data_obj.day, data_obj.month, data_obj.year
    if not 1 <= mes <= 12:
       return False
    
    ### Verifica se o número de dias está de acordo com o mês (considerando anos bissextos).
    if dia > 28:
        ### Último dia de casa mês
        dias_no_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ### Considera ano bissexto
        if mes == 2 and (ano % 4 == 0 or (ano % 100 == 0 and ano % 400 != 0)):
            dias_no_mes[1] = 29
        if dia > dias_no_mes[mes - 1]:
            return False
    return True

def verificar_cpf(cpf):
    if len(cpf) == 11:
        if cpf.isnumeric():
           return True
    
    return False

def verifica_num_endereco(endereco_numero):
    if endereco_numero.isnumeric():
        return True
    else:
        return False

def verifica_estado(endereco_estado):
    if len(endereco_estado) == 2:
        return True
    else:
        return False

def cpf_existe(cpf):
    try:
        with open('usuarios.json', 'r') as arquivo_json:
            lista_usuarios_json = json.load(arquivo_json)
            for usuario_json in lista_usuarios_json:
                if usuario_json == cpf:
                    return True
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return False

def gerar_numero_conta_sequencial():
    # Carregar o último número de conta do arquivo
    try:
        with open('ultimo_numero_conta.txt', 'r') as arquivo_txt:
            ultimo_numero_conta = int(arquivo_txt.read())
    except (FileNotFoundError, ValueError):
        ultimo_numero_conta = 0

    novo_numero_conta = ultimo_numero_conta + 1

    with open('ultimo_numero_conta.txt', 'w') as arquivo_txt:
        arquivo_txt.write(str(novo_numero_conta))

    return novo_numero_conta
    

def main():
    lista_usuarios = []
    try:
        with open('usuarios.json', 'r') as arquivo_json:
            lista_usuarios = json.load(arquivo_json)
    except (FileNotFoundError, json.JSONDecodeError):
        lista_usuarios = []

    while True:
        novo_usuario = cadastrar_usuario()
        cadastroConta.cadastrarConta()
        if novo_usuario:
            cadastroConta.cadastrarConta(novo_usuario)
        
        if novo_usuario:
            lista_usuarios.append(novo_usuario)
            with open('usuarios.json', 'w') as arquivo_json:
                json.dump(lista_usuarios, arquivo_json, indent=4)
            print("Usuário cadastrado com sucesso!")

        continuar = input("Deseja cadastrar outro usuário? (SIM/NAO): ")
        if continuar.upper() != "SIM":
            break

    print("\nUsuários Cadastrados:")
    print(lista_usuarios)

#if __name__ == "__main__":
#    main()
