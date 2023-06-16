import textwrap

def menu():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    return input(textwrap.dedent(menu))

def deposito(saldo, valor, extrato, /):
    if(valor > 0 and valor <= 500):
        saldo += valor
        extrato += f'Déposito: R$ {valor:.2f}\n'
        return saldo, extrato
    else:
        print('O valor informado é invalido')

def sacar(*, valor, saldo, numero_saques, limite, extrato, limite_saques):
    if(valor > 0 and valor < saldo and numero_saques<limite_saques):
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'     
        numero_saques+=1
        return saldo, extrato
    else:
        print('O valor informado é invalido ou voce atingiu seu limite de saques')

def exibir_extrato(saldo,extrato):
    print(extrato)
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Valor do Deposito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        
        elif opcao == 's':
            valor = float(input("Valor do Saque: "))

            saldo, extrato = sacar(
                saldo=saldo, 
                valor= valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=LIMITE_SAQUES)
                
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            print("Operações realizadas")
            break

        else:
            print("Não foi identificada sua operação!!")

main()