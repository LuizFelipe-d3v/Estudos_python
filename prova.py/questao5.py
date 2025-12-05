# Desenvolva uma expressão regular para validar senhas. A senha deve ter pelo menos 8 caracteres,
# incluir pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial
# (como ! , @ , # , etc).

import re

padrao_senha = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$'

senha = "Abc123!!!"
if re.match(padrao_senha, senha):
    print("Senha válida")
else:
    print("Senha inválida")