import pickle
class pk():
    '''classe para armazenar a chave privada'''
    def __init__(self, pkAsk, se, ull, sigma0, sigma1, P):
        self.pkAsk = pkAsk
        self.se = se
        self.ull = ull
        self.sigma0 = sigma0
        self.sigma1 = sigma1
        self.P = P

class sk():
    '''classe para armazenar a chave publica'''
    def __init__(self, sz, su, P):
        self.s0 = sz
        self.s1 = su
        self.P = P
    def write(obj, name):
        with open(name, 'wb') as arq:
            pickle.dump(obj, arq)

    def read(name):
        with open(name, 'rb') as arq:
            return pickle.load(arq)
