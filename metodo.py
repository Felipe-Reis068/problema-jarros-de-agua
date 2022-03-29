#Criando objeto Jarro
class Jarro:
    def _init_(s, v, l):
        s.vo = v
        s.li = l

    def setVol(s, x):
        s.vo = x

    def getVol(s):
        return s.vo

    def setLimited(s, x):
        s.li = x

    def getLimited(s):
        return s.li

    def despeja(s, x):
        Total = 0
        if (s.vo + x <= s.li):
            s.vo += x
        elif (s.vo + x > s.li):
            Atual = s.li - s.vo
            Total = x - Atual
            s.vo += Atual
        return Total

# Método para despejo
class Metodo:
    def ___init___ (s, jarro1, jarro2):
        s.jarro1 = jarro1
        s.jarro2 = jarro2

    def setJarro1(s, jarro1):
        s.jarro1 = jarro1
    def getJarro1(s):
        return s.jarro1

    def setJarro2(s, jarro2):
        s.jarro2 = jarro2
    def getJatto2(s):
        return s.jarro2

    def encheJarro1(s):
        s.jarro1.setVol(s.jarro1.getLimited())

    def encheJarro2(s):
        s.jarro2.setVol(s.jarro2.getLimited())
    
    def esvaziarJarro1(s):
        s.jarro1.setVol(0)
    
    def esvaziarJarro2(s):
        s.jarro2.setVol(0)
    
    def despejarJarro1emJarro2(s):
        sobra = s.jarro2.despeja(s.jarro1.getVol())
        s.jarro1.setVol(sobra)
    
    def despejarJarro2emJarro1(s):
        sobra = s.jarro1.despeja(s.jarro2.getVol())
        s.jarro2.setVol(sobra)