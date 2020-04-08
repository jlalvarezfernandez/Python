class Rectangulo:  # los parentesis se ponen cuando una clase hereda de otra

    """
     Esta clase representa objetos de tipo rectangulo

     Atributos: base
                altura

     Acciones: calculo del perimetro
               calculo del area
               saber si es igual a otro rectangulo
               dibujar
               comparar

     Hay cosas que mejorar, que se harán el la version 2.0

    """

    # constructor

    def __init__(self, base, altura):

        """
        Constructor de la clase, en el tenemos que pasarle los atributos, siempre lleva uno al menos (self), los demas
        sirven para instanciar el objeto
        da un estado inicial a los objetos
        :param base: base del rectangulo
        :param altura: altura del rectangulo
        """
        # creamos los atributos

        self.base = base
        self.altura = altura

    # metodo calcular perimetro

    def perimetro(self):

        """
        :return: perimetro del rectangulo
        """
        return 2 * (self.base + self.altura)

    # metodo calcular area

    def area(self):

        """
        :return: area del rectangulo
        """
        return (self.base * self.altura)

    # metodo comparar rectangulos

    def compara(self, otro_rectangulo):

        """
        Compara nuestro rectangulo con otro
        :param otro_rectangulo: objeto con el que comparamos el actual
        :return: >0 si mayor, 0 si igual, <0 si menor
        """

        return self.area() - otro_rectangulo.area()

    # metodo saber si es igual a otro rectangulo

    def es_gemelo(self, otro_rectangulo):

        """
        comprueba si el objeto pasado es el mismo rectangulo, o sea, tiene la misma base y altura
        :param otro_rectangulo: objeto con el que comparamos el actual
        :return: True o False
        """
        return self.base == otro_rectangulo.base and self.altura == otro_rectangulo.altura

    # metodo muestra rectangulo

    def muestra(self):

        """
        muestra en pantalla el rectangulo

        :return:
        """

        for i in range(self.altura):
            print("*" * self.base)


if __name__ == "__main__":

    # creamos los objetos de la clase rectangulo

    rectangulo1 = Rectangulo(4,1)
    rectangulo2 = Rectangulo(3,2)

    print(f"Probamos clase rectangulo con rectangulo 1: ({rectangulo1.base},{(rectangulo1.altura)}) y "
          f" rectangulo 2: ({rectangulo2.base},{(rectangulo2.altura)})\n")


    # dibujamos rectangulo

    rectangulo1.muestra()

    print()

    rectangulo2.muestra()

    # comparamos

    print("Resultado de comparar rectangulo 1 con rectangulo 2:", rectangulo1.compara(rectangulo2))
    print("¿Son gemelos?", rectangulo1.es_gemelo(rectangulo2))

    # magnitudes
    print("Area rectangulo 1:",rectangulo1.area(), "perimetro rectangulo 1:", rectangulo1.perimetro())
    print("Area rectangulo 2:",rectangulo2.area(), "perimetro rectangulo 2:", rectangulo2.perimetro())






