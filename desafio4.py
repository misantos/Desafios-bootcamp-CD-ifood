def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
 
  #TODO: Criar as condições para aplicar o cupom de desconto (10% ou 20%).
    desconto = input().split('%')
    desconto = int(desconto[0])
    desconto_total = total - (total * (desconto / 100))
    
    print(f'Valor total: {desconto_total:.2f}')
 
if __name__ == "__main__":
    main()