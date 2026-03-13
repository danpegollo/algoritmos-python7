salario = float(input("Coloque o salário do funcionário: "))
percentual = int(input("Coloque o percentual de aumento: "))

aumento = salario * (percentual/100)
novo_salario = salario + aumento

print(f"O valor do aumento é {aumento:.2f}")
print(f"O salário com aumento sai de {salario:.2f} para {novo_salario:.2f}")