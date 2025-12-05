# Desenvolva uma expressão regular para extrair datas no formato DD/MM/AAAA de um texto. Os dias
# ( DD ) e meses ( MM ) podem ter um ou dois dígitos, enquanto o ano ( AAAA ) deve ter quatro dígitos.

import re

texto = ("Hoje e dia 05/12/2025 amanha sera dia 06/12/2025")

resultado = re.sub(r"\b\d{1,2}/\d{1,2}/\d{4}\b", "DD/MM/AAAA", texto)

print(resultado)    