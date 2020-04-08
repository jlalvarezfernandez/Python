"""
2. Crea una clase Fracción (Python) de forma que podamos hacer las siguientes operaciones:

-Construir un objeto Fracción pasándole el numerador y el denominador.
-Obtener la fracción como cadena de caracteres.
-Obtener y modificar numerador y denominador. No se puede dividir por cero.
-Obtener resultado de la fracción (número real).
-Multiplicar la fracción por un número.
-Multiplicar, sumar y restar fracciones.
-Simplificar la fracción.

"""
# Creamos la calse fracción

class Fraccion:

    # constructor

    def __init__(self, numerador, denominador):
        """
        :param numerador: numerador
        :param denominador: denominador
        """
        self.__numerador = numerador
        self.__denominador = denominador

    # método getter numerador
    @property
    def numerador(self):
        """
        :return: numerador
        """
        return self.__numerador

    # metodo setter numerador
    @numerador.setter
    def numerador(self, value_numerador):
        """
        :param value_numerador:
        """
        self.__numerador = value_numerador

    # metodo getter denominador
    @property
    def denominador(self):
        """
        :return: denominador
        """
        return self.__denominador

    # metodo setter denominador
    @denominador.setter
    def denominador(self, value_denominador):
        """
        :param value_denominador:
        :return:
        """
        assert value_denominador != 0
        self.__denominador = value_denominador

    # resto de metodos

    # mostrarFraccion

    def __str__(self):
        return f"{self.__numerador} / {self.__denominador}"

    # resultado_fraccion

    def resultado(self):
        return self.__numerador / self.__denominador

    # multiplicar_por_otro_fraccion

    def multiplica_por_fraccion(self, fraccion):
        return print(self.__numerador * fraccion.__numerador, "/", self.__denominador * fraccion.__denominador)

    # multiplicar por un numero

    def multiplica_por_num(self, num):
        return print(self.__numerador * num, "/", self.denominador * 1)

    #Suma fracciones

    def suma_fracciones(self, otra_fraccion):
        self.__numerador = (self.__numerador * otra_fraccion.denominador) + (self.__denominador * otra_fraccion.numerador)
        self.__denominador = (self.__denominador * otra_fraccion.denominador)

    # resta fracciones
    def resta_fracciones(self,otra_fraccion):
        self.__numerador = (self.__numerador * otra_fraccion.denominador) - (self.__denominador * otra_fraccion.numerador)
        self.__denominador = (self.__denominador * otra_fraccion.denominador)

    # metodo para calcular el mcd de la fracción para despues simplificar la fraccion

    def mcd(self):
        dividendo = self.__numerador
        divisor = self.__denominador
        resto = dividendo % divisor

        while resto != 0:
            dividendo = divisor
            divisor = resto
            resto = dividendo % divisor
            mcd = divisor
        return mcd
    # metodo apra simplificar la fraccion

    def simplifica(self):
        """
        Simplifica la fracción partiendo del mcd.
        """
        mcd = self.mcd()
        self.__numerador //= mcd
        self.__denominador //= mcd






if __name__ == "__main__":
    f = Fraccion(3, 5)
    f2 = Fraccion(6, 2)

    print("Mostramos la fracción f")
    print(f)
    print("----------------------------")
    print("Mostramos la fraccion f2: ")
    print(f2)
    print("------------------------------------------------")
    print("El resultado de la fraccion es: ")
    print(f.resultado())
    print("---------------------------------------------------")
    print(f"El resultado de multiplicar la fraccion {f} por la fracción {f2} es: ")
    f.multiplica_por_fraccion(f2)
    print("--------------------------------------------------")
    num = int(input("Intruduce un numero para mutiplicarlo por la fracción:"))
    print(f"El resultado de multipicar {f} por {num} es: ")
    f.multiplica_por_num(num)
    print("-----------------------------------------------------------------------")
    print(f"sumamos {f} + {f2}: ")
    f.suma_fracciones(f2)
    print(f)
    print("-----------------------------------------------")
    print(f"restamos {f} - {f2}")
    f.resta_fracciones(f2)
    print(f)
    print("-----------------------------------------------")
    print(f"La fracción {f} simplificada es: ")
    f.simplifica()
    print(f)
    print("--------------------------------------------------")
