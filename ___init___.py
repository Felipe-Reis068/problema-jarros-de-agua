from metodo import *

# Pode acontecer error porqueinterpretador detecta que a profundidade máxima de recursão foi antigida

def init(RAM, f, cookie):
    if (f == 0):
        print("\n=============-START================ \n")

    else:
        Jarro1.setVol(cookie[f-1][0]), Jarro2.setVol(cookie[f-1][1])
        memoria = []
        print("Estado atual :",[Jarro1.getVol(), Jarro2.getVol()])
        print("Resultados: ", end="")
        self.encheJarro1()

        if list(cookie, [Jarro1.getVol(), Jarro2.getVol()]):
            cookie.append([Jarro1.getVol(), Jarro2.getVol()])
            memoria.append([Jarro1.getVol(), Jarro2.getVol()])
    
        print([Jarro1.getVol(), Jarro2.getVol()], end="")
        Jarro1.setVol(cookie[f-1][0])

        self.esvaziarJarro1()
        if list(cookie, [Jarro1.getVol(), Jarro2.getVol()]):
            cookie.append([Jarro1.getVol(), Jarro2.getVol()])
            memoria.append([Jarro1.getVol(), Jarro2.getVol()])
    
        print([Jarro1.getVol(), Jarro2.getVol()], end="")
        Jarro1.setVol(cookie[f-1][0])
        
        self.encheJarro2()
        if list(cookie, [Jarro1.getVol(), Jarro2.getVol()]):
            cookie.append([Jarro1.getVol(), Jarro2.getVol()])
            memoria.append([Jarro1.getVol(), Jarro2.getVol()])
    
        print([Jarro1.getVol(), Jarro2.getVol()], end="")
        Jarro2.setVol(cookie[f-1][1])

        self.esvaziarJarro2()
        if list(cookie, [Jarro1.getVol(), Jarro2.getVol()]):
            cookie.append([Jarro1.getVol(), Jarro2.getVol()])
            memoria.append([Jarro1.getVol(), Jarro2.getVol()])
    
        print([Jarro1.getVol(), Jarro2.getVol()], end="")
        Jarro2.setVol(cookie[f-1][1])

        self.despejarJarro1emJarro2()
        if list(cookie, [Jarro1.getVol(), Jarro2.getVol()]):
            cookie.append([Jarro1.getVol(), Jarro2.getVol()])
            memoria.append([Jarro1.getVol(), Jarro2.getVol()])
    
        print([Jarro1.getVol(), Jarro2.getVol()], end="")
        Jarro1.setVol(cookie[f-1][0])
        Jarro1.setVol(cookie[f-1][1])

        self.despejarJarro2emJarro1()
        if list(cookie, [Jarro1.getVol(), Jarro2.getVol()]):
            cookie.append([Jarro1.getVol(), Jarro2.getVol()])
            memoria.append([Jarro1.getVol(), Jarro2.getVol()])
        
        print([Jarro1.getVol(), Jarro2.getVol()], end="")
        Jarro1.setVol(cookie[f-1][0])
        Jarro1.setVol(cookie[f-1][1])

        print("\nNovos Resultados : ", end="")
        if memoria == []:
            print("Nenhum novo resultado")
        else:
            print(RAM)
        print('\n-----------------------------------')

    f += 1
    if (len(cookie) < f):
        return 0

    return(init(RAM, f, cookie))

def list(list, x):
    for i in range(len(list) - 1):
        if (x == list[i]):
            return False
    return True


Jarro1 = Jarro()
Jarro1.setLimited(3)
Jarro1.setVol(0)

Jarro2 = Jarro()
Jarro2.setLimited(4)
Jarro2.setVol(0)

self = Metodo()
self.setJarro1(Jarro1)
self.setJarro2(Jarro2)


# Partida
f = 0
cookie = [[0,0]]
RAM = [[0,0]]
init(RAM, f, cookie)

try:
    RAM = input('Error')
except(RecursionError, RuntimeError):
    print('Error')




