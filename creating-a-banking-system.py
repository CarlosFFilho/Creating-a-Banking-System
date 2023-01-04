depositos = []
saques = []
extrato = 0 #Saldo final

numero_saques = 0

print("Comandos: (a) Saque, (b) Depósito, (c) Ver extrato")
print ("Para finalizar as ações digite FINALIZAR")

acao = 0

while acao != "FINALIZAR":
    
    print("Qual ação deseja realizar?")
    acao = input("Comando: ")
    
    if acao == "a":
        if numero_saques < 3:
            valor_saque = float(input("Valor de Saque: "))
            if valor_saque < 0 or valor_saque > 500:
                print("Valor inválido!")
            else:
                if valor_saque <= extrato:
                    numero_saques+=1
                    saques.append(valor_saque)
                    extrato = extrato - valor_saque
                else:
                    print("Valor de saque é superior ao valor em conta!")
        else:
            print("Já foram realizados os 3 sauques permitidos!")
        
    elif acao == "b":
        valor_deposito = float(input("Valor de Depósito: "))
        if valor_deposito<0:
            print("Valor inválido!")
        else:
            depositos.append(valor_deposito)
            extrato += valor_deposito
        
    elif acao == "c":
        if len(saques) == 0 and len(depositos)== 0:
            print("Não foram realizadas movimentações")
        else:
            print("Saques")
            for i in saques:
                print ('R$%.2f' %(i))
            print("-----")
            print("Depósitos")
            for q in depositos:
                print ('R$%.2f' %(q))
            print("-----")
            print('SALDO FINAL: R$%.2f' %(extrato))
    else:
        print("Operação inválida!")