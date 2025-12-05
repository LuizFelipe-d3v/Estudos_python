# Crie uma expressão regular para analisar linhas de log com o seguinte formato: [DD/MM/AAAA
# HH:MM:SS] Severidade: Mensagem . A expressão deve capturar a data, a hora, a severidade (que pode
# ser INFO , WARNING , ERROR , DEBUG ) e a mensagem de log.

import re

import re

padrao = r'^\[(\d{2}\/\d{2}\/\d{4})\s+(\d{2}:\d{2}:\d{2})\]\s+(INFO|WARNING|ERROR|DEBUG):\s+(.*)$'

log = "[05/12/2025 14:32:10] ERROR: Falha ao conectar ao banco de dados"

resultado = re.match(padrao, log)

if resultado:
    data, hora, severidade, mensagem = resultado.groups()
    print("Data:", data)
    print("Hora:", hora)
    print("Severidade:", severidade)
    print("Mensagem:", mensagem)
