numPedidos = int(input())
lista = []

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = False
    eh_vegano = input()

    #TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
    if eh_vegano == 's':
      ehVegano = True
    
    lista.append([i, prato, ehVegano, calorias])

for pedido in lista:
    if pedido[2] == True:
        pedido[2] = 'Vegano'
    else:
        pedido[2] = 'Nao-vegano'
    print(f'Pedido {pedido[0]}: {pedido[1]} ({pedido[2]}) - {pedido[3]} calorias')
    #print(pedido, sep='\n')