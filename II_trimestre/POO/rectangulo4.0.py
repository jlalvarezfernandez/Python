class Rectangulo:  # los parentesis se ponen cuando una clase hereda de otra

    """
    VERSION 4.0
    Esta clase representa objetos de tipo rectangulo

     Acciones: calculo del perimetro
               calculo del area
               dibujar
               comparar

     Mejoras respecto a la version 3.0

     - añadimos destructor
     - lanzamos excepciones con assert
     - sobrecargamos operador *
    """

    # creamos una variable de instancia privada y publica, se ponen siempre antes del constructor

    lado_maximo = 10            #lado maximo del rectangulo (publica)
    __num_creados = 0       #contador de rectangulos creados (privada), la pasamos como propiedad

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

    # destructor, borra objetos

    def __del__(self):
        Rectangulo.__num_creados -=1



    # getters y setters (ojo!!!, estilo java, no python)

    @property
    def num_creados(self):
        return Rectangulo.__num_creados


    @property
    def base(self):
        return self.__base


    @base.setter
    def base(self, value):

        assert Rectangulo.__es_lado_correcto(value)
        self.__base = value



    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        assert Rectangulo.__es_lado_correcto(value)
        self.__altura = value



    # resto de los metodos

    @staticmethod  # para que sea privada, esta dentro del espacio de la clase no del objeto
    def __es_lado_correcto(value):
        return type(value)==type(1) and 0 < value <= Rectangulo.lado_maximo


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
            str += "-" * self.base
            str += "\n"
        str = str[:-1]
        return str

    # sobrecargamos el operador multiplicacion

    def __mul__(self, other):
        """
        multiplica la base si no se pasa de lado maximo, en ese caso lo hace con la altura
        :param other: valor entero positivo
        :return: otro rectangulo con la superficie original * otro
        """

        assert  type(other) == type(1) and other > 0  # operando correcto
        assert self.base * other <= Rectangulo.lado_maximo or self.altura * other <= Rectangulo.lado_maximo

        if self.base * other <= Rectangulo.lado_maximo:
            return Rectangulo (self.base * other, self.altura)
        else:
            return Rectangulo(self.altura * other)

    # método para llamar al objeto por un número

    def __rmul__(self, other):
        return self * other

    # método para comparar el menor, devuelve True si el objeto es menor que con el que se esta comparando

    def __lt__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() < other.area()

    # método para comparar el menor o igual, devuelve True si el objeto es menor o igual que con el que se esta comparando


    def __le__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() <= other.area()

    # método para comparar si son iguales, devuelve True si el objeto es igual que con el que se esta comparando


    def __eq__(self, other):
        assert isinstance(other, Rectangulo)
        return self.area() == other.area()



if __name__ == "__main__":

    r1 = Rectangulo(4, 1)
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






