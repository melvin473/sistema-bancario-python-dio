saldo = 0
q_saques = 0

# Menu principal, exibido no início do
# programa e no final de cada operação
def menu():
  opcao = input("\n\n [1] Extrato\n [2] Depositar\n [3] Sacar\n [0] Sair\n\nEscolha a opção desejada:")
  if opcao == "1":
    extrato()
  elif opcao == "2":
    depositar()
  elif opcao == "3":
    sacar()
  elif opcao == "0":
    pass
  else:
    print("Opção inválida. Digite novamente.")
    menu()

# Exibe o extrato da conta
def extrato():
  print("\n\n*** EXTRATO ***\n\nSaldo: {}\nQuantidade de saques: {}".format(saldo, q_saques))
  menu()

# Realiza o depósito na conta
def depositar():
  global saldo
  valor = float(input("\n(Para voltar, digite zero.)\nDigite o valor do depósito: "))
  if valor == 0:
    print("Depósito cancelado.")
    menu()
  confirma = input("\nDepósito de R${:.2f}. Deseja confirmar? [s]/[n]: ".format(valor))
  if confirma == "s":
    saldo += valor
    print("Depósito de R${:.2f} realizado com sucesso.\nSeu saldo atual é de R${:.2f}.".format(valor, saldo))
    menu()
  elif confirma == "n":
    print("Depósito cancelado.")
    menu()

# Realiza o saque da conta
def sacar():
  global saldo
  global q_saques
  if q_saques == 3:
    print("Número máximo de saques atingido.\nTente novamente em 24h.")
    menu()
  else:
    valor = float(input("\n(Para voltar, digite zero.)\nDigite o valor do saque: "))
    if valor == 0:
      print("Saque cancelado.")
      menu()
    if valor > saldo:
      print("Saldo insuficiente.")
      sacar()
    confirma = input("\nSaque de R${:.2f}. Deseja confirmar? [s]/[n]: ".format(valor))
    if confirma == "s":
      saldo -= valor
      q_saques += 1
      print("Saque de R${:.2f} realizado com sucesso.\nSeu saldo atual é de R${:.2f}.".format(valor, saldo))
      menu()
    elif confirma == "n":
      print("Saque cancelado.")
      menu()

print("*** Python Bank ***")
menu()
