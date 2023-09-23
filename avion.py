class Tanque_Combustible:
    def __init__(self):
        self.combustible = 100

    def agregar_combustible(self,cantidad):
        self.combustible  = self.combustible + cantidad

    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self, cantidad):
        self.combustible = self.combustible - cantidad

class Avion:
    def __init__(self, tanque):
        self.posicion = 0
        self.tanque = tanque

    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia /2:
            self.posicion = self.posicion + distancia
            self.tanque.usar_combustible(distancia/2)
            print("El avion ha podido recorrer una distancia")

        else:
            print("No hay combustible para que el avion pueda volar")

    def obtener_posicion(self):
        return self.posicion

tanque = Tanque_Combustible()
boeing = Avion(tanque)

print(boeing.obtener_posicion())
boeing.mover(10)
print(boeing.obtener_posicion())
boeing.mover(50)
print(boeing.obtener_posicion())
boeing.mover(80)
print(boeing.obtener_posicion())
boeing.mover(80)
            





    
