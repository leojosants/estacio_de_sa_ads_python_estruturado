def rec(n):
    if n < 2:
        return rec(n - 1)


print(rec(1))

# FUNÇÃO NÃO POSSUI CONDIÇÃO DE PARADA