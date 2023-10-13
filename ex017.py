print('--------Está na dúvida se sua cidade começa com "SANTO"? Digite aqui para sanar sua dúvida--------')
n = input('Nome da cidade: ')
dividido = n.split()

if 'SANTO' in dividido[0]:
    print('Sua cidade começa com SANTO!!!')
else:
    print('Sua cidade não começa com SANTO!!!')