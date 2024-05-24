import json
import cadastroCliente

def cadastrarConta():
    conta_corrente = {
        "agencia": "0001",
        "numero_conta": cadastroCliente.cadastrar_usuario().usuario["numero_conta"] ,
        "usuario": cadastroCliente.usuario["numero_conta"]  # Vincular conta ao usuário
    }
    
    cadastroCliente.usuario["numero_conta"] = conta_corrente["numero_conta"]

    salvar_conta_corrente(conta_corrente)
    salvar_usuario(cadastroCliente.usuario)

def salvar_conta_corrente(conta_corrente):
    try:
        # Carrega os dados do arquivo JSON, se existir.
        with open("contas_correntes.json", "r") as arquivo_json:
            lista_contas_correntes = json.load(arquivo_json)
    except (FileNotFoundError, json.JSONDecodeError):
        # Cria uma lista vazia se o arquivo não existir.
        lista_contas_correntes = []

    # Adiciona a nova conta corrente à lista.
    lista_contas_correntes.append(conta_corrente)

    # Salva a lista atualizada no arquivo JSON.
    with open("contas_correntes.json", "w") as arquivo_json:
        json.dump(lista_contas_correntes, arquivo_json, indent=4)

def salvar_usuario(usuario):
    try:
        # Carrega os dados do arquivo JSON, se existir.
        with open("usuarios.json", "r") as arquivo_json:
            lista_usuarios = json.load(arquivo_json)
    except (FileNotFoundError, json.JSONDecodeError):
        # Cria uma lista vazia se o arquivo não existir.
        lista_usuarios = []

    # Adiciona o novo usuário à lista.
    lista_usuarios.append(usuario)

    # Salva a lista atualizada no arquivo JSON.
    with open("usuarios.json", "w") as arquivo_json:
        json.dump(lista_usuarios, arquivo_json, indent=4)
