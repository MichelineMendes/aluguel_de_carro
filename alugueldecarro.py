carro = """
          / ######## \\
         /            \\
    ####/______________\\ #######|
    §)   ___      |       ___   (@ 
    |_ (@  @)____|_____(@  @)___| 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~      
"""
print(carro)
print("#" * 10, "Calcule valor a ser pago pelo aluguel de um carro, considerando Km e dias de uso" , "#"* 10)
print("O carro custa R$ 100 por dia e R$ 0,50 por km rodado.\n")
dias = int(input("Informe a quantidade de dias de locação do veículo: "))
uso = float(input("Informe a quilometragem rodada:  "))

pagar = dias * 100 + uso * 0.5

print("Valor a ser pago: R$", pagar )

