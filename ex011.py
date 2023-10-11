num1 = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o Segundo numero: '))

op = float(input('qual operação deseja realizar entre os dois números?\n 1. soma \n 2. subtração \n 3. multiplicação \n 4. divisão \n  '))

if op == 1:
    r = num1+num2
    print('o valor da soma é: {}'.format(r))

elif op == 2: 
    r = num1 - num2
    print('o resultado da subtração é: {}'.format(r))
elif op == 3:
    r = num1*num2
    print('o resultado da subtração é: {}'.format(r))
elif op == 4:
    r = num1/num2
    print('o resultado da divisão é: {}'.format(r))
else: 
    
    print ('essa opção não é valida')
