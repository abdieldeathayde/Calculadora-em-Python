from sys import exit

def Calculadora():
  

  operacao = 1


  while operacao > 0:

    print("Digite o primeiro numero: ");
    num1 = int(input())
    

    print("Digite o segundo numero: ");
    num2 = int(input())
 

    print ("-----Escolha uma operação matemática ----\n\n 1 - soma \n 2 - subtracao \n 3 - multiplicacao \n 4 - divisao \n 5 - potencia\n '0' Sair");
    operacao = int(input())
    opcoes(operacao, num1, num2)

    
   


def opcoes(operacao, num1, num2):
  if operacao == 1:
    somar(num1, num2)

  elif operacao == 2:
    subtrair(num1, num2)


  elif operacao == 3:
    multiplicar(num1, num2)

  elif operacao == 4:
    dividir(num1, num2)

  elif operacao == 5:
    elevar(num1, num2)

  elif operacao == 0:
    exit()

  else:
    print("Erro, tente novamente"); 

def somar(num1, num2):
  soma = num1 + num2;
  print(soma);

def subtrair(num1, num2):
  sub = num1 - num2;
  print (sub);

def multiĺicar(num1, num2):
  mult = num1 * num2;
  print(mult);

def dividir(num1, num2):
  div = num1 / num2;
  print(div);

def elevar(num1, num2):
  potencia = pow(num1,num2);
  print(potencia);

Calculadora();

