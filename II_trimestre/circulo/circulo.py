"""

/**
 * 2. Crea la clase “Circulo” en Java que responda al siguiente comportamiento:

              Un círculo puede crecer. Aumenta su radio.
              Un círculo puede menguar. Decrementa su radio.
              Un círculo me devuelve su área si se la pido.
              Un círculo me dice su estado, por ejemplo “Soy un círculo de radio 0.5 metros.
              Ocupo un área de 0.7853981633974483 metros cuadrados” (método toString())


3. Crea una clase TestCirculo que cree una instancia de “Circulo”, muestre su estado, lo haga crecer 27 veces, averigüe su área,
   lo haga decrecer 10 veces y muestre su estado final.

4. Modifica la clase Círculo para que cuando el radio se convierta a 0 el círculo reaccione y diga con una caja de texto gráfica
   “Soy un mísero punto sin área” usando la clase JOptionPane del paquete javax.swing. Podéis ver este vídeo: https://youtu.be/F_48qh3BcDs

 * @author AJFRU
 *
 */
"""

import math
from _json import make_encoder


class Circulo:

    # constructor

    def __init__(self, radio):
        self.__radio = radio


    # geters y seters


    @property
    def radio(self):
        return self.radio

    @radio.setter
    def radio(self, value):
        self.radio = value

    # sobrecarga cadena

    def __str__(self):
        return f"Soy un círculo de radio {self.__radio} metros. Ocupo un área de {c1.area()} metros cuadrados"



    def area (self):
        """
        # metodo para calcular area
        :return:
        """
        return math.pi * math.pow(self.__radio,2)

    def crece(self, tamanio):
        if (self.__radio < 0):
           print("Error, el radio no puede ser negativo")
        self.__radio *= tamanio
        return self.__radio

    def mengua(self, tamanio):
       if self.__radio < 0:
           print("Error, el radio no puede ser negativo")

       return self.__radio - tamanio


if __name__ == '__main__':


    c1 = Circulo(2)

    print(c1)
    print("area",c1.area())
    print()
    print("Circunferencia despues de aumentar 27 veces su radio", c1.crece(27))
    print("area",c1.area())
    print()
    print("Circunferencia despues de menguar 10 veces su radio",c1.mengua(10))
    print()
    print("Estado final de la circunferencia", c1.area())



