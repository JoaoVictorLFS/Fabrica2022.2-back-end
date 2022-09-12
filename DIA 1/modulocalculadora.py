import os

def console():
    print("*"*50)
    print('\n[1] Adição\n[2] Subtração \n[3] Multiplicação \n[4] Divisão\n')
    print("*"*50)

def opcao():
    opcao = int(input('\nEscolha uma opção:'))
    if opcao == 1:
        return soma()
        
    elif opcao == 2:
        return subtracao()
        
    elif opcao == 3:
        return multplicacao()
        
    elif opcao == 4:
        return divisao()

def soma():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero'))
    return n1+n2

def subtracao():
     n1 = int(input('Digite um numero: '))
     n2 = int(input('Digite outro numero'))
     return n1-n2
    
def multplicacao():
     n1 = int(input('Digite um numero: '))
     n2 = int(input('Digite outro numero'))
     return n1*n2

def divisao():
     n1 = int(input('Digite um numero: '))
     n2 = int(input('Digite outro numero'))
     return n1/n2


def calculadora():
    console()
    return opcao()
    
    
   