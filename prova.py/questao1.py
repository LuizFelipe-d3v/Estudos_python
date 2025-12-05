# Escreva uma expressão regular que valide endereços de e-mail no formato nome@dominio.com . O
# nome pode conter letras, números, pontos, hifens e underscores. O dominio deve conter apenas
# letras e pode ter um ou mais sufixos de domínio, como .com , .net , .org , etc.

import re

def validar_email(email):
    email_valido = r'[a-zA-Z0-9.-_]+@[a-zA-Z]+\.[a-z]'

    if re.match(email_valido, email):
        return True
    else:
        return False
    

print(validar_email("Teste@dominio.com"))
print(validar_email("teste@dominio"))
