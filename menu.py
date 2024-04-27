import time
saldo = 2500
LIMITES_DE_SAQUES = 3
contador_saques = 0
extrato = []

def saldo_em_conta(saldo):
    print(f"Seu saldo está no valor de R${saldo:.2f}")

def deposito(valor):
    global saldo
    saldo += valor
    extrato.append(f"Deposito de R${valor:.2f}")
    print("Depósito realizado com sucesso!")

def  saque(valor):
    global saldo
    if valor > 500:
        print("Saque excede o limite máximo.\nSaque máximo no valor de R$ 500,00")
    elif valor <= 0:
        print("Valor Inválido! Tente Novamente.")
    elif valor > saldo:
        print("Saldo Insuficiente!\nLimite máximo para saques é de R$ 500,00")
    else:
        saldo -= valor
        extrato.append(f"Saque de R$ {valor:.2f}")
        print("Saque realizado com sucesso!")
            

def extrato_fun(extrato):
    print("Seu extrato:")
    for movimentacao in extrato:
        print(movimentacao)


while True:
    menu_inicial = int(input(
        """
        --------------------------------------------

                 Olá Bem Vindo ao FutureBank       
        
        --------------------------------------------
        
        Selecione a Opção desejada:
        [1]Saldo em Conta
        [2]Depósito
        [3]Saque
        [4]Extrato
        [0]Sair
        """
    ))
    if menu_inicial == 0:
        break
    elif menu_inicial == 1:
        print("...\n")
        time.sleep(2)
        saldo_em_conta(saldo)
    elif menu_inicial == 2:
        try:
            valor = float(input("Digite o valor do depósito: R$ "))
            print("...\n")
            time.sleep(2)
            deposito(valor)
        except ValueError:
            print("Valor Inválido! Tente novamente.")
    elif menu_inicial == 3:
        try:
            valor = float(input("Valor de Saque: R$ "))
            print("...\n")
            time.sleep(2)
            saque(valor)
            contador_saques += 1
            if contador_saques >= LIMITES_DE_SAQUES:
                print("\nVocê atingiu o limite de saques diários permitidos.")
                print("...\n")
                time.sleep(2)
                break
        except ValueError:
            print("Valor Inválido! Tente Novamente.")
    elif menu_inicial == 4:
        print("...\n")
        time.sleep(2)
        extrato_fun(extrato)
print("...\n")
time.sleep(2)
print("""
-------------------------------------------
      
      Obrigado Por Usar o FutureBank
      
-------------------------------------------""")