# Escreva uma expressão regular para extrair códigos de produtos de strings. Os códigos seguem o
# formato PROD-XXXXX-YYYY , onde XXXXX é uma sequência de 5 dígitos e YYYY é uma sequência de 4
# dígitos.

import re

padrao = r'PROD-\d{5}-\d{4}'


texto = "Os produtos são PROD-12345-6789, PROD-99999-0001 e PROD-54321-1234."

print(re.findall(padrao,texto))