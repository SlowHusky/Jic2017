def expand(pk, cAsk):
    #cria uma matriz de sqrt(theta) elementos
    l = int(math.sqrt(pk.P._theta))
    y = [[0 for i in range(l)] for i in range(l)]
    kappa = pk.P._gamma + 6
    n = 2 #ceil (log2(thetaM + 1))
    gmpy2.get_context().precision = n
    for i in range (l): #computa matriz y[i][j]
        for j in range(l):
            y[i][j] =  float(gmpy2.mpfr(randomMatrix(i, j, kappa, pk.se, \
                    l)/(2**kappa)))
    y[0][0] =  float(gmpy2.mpfr(pk.ull/2**kappa))
    gmpy2.get_context().precision = 21000
    expand = [[1 for i in range(l)] for i in range(l)]
    for i in range(l):
        for j in range(l):
            expand[i][j] = float((cAsk * y[i][j])*2)
    return expand

