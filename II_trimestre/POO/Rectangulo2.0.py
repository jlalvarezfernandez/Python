class Rectangulo:  # los parentesis se ponen cuando una clase hereda de otra

    """
    VERSION 2.0
     Esta clase representa objetos de tipo rectangulo

     Acciones: calculo del perimetro
               calculo del area
               dibujar
               comparar
     Mejoras respecto a la version anterior

     - Protegemos (ocultamos) los atributos, esto es encapsular
     - Creamos getters (observador) y setters(modificador) para acceder a los mismos. Ojo, esta no es la filosofia de Python
     - Sobrecargamos el metodo __str__ para poder usar la funcion print y otras.

    """

    # constructor

    def __init__(self, base, altura):

        """
        Constructor de la clase, en el tenemos que pasarle los atributos, siempre lleva uno al menos (self),
        los demas sirven para instanciar el objeto
        da un estado inicial a los objetos
        :param base: base del rectangulo
        :param altura: altura del rectangulo
        """
        # creamos los atributos

        self.__base = 1 # el doble guión bajo es para proteger ese atributo
        self.__altura = 1
        # ojo solo en este ejemplo
        self.set_base(base)
        self.set_altura(altura)

    # getters y setters (ojo!!!, estilo java, no python)

    # getter: sirve para devolver el valor de este atributo (observador)

    def get_base(self):
        """
        getter tipo java
        :return:
        """
        return self.__base

    # Setter: permite cambiar el valor del atributo (modificador), por ese le metemos dos aprametros el propio y el que le vamos a dar nuevo

    def set_base(self, base):
        """
        setter tipo java
        :param base:
        :return:
        """
        if base > 0:
            self.__base = base
        else:
            # mucho mejor mandar una excepcion
            print("!!ERROR, base incorrecta!!")

    def get_altura(self):
        """

        :return:
        """
        return self.__altura

    def set_altura(self, altura):
        """

        :param altura:
        :return:
        """
        if altura > 0:
            self.__altura = altura
        else:
            print("!!ERROR, altura incorrecta!!")

    # resto de los metodos

    def perimetro(self):

        """

        :return: perimetro del rectangulo

        """
        return 2 * (self.__base + self.__altura)


    def area(self):

        """

        :return: area del rectangulo

        """
        return (self.__base * self.__altura)

    def compara(self, otro_rectangulo):

        """
        Compara nuestro rectangulo con otro
        :param otro_rectangulo: objeto con el que comparamos el actual
        :return: >0 si mayor, 0 si igual, <0 si menor

        """

        return self.area() - otro_rectangulo.area()

    def es_gemelo(self, otro_rectangulo):

        """
        comprueba si el objeto pasado es el mismo rectangulo, o sea, tiene la misma base y altura
        :param otro_rectangulo: objeto con el que comparamos el actual
        :return: True o False
        """
        return self.__base == otro_rectangulo.get_base and self.__altura == otro_rectangulo.get_altura


    def muestra(self):

        """
        muestra en pantalla el rectangulo

        :return:
        """

        print(self)

    # metodos sobrecargados

    def __str__(self):
        str = ""
        for i in range(self.__altura):
            str += "*" * self.__base
            str += "\n"
        str = str[:-1]
        return str





if __name__ == "__main__":

    rectangulo1 = Rectangulo(4,1)
    rectangulo2 = Rectangulo(3,2)

    print(f"Probamos clase rectangulo con rectangulo1: ({rectangulo1.get_base} , {(rectangulo1.get_altura)}) y "
          f" rectangulo2: ({rectangulo2.get_base} , {(rectangulo2.get_altura)})\n")


    # dibujamos rectangulo

    rectangulo1.muestra()

    print()

    rectangulo2.muestra()

    # comparamos

    print("Resultado de comparar rectangulo1 con rectangulo2:", rectangulo1.compara(rectangulo2))
    print("¿Son gemelos?", rectangulo1.es_gemelo(rectangulo2))

    # magnitudes
    print("Area rectangulo1:",rectangulo1.area(), "perimetro rectangulo1:", rectangulo1.perimetro())
    print("Area rectangulo2:",rectangulo2.area(), "perimetro rectangulo2:", rectangulo2.perimetro())






