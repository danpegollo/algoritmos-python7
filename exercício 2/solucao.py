km_percorridos = float(input("Coloque a quantidade de km que o carro percorreu: "))
dias_alugado = int(input("Coloque a quantidade de dias pelos os quais o carro ficou alugado: "))

preco_pagar = (dias_alugado * 60) + (km_percorridos * 0.15)
print(f"O carro que ficou {dias_alugado} dias alugado e percorreu {km_percorridos} km deve pagar {preco_pagar:.2f}")