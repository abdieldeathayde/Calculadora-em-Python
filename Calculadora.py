def Calculadora():

  num1 = input ("Digite o primeiro numero: ");
  num1 = int (num1);

  num2 = input ("Digite o segundo numero: ");
  num2 = int (num2);

  operacao = input ("-----Escolha uma operação matemática ----\n\n '+' soma \n '-' subtracao \n '*' multiplicacao \n '/' divisao \n 'pow' potencia\n");
  operacao = str (operacao); 


  if operacao == '+':
    soma = num1 + num2;

    print(soma);

  elif operacao == '-':
    sub = num1 - num2;

    print (sub);


  elif operacao == "*":
    mult = num1 * num2;

    print(mult);

  elif operacao == "/":
    div = num1 / num2;

    print(div);

  elif operacao == "pow":
   potencia = pow(num1,num2);

   print(potencia);

  else:
    print("Erro, tente novamente");

Calculadora();
