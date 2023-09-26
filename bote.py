class TanqueCombustible:
    def __init__(self):
        self.combustible = 100

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible = self.combustible - cantidad

class Lancha:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia/2:
            self.posicion = self.posicion + distancia
            self.tanque.usar_combustible(distancia/2)
            print("El bote se ha movido exitosamente")
        else:
            print("No hay suficiente combustible para mover el bote")

    def obtener_posicion(self):
        return self.posicion
    
tanque = TanqueCombustible()
yate = Lancha(tanque)
print(yate.obtener_posicion())
yate.mover(10)
print(yate.obtener_posicion())
yate.mover(50)
print(yate.obtener_posicion())
yate.mover(80)
print(yate.obtener_posicion())
yate.mover(100)
print(yate.obtener_posicion())