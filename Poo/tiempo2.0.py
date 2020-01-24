'''
1. Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la forma:

t = Tiempo(1, 20, 30)

donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.

Crea métodos para:

Sumar y restar otro objeto de la clase Tiempo.
Sumar y restar segundos, minutos y/o horas.
-Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.
-Realiza un programa de prueba para comprobar que la clase funciona bien.

'''

# Creamos la clase tiempo

class Tiempo2:

    # Creamos el constructor

    def __init__(self,horas,minutos,segundos):
        """
        :param horas: horas
        :param minutos: minutos
        :param segundos: segundos
        """
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    # Creamos los setters y los getters

    # getter horas

    @property
    def horas(self):
        return self.__horas

    # setter horas

    @horas.setter
    def horas(self, value):
        self.__horas = value

    # getter minutos

    @property
    def minutos(self):
        return self.__minutos

    # setter minutos

    @minutos.setter
    def minutos(self, value):
        self.__minutos = value

    # getter segundos

    @property
    def segundos(self):
        return self.__segundos

    # setter segundos

    @segundos.setter
    def segundos(self, value):
        self.__segundos = value


    # Sobrecarga de datos para mostrar salida formateada

    def __str__(self):
        return f"{self.__horas}h {self.__minutos}m {self.__segundos}s"

    # metodo para sumar otro objeto tiempo

    def sumar_tiempo(self, otro_tiempo):
        tiempo_total = self.__horas * 3600 + self.__minutos * 60 + self.__segundos + otro_tiempo.horas * 3600 + otro_tiempo.minutos * 60 + otro_tiempo.segundos
        self.convertidor(tiempo_total)

    # metodo apra restar otro objeto tiempo
    def restar_tiempo(self, otro_tiempo):
        tiempo_total = self.__horas * 3600 + self.__minutos * 60 + self.__segundos - (otro_tiempo.horas * 3600 + otro_tiempo.minutos * 60 + otro_tiempo.segundos)
        self.convertidor(tiempo_total)

    # metodo para sumar horas

    def suma_horas(self,horas):
        self.__horas += horas

    # metodo apra restar horas

    def restar_horas(self,horas):
        self.__horas -= horas

    # metodo para sumar minutos

    def suma_minutos(self,minutos):
        tiempo_total = self.__horas * 3600 + self.__minutos * 60 + self.__segundos + minutos *60
        self.convertidor(tiempo_total)

    # metodo para restar minutos

    def resta_minutos(self,minutos):
        tiempo_total = self.__horas * 3600 + self.__minutos * 60 + self.__segundos - minutos * 60
        self.convertidor(tiempo_total)

    # metodo sumar segundos

    def sumar_segundos(self,segundos):

        if segundos >= 0:
            tiempo_total = self.__horas * 3600 + self.__minutos * 60 + self.__segundos + segundos
            self.convertidor(tiempo_total)
        else:
            print("Parámetro erroneo")

    # metodo restar segundos

    def restar_segundos(self,segundos):
        if segundos >=0:
            tiempo_total = self.__horas * 3600 + self.__minutos * 60 + self.__segundos - segundos
            self.convertidor(tiempo_total)
        else:
            print("Parametro erroneo")




    # metodo conversor para pasar a segundos cualquier cantidad de tiempo


    def convertidor(self, tiempo_total):
        self.__segundos = tiempo_total % 60
        self.__minutos = (tiempo_total % 3600) // 60
        self.__horas = tiempo_total // 3600




#PRUEBAS

if __name__ == "__main__":

    # creamos los objetos
    t1 = Tiempo2(3, 3, 3)
    t2 = Tiempo2(2, 2, 2)

    print("Mostramos t1 y t2")
    print("t1: ",t1)
    print("t2: ",t2)
    print("------------------------------")
    print("Sumamos t2 a t1")
    t1.sumar_tiempo(t2)
    print(t1)
    print("--------------------------------")
    print("Restamos t2 a t1")
    t1.restar_tiempo(t2)
    print(t1)
    print("--------------------------------")
    print("Le sumamos 7h a t1")
    t1.suma_horas(7)
    print(t1)
    print("----------------------------------")
    print("Le restamos 5h a t1")
    t1.restar_horas(5)
    print(t1)
    print("---------------------------")
    print("Le sumamos 70 min a t1")
    t1.suma_minutos(70)
    print(t1)
    print("-------------------------------")
    print("Le restamos 25 min a t1")
    t1.resta_minutos(25)
    print(t1)
    print("-----------------------------")
    print("Le sumamos 70 segundos a t1")
    t1.sumar_segundos(70)
    print(t1)
    print("-----------------------------")
    print("Le restamos 100 segundos a t1")
    t1.restar_segundos(100)
    print(t1)



