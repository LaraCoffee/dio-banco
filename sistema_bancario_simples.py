from datetime import datetime



"""
operaçao de deposito:

    deve ser possivel valores positivos par minha conta
    toods os valores devem ser armaenados em uma variavel e exibidos na operacao de extrato

operaçao de saque:
    
    o sistema deve permitir realizar 3 saques diarios com limite maximo de 500 reais por saque
    caso o usuario nao tenha saldo em conta, deve ser exibida uma mensagem informando que nao ha saldo suficiente
    todos os valores devem ser armazenados em uma variavel e exibidos na operaçao de extrato
        
operacao de extrato:
    essa operaçao deve exibir todos os valores armazenados nas operaçoes de deposito e saque realizados na conta
    no fim da listagem deve ser exibido o saldo atual da conta
    os valores devem seguir o padrao R$ xxx.xx exemplo: R$ 1000.00        
"""




def menu():
    
    print("""\n Banco Quebrado
    Menu
    
    1 - Deposito
    2 - Saque
    3 - Extrato
    4 - Sair


""")
   


saldo = 0
depositos = []
saques = []
limite_saque_diario = 3
saque_limite = 500
contador_deposito = 0
contador_saque = 0



def extrato():
  
    print(' Extrato '.center(50, '#'))
    print('Depositos:')
    for deposito in depositos:
        print(f"Deposito {deposito['numero_do_deposito']}: R$ {deposito['valor']:.2f} data e hora: {deposito['data_hora']}")
        
    print('\nSaques:')   
    for saque in saques:
        print(f"Saque: {saque['numero_do_saque']}: valor de R$: {saque['valor']:.2f} data e hora: {saque['data_hora']}") 
    print(f'\nSaldo atual: R$ {saldo:.2f}')



while True:
    menu()
    opcao = input("escolha a opção desejada:")
    
    
    if opcao == '1':
        print('Deposito'.center(50,'#'))
        valor = float(input('Digite o valor do deposito: '))
        if valor > 0:
            saldo += valor
            print("Deposito realizado com sucesso")
            contador_deposito += 1
            depositos.append({'numero_do_deposito': contador_deposito ,'valor': valor, 'data_hora': datetime.now().strftime('%d/%m/%Y %H:%M:%S')})
        else:
            print("Valor invalido")  
        
        
    elif opcao == '2':
        print(' Saque '.center(50,'#'))
        valor_saque = float(input("Digite o valor a ser sacado: "))  
            
        if saldo < valor_saque:
            print("valor de saque acima do saldo existente!")
            
        elif valor_saque > saque_limite:
            print("valor de saque acima do limite permitido de R$500.00!")
            
        elif contador_saque >= limite_saque_diario: 
            print("limite de saques diarios atingido!")
    
        else:
            saldo -= valor_saque
            print("saque realizado com sucesso!")
            contador_saque += 1
            saques.append({'numero_do_saque': contador_saque ,'valor': valor_saque, 'data_hora': datetime.now().strftime('%d/%m/%Y %H:%M:%S')}) 

    elif opcao == '3':
        extrato()
    elif opcao == '4':
        print('Sair')
        break     
    else:
        print('Opcao invalida')       