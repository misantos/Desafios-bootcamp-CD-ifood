valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

#TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
valor_total_pedido = (valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida)

#TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
troco = valorPago - valor_total_pedido

#TODO: Imprimir a saída no formato especificado neste desafio.
print(f'O preço final do pedido é R$ {valor_total_pedido:.2f}. Seu troco é R$ {troco:.2f}.')