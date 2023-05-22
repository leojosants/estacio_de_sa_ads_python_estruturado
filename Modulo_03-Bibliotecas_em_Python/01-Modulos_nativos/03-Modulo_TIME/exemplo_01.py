"""
    Exemplo de chamada das funções time() e ctime().
"""
import time

# A variável x recebe o número de segundos desde 00:00:00 de 01/01/1970 pela função time().
x = time.time()

# Ao executar ctime(x), o número de segundos armazenado em x é convertido em uma string com o horário local.
print(f'Local time: {time.ctime(x)}')
