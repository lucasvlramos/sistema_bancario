saldo = 0
extrato = []
limite = 500
limite_saques = 3
qtd_saques= 0
saque_excedidos = False


saldo = float(input("Informe o saldo da conta"))


menu = """
= Seja Bem vindo =

[1] Sacar
[2] Depositar
[3] Extrato
[0] Sair

======= VB =======
"""

while True:
    opcao = int(input(menu))

    if opcao == 1:
        if not saque_excedidos:
            if qtd_saques < limite_saques:
                valor = float(input("Informe o valor de saque: "))
                if valor > limite:
                    print("Limite de saque excedido.")
                elif valor <= saldo:
                    saldo -= valor
                    qtd_saques += 1
                    extrato.append(("Saque", valor))
                    print("Saque realizado:", valor, 
                          "Saldo atualizado:", saldo,
                          "Quantidade de saques disponíveis:", limite_saques - qtd_saques)
                    if qtd_saques == limite_saques:
                        saque_excedidos = True
                else:
                    print("Saldo insuficiente.")
            else:
                print("Limite de saques atingido")
        else:
            print("Limite atingido, sem saques por hoje.")
            
                        
    elif opcao == 2:
        valor = float(input("Informe o valor a ser depositado: "))
        saldo += valor
        print("Deposito realizado:", valor, 
            "Saldo atualizado:", saldo)
    
    elif opcao == 3:
        print("===== Extrato =====")
        for transacao in extrato:
            print(transacao[0] + ":", transacao[1])
        print("Saldo atual:", saldo)
        
    elif opcao == 0:
        print("Obrigado por utilizar nosso sistema...")
        break
    else:
        exit("Opção inválida")