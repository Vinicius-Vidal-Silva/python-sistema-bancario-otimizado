lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 3, 6, 7]

def verifica_na_lista(valor, lista):
  return any(elemento == valor for elemento in lista)

valor_input = int(input("Digite um valor: "))

if verifica_na_lista(valor_input, lista):
  print(f"{valor_input} já está na lista.")
else:
  print(f"{valor_input} não está na lista.")
