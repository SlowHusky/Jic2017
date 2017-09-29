def encrypt(pk, m):
    if m != 0 and m !=1:
        print('not a valid m')
        return 0
    alpha = pk.P._lambda
    matrix = [[0 for i in range(pk.P._beta)] for j in range(pk.P._beta)]
    for i in range(pk.P._beta):
        for j in range(pk.P._beta):
            matrix[i][j] = random.randint(0, 2**alpha - 1)
    pprime = 2**pk.P._rho
    r = random.randint(-pprime, pprime)
    pkAsk = (pk.pkAsk).copy()
    x0 = pkAsk.pop(0)
    xi0 = pkAsk[::2]
    xj1 = pkAsk[1::2]
    # iniciando processo de encriptacao
    somatorio = mpz(0)
    for i in range(pk.P._beta):
        for j in range(pk;P._beta):
            x = gmpy2.mul(xj1[j], xi0[i])
            somatorio += gmpy2.mul(matrix[i][j], x)
    c = (mpz(m) + 2*r + 2*somatorio) % x0
    return c
