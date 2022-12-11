valor_hora = float(input("Digite o valor da hora de trabalho:"))
horas_trabalhadas = float(input("Digite o total de horas trabalhadas por dia:"))
quant_dias = float(input("Digite a quantidade de dias trabalhados:"))
total_horas = valor_hora * horas_trabalhadas
salario = total_horas * quant_dias
salario_bruto = 21
salario_bruto = salario / 100
pagamento = salario * salario_bruto
print('O salário líquido será: ', pagamento)

