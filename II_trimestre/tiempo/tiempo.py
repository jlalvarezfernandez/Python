'''
1. Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:

t = Tiempo(1, 20, 30)

donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.

Crea métodos para:

Sumar y restar otro objeto de la clase Tiempo.
Sumar y restar segundos, minutos y/o horas.
Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
Realiza un programa de prueba para comprobar que la clase funciona bien.
'''


class Tiempo:
    """
    Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:

    t = Tiempo(1, 20, 30)

    donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.
    """

    # creamos el constructor

    def __init__(self, horas, minutos, segundos):
        """
        Constructor de la clase
        lanza la excepción en caso de valores incorrectos
        :param horas: horas
        :param minutos: minutos
        :param segundos: segundos
        """
        assert horas >=0 and 0<= minutos<60 and 0<segundos<60 # evalua la condición, si es cierta no hace nada si no nos lanza excepción
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    # Propiedades
    # No hacemos el setter porque el programa no pide que cambiemos los valores del tiempo

    @property
    def horas(self):
        return self.__horas


    @property
    def minutos(self):
        return self.__minutos


    @property
    def segundos(self):
        return self.__minutos



    # Resto metodos

    def __str__(self):
        return f"{self.__horas}h {self.__minutos}m {self.__segundos}s"


    # sumar y restar horas

    def suma_horas(self,horas):
        """
        suma horas al objeto. si el resultado es negativo lanza una excepción
        :param horas:
        :return:
        """
        assert self.__horas + horas >= 0
        self.__horas += horas

    def resta_horas(self,horas):
        """
        resta horas al objeto. si el resultado es negativo lanza una excepción
        :param horas:
        :return:
        """
        assert self.__horas - horas >= 0
        # self.suma_horas(-horas)
        self.__horas -= horas

    def suma_minutos(self,minutos):
        """
        suma minutos al objeto, si las horas finales son negativas lanza una excepción
        :param minutos:
        :return:
        """

        seg = Tiempo.__segundos_total(self) + minutos * 60
        assert seg >= 0 # si los segundos son negativos el estado es inconsistente
        resultado = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos,self.__segundos = resultado.horas, resultado.minutos, resultado.segundos

    def resta_minutos(self, minutos):
        self.suma_minutos(-minutos)

    # sumar y restar segundos al objeto

    def suma_segundos(self,segundos):
        """
        suma minutos al objeto, si las horas finales son negativas lanza una excepción
        :param minutos:
        :return:
        """

        seg = Tiempo.__segundos_total(self) + segundos
        assert seg >= 0 # si los segundos son negativos el estado es inconsistente
        resultado = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos,self.__segundos = resultado.horas, resultado.minutos, resultado.segundos

    def resta_segundos(self, segundos):
        self.resta_segundos(-segundos)

    # sumar y restar otro objeto de la clase tiempo

    def suma(self, t):
        """
        suma otro objeto tiempo al objeto, si las horas finales son negativas lanza una excepción
        :param minutos:
        :return:
        """

        seg = Tiempo.__segundos_total(self) + Tiempo.__segundos_total(t)
        resultado = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = resultado.horas, resultado.minutos, resultado.segundos

    def resta(self, t):
        seg = Tiempo.__segundos_total(self) - Tiempo.__segundos_total(t)
        assert seg >= 0  # si los segundos son negativos el estado es inconsistente
        resultado = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = resultado.horas, resultado.minutos, resultado.segundos

    # Metodos estaticos

    @staticmethod  # metodo estatico y privado
    def __segundos_total(t):
        return t.horas * 3600 + t.minutos*60 + t.segundos

    @staticmethod
    def __segundos_a_tiempo(s):
        horas = s // 3600
        s = s % 3600
        minutos = s // 60
        segundos = s % 60
        return Tiempo(horas, minutos, segundos)


if __name__== "__main__":

    t1 = Tiempo(10, 10, 10)
    t2 = Tiempo(3, 3, 3)

    print("t1: ", t1)
    h = int(input(f"Horas a sumar a {t1}: "))
    t1.suma_horas(h)
    print(f"Ahora t1 es {t1} ")
    print("-----------------------------------")
    h = int(input(f"Horas a restar a {t1}: "))
    t1.resta_horas(h)
    print(f"Ahora t1 es {t1} ")
    print("------------------------------------")
    m = int(input(f"Minutos a sumar a {t1}: "))
    t1.suma_minutos(m)
    print(f"Ahora t1 es {t1}")
    print("------------------------------------")
    m = int(input(f"Minutos a restar a {t1}: "))
    t1.resta_minutos(m)
    print(f"Ahora t1 es {t1}")
    print("------------------------------------")
    s = int(input(f"Segundos a sumar a {t1}: "))
    t1.suma_segundos(s)
    print(f"Ahora t1 es {t1}")
    print("------------------------------------")
    '''
    s = int(input(f"Segundos a restar a {t1}: "))
    t1.resta_segundos(s)
    print(f"Ahora t1 es {t1}")
    '''
    print("-------------------------------------")
    print(f"Sumamos a {t1} el tiempo {t2}")
    t1.suma(t2)
    print(f"Ahora t1 es {t1}")
    print("-------------------------------------")
    print(f"Restamos a {t1} el tiempo {t2}")
    t1.resta(t2)
    print(f"Ahora t1 es {t1}")








