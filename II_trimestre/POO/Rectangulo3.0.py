class Rectangulo:  # los parentesis se ponen cuando una clase hereda de otra

    """
    VERSION 3.0
    Esta clase representa objetos de tipo rectangulo

     Acciones: calculo del perimetro
               calculo del area
               dibujar
               comparar

     Mejoras respecto a la version 2.0

     - Quitemos getters (observador) y setters(modificador) estilo java y los sustituimos por propiedades.
     - Usaremos metodos privados (no se pueden acceder desde fuera) y estaticos
     - Usaremos variables de instancia de clase, es un atributo compartido por todos los objetos

    """

    # creamos una variable de instancia privada y publica, se ponen siempre antes del constructor

    lado_maximo = 10            #lado maximo del rectangulo (publica)
    __num_creados = 0           #contador de rectangulos creados (privada), la pasamos como propiedad

    # constructor

    def __init__(self, base, altura):

        """
        Constructor de la clase
        :param base: base del rectangulo
        :param altura: altura del rectangulo
        """
        self.__base = 1 # el doble guión bajo es para proteger ese atributo
        self.__altura = 1
        Rectangulo.__num_creados +=1

        # por si hubiera errores en los parametros hemos dado valor inicial
        self.base = base
        self.altura = altura

    # getters y setters (ojo!!!, estilo java, no python)

    @property
    def num_creados(self):
        return Rectangulo.__num_creados


    @property
    def base(self):
        return self.__base


    @base.setter
    def base(self, value):
        if Rectangulo.__es_lado_correcto(value):
            self.__base = value
        else:
            print("!!ERROR, base incorrecta!!")


    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        if  Rectangulo.__es_lado_correcto(value):
            self.__altura = value
        else:
            print("!!ERROR, altura incorrecta!!")


    # resto de los metodos

    @staticmethod  # para que sea privada, esta dentro del espacio de la clase no del objeto
    def __es_lado_correcto(value):
        return type(value) == type(1) and 0 < value <= Rectangulo.lado_maximo


    def perimetro(self):

        """

        :return: perimetro del rectangulo

        """
        return 2 * (self.base + self.altura)


    def area(self):

        """

        :return: area del rectangulo

        """
        return (self.base * self.altura)

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
        return self.base == otro_rectangulo.base and self.altura == otro_rectangulo.altura


    def muestra(self):

        """
        muestra en pantalla el rectangulo

        :return:
        """

        print(self)

    # metodos sobrecargados

    def __str__(self):
        str = ""
        for i in range(self.altura):
            str += "*" * self.base
            str += "\n"
        str = str[:-1]
        return str


if __name__ == "__main__":

    r1 = Rectangulo(40, 1)
    r2 = Rectangulo(3, 2)

    print(f"Probamos clase rectangulo con rectangulo1: ({r1.base} , {(r1.altura)}) y "
          f" rectangulo2: ({r2.base} , {(r2.altura)})\n")


    # dibujamos rectangulo

    r1.muestra()

    print()

    r2.muestra()

    # comparamos

    print("Resultado de comparar rectangulo1 con rectangulo2:", r1.compara(r2))
    print("¿Son gemelos?", r1.es_gemelo(r2))

    # magnitudes
    print("Area rectangulo1:", r1.area(), "perimetro rectangulo1:", r1.perimetro())
    print("Area rectangulo2:", r2.area(), "perimetro rectangulo2:", r2.perimetro())
    # accedemos a variables de instancia de clase
    print("rectangulos creados", r1.num_creados)
    print("cual es el lado máximo del rectangulo: ", Rectangulo.lado_maximo)






