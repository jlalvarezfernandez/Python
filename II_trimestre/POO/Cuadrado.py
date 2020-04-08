from II_trimestre.POO.Rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    """
    Implementamos la clase cuadrado partiendo de la clase Rectangulo
    Consideraremos que un cuadrado es un rectangulo con base==altura
    """

    # Constructor

    def __init__(self, lado): # le pasamos solo un aprametro, que es lo que necesita, pero al heredar de otra clase hay que hacer otro metodo
        super().__init__(lado,lado) # con este constructor nos aseguramos que el cuadrado hereda los dos parametros del constructor d ela clase rectangulo


    @property
    def lado(self):
        return self.base

    @lado.setter
    def lado(self, value):
        self.base = value
        self.altura = value

if __name__ == '__main__':


    c1 = Cuadrado (5)
    print(c1.perimetro())

