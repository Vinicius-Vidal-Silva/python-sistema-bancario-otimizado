import cadastroCliente

def cadastrarConta():
    conta_corrente = {
        "agencia": "0001",
        "numero_conta": cadastroCliente.usuario["numero_conta"],
        "usuario": cadastroCliente.usuario["numero_conta"]  # Vincular conta ao usuário
    }
    
    cadastroCliente.usuario["numero_conta"] = conta_corrente["numero_conta"]

    salvar_conta_corrente(conta_corrente)
    salvar_usuario(cadastroCliente.usuario)

### Falta implementar as duas funções

def salvar_conta_corrente(conta_corrente):
    pass

def salvar_usuario(usuario):
    pass
