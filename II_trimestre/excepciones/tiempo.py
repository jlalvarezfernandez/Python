"""
Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:

t = Tiempo(1, 20, 30)

donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.

Crea métodos para:
    - Sumar y restar otro objeto de la clase Tiempo.
    - Sumar y restar segundos, minutos y/o horas.
    - Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

Realiza un programa de prueba para comprobar que la clase funciona bien.
"""
import sys


class Tiempo:

    def __init__(self, hora, minuto, segundo):
        """
        Constructor de la clase tiempo
        :param segundo:
        :param minuto:
        :param hora:
        """
        if not Tiempo.tiempo_correcto(hora, minuto, segundo):
            print(f"Tiempo introducido incorrecto", file=sys.stderr)
            exit(1)
        else:
            self.__hora = hora
            self.__minuto = minuto
            self.__segundo = segundo

    # Modificadores de los atributos
    @property
    def hora(self):
        return self.__hora

    @hora.setter
    def hora(self, value):
        self.__hora = value

    @property
    def minuto(self):
        return self.__minuto

    @minuto.setter
    def minuto(self, value):
        self.__minuto = value

    @property
    def segundo(self):
        return self.__segundo

    @segundo.setter
    def segundo(self, value):
        self.__segundo = value

    def __str__(self):
        """
        Salida formateada del tiempo
        :return: Devolver una cadena con el tiempo almacenado, de forma que si lo que
                    hay es (10 35 5) la cadena sea 10h 35m 5s.
        """
        return f"{self.__hora}h {self.__minuto}m {self.__segundo}s"

    def tiempo_segundos(self):
        """
        Método para pasar el objeto a segundos
        :return:
        """
        return self.hora * 3600 + self.minuto * 60 + self.segundo

    def conversor(self, tiempo_total):
        """
        Metodo para pasar los segundos a tiempo
        :param tiempo_segundos:
        :return:
        """
        self.__hora = tiempo_total // 3600
        self.__minuto = (tiempo_total % 3600) // 60
        self.__segundo = (tiempo_total % 3600) % 60

    def suma_tiempo(self, other):
        """
        Este método se suman dos tiempos
        :param other: Otro tiempo
        """
        tiempo_total = (Tiempo.tiempo_segundos(self)) + (other.hora * 3600 + other.minuto * 60 + other.segundo)
        Tiempo.conversor(self, tiempo_total)

    def resta_tiempo(self, other):
        """
        Este método se resta dos tiempos
        :param other: Otro tiempo
        """
        tiempo_total = (Tiempo.tiempo_segundos(self)) - (other.hora * 3600 + other.minuto * 60 + other.segundo)
        if tiempo_total < 0:
            print("El resultado del tiempo no puede ser menor que 0", file=sys.stderr)
            exit(888)
        else:
            Tiempo.conversor(self, tiempo_total)

    def suma_hora(self, horas):
        """
        Método que sumará horas a nuestro tiempo
        :param horas: horas a sumar
        """
        if horas < 0:
            print("Las horas no pueden ser negativas", file=sys.stderr)
            exit(1)
        else:
            self.__hora += horas

    def resta_hora(self, horas):
        """
        Método que restará horas al ol objeto
        :param horas: horas a restar
        """
        if horas < 0:
            print("Las horas no pueden ser negativas", file=sys.stderr)
            exit(1)
        else:
            self.__hora -= horas
            if self.__hora < 0:
                print("El resultado de horas no pueden ser negativas", file=sys.stderr)
                exit(2)

    def suma_minuto(self, minutos):
        """
        Método que sumará minutos al objeto tiempo
        :param minutos: minutos a restar
        """
        tiempo_total = Tiempo.tiempo_segundos(self) + minutos * 60
        Tiempo.conversor(self, tiempo_total)

    def resta_minuto(self, minutos):
        """
        Métodos que restará minutos al objeto tiempo
        :param minutos:
        """

        if minutos < 0:
            print("No puedes introducir una cantidad de minutos negativa", file=sys.stderr)
            exit(1)
        else:
            tiempo_total = Tiempo.tiempo_segundos(self) - minutos * 60
            Tiempo.conversor(self, tiempo_total)
            if tiempo_total < 0:
                print("el resultado no puede ser negativo al restarle minutos al tiempo", file=sys.stderr)
                exit(2)

    def suma_segundo(self, seg):
        """
        Método para sumar segundos a un objeto de la clase tiempo
        :param seg: segundos que se le restarán
        :return:
        """
        if seg < 0:
            print("No se le pueden sumar una cantidad de segundos negativos", file=sys.stderr)
            exit(1)
        else:
            tiempo_total = Tiempo.tiempo_segundos(self) + seg
            Tiempo.conversor(self, tiempo_total)

    def resta_segundo(self, seg):
        """
        Método para restarle una cantidad de segundos al objeto de la clase tiempo
        :param seg:
        :return:
        """
        if seg < 0:
            print("No se le pueden sumar una cantidad de segundos negativos", file=sys.stderr)
            exit(1)
        else:
            tiempo_total = Tiempo.tiempo_segundos(self) - seg
            Tiempo.conversor(self, tiempo_total)
            if tiempo_total < 0:
                print("La cantidad de segundos a restar no puede dar una cantidad negativas", file=sys.stderr)
                exit(2)

    @staticmethod
    def tiempo_correcto(hora, minuto, segundo):
        """
        Este método nos dirá si el tiempo es correcto o incorrecto
        :return: true o false
        """
        if not isinstance(hora, int) or not isinstance(minuto, int) or not isinstance(segundo, int):
            raise TypeError
            raise ValueError
        if hora < 0 or minuto < 0 or segundo < 0:
            return False
        if minuto > 59 or segundo > 59:
            return False
        else:
            return True


if __name__ == '__main__':



        try:

            print("CLASE TIEMPO")
            h = int(input("Introduce valor para Hora:\t\t"))
            m = int(input("Introduce valor para Minuto:\t"))
            s = int(input("Introduce valor para Segundo:\t"))

            # Creamos el objeto
            t = Tiempo(h,m,s)
            print(t)

        except TypeError:
            print("Error al introducir los datos")

        except ValueError:
            print("Tipo de dato incorrecto")

