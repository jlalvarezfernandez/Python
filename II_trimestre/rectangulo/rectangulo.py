# definimos la clase rectangulo

class Rectangulo():
    """
             Esta clase representa objetos de tipo rectangulo

             Atributos: base
                        altura

             Acciones: calculo del perimetro
                       calculo del area
                       saber si es igual a otro rectangulo
                       dibujar
                       comparar

            """
    # creamos una variable de instancia privada y publica, se ponen siempre antes del constructor

    lado_maximo = 10
    __num_creados = 0
    # creamos el constructor de la clase Rectangulo para dar un estado inicial a los objetos de esta clase

    def __init__(self, base, altura):

        """
         creamos los atributos
        :param base:
        :param altura:
        """
        self.__base = 1
        self.__altura = 1
        Rectangulo.__num_creados += 1
        # por si hubiera errores en los parametros hemos dado valor inicial
        self.base = base
        self.altura = altura


    # propiedades para la clase rectangulo, equivalen a los getters y bsetters de java

    # se tratan como atributos

    @property
    def num_creados(self):
        return Rectangulo.__num_creados

    # seria como el getter de java

    @property
    def base(self):
        return self.__base

    @property
    def altura(self):
        return self.__altura


    # serian como los setters de java

    @base.setter
    def base(self, base):
        if Rectangulo.__es_lado_correcto(base):
            self.__base = base
        else:
            print("Error, base incorrecta!!")

    @altura.setter
    def altura(self,altura):
        if Rectangulo.__es_lado_correcto(altura):
            self.__altura = altura
        else:
            print("Error, base incorrecta!!")

    # Metodos

    # Método para calcular el perimetro del rectangulo

    def perimetro(self):
        return (self.__base + self.__altura) * 2

    # Método para calcular el área del rectangulo

    def area(self):
        return (self.__base * self.__altura);

    # método para comparar rectangulos

    def compara(self, otro_rectangulo):
        """
        :param otro_rectangulo:
        :return: >0 si mayor, 0 si igual, <0 si menor
        """
        return self.area() - otro_rectangulo.area()

    # método para saber si son iguales dos rectangulos

    def es_gemelo (self, otro_rectangulo):
        return self.__base == otro_rectangulo.__base and self.__altura == otro_rectangulo.__altura


    # método mastrar rectangulo

    def muestra (self):
        print(self)

        # metodos sobrecargados para mostrar el rectangulo

    def __str__(self):
        str = ""
        for i in range(self.__altura):
            str += "*" * self.__base
            str += "\n"

        return str

    # resto metodos
    '''
    este método es privado y estático
    '''
    @staticmethod
    def __es_lado_correcto(value):
        return type(value) == type(1) and 0 < value <= Rectangulo.lado_maximo



if __name__ == '__main__':

    r1 = Rectangulo(5,7)
    r2 = Rectangulo(8,6)


    print("Ejercicio sobre la clase Rectangulo, probaremos los diferentes métodos")
    print()
    print(f"probamos el rectangulo r1 ({r1.base},{r1.altura}) y el rectangulo r2"
          f" ({r2.base},{r2.altura})")
    print()
    print("Mostramos el rectangulo r1: \n")
    r1.muestra()
    print()
    print("Mostramos el rectangulo r2: \n")
    r2.muestra()
    print()
    print("El perimetro del rectangulo r1 es: ",r1.perimetro() ,"cm")
    print()
    print("El perimetro del rectangulo r2 es:", r2.perimetro(),"cm")
    print()
    print("Los rectangulos son gemelos (iguales en su área): ",r1.es_gemelo(r2))
    print()
    print("El resultado de comparar los rectangulos r1 y r2 es: ", r1.compara(r2))
    print()
    print("Número de rectangulos creados: ", r1.num_creados)
    print()
    print("Cual es el lado maximo del rectangulo: ",r1.lado_maximo)



