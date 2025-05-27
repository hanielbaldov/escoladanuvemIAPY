"""
Conversor de moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.66
Taxa do euro: R$ 6.44 O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

# Valor das moedas 
valor_em_reais = 100.00
taxa_do_dolar = 5.66
taxa_do_euro = 6.44

# Conversões 
valor_em_dolares = valor_em_reais / taxa_do_dolar 
valor_em_euros = valor_em_reais / taxa_do_euro 

# Exibição dos resultados
print(f"Valor em reais: R${valor_em_reais: 2f}")
print(f"Valor em dolares: $", round(valor_em_dolares, 2))
print(f"Valor em euros: €", round(valor_em_euros, 2))