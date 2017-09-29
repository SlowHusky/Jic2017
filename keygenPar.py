
def keygen(file, size='toy'):
    P.setPar(size)
    tempo =- time.time()
    p = genZi(P._eta)
    q0, x0 = genX0(p, P._gamma, P._lambda)
    listaX = genX(P._beta, P._rho, p, q0)
    pkAsk = listaX
    pkAsk.insert(0, x0)
    while True:
        s0, s1 = genSk(P._theta, P._thetam)
        if (s0.count(1)*s1.count(1)==15): break
    se = int(time.time()*1000) #seed para RNG
    _kappa = P._gamma + 6
    ull = genUll(se, s0, s1, P._theta, _kappa, p)
    sigma0 = encryptVector(s0, p, q0, x0, P._rho)
    sigma1 = encryptVector(s1, p, q0, x0, P._rho)
    tempo += time.time()
    #picle files
    public = fheKey.pk(pkAsk, se, ull, sigma0, sigma1, P)
    secret = fheKey.sk(s0, s1, p)
    fheKey.write(puplic, 'pk_pickle_' + file)
    fheKey.write(secret, 'sk_pickle_' + file)
