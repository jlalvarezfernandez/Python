"""
Colección de funciones para manejar fechas en cadenas de caracteres.
El formato de la cadena es: AAAAMMDD.
Ejemplo: El 15 de diciembre de 2019 sería: "20191215"
Colección de funciones:
    1. fecha_correcta: dice si la fecha que se pasa como parámetro es correcta.
    2. fecha_mas_1dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.
    3. fecha_mas_ndias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.
    4. fecha_menos_1dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.
    5. fecha_menos_ndias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.
    6. es_bisiesto: dice si la fecha que se pasa como parámetro es bisiesto.
    7. compara_fechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
       segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.
    8. fecha_formateada: recibe un fecha y devuelve una cadena con el formato:
        DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")
    9. año, mes, dia, nombre_mes: recibe un fecha y devuelve esos valores.
Hay un script para hacer pruebas: prueba_fecha.py.


"""


class Fecha_incorrecta(Exception):
    """
    :exception
    """

    def __init__(self, mensaje_error):
        Exception.__init__(self)
        self.__mensaje_error = mensaje_error


class Fecha:

    def __init__(self, dia, mes, anio):
        """
        Creamos el constructor
        :param dia:
        :param mes:
        :param anio:
        """

        if not Fecha.fecha_correcta(dia, mes, anio):
            raise Fecha_incorrecta("Error al introducir los datos")
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio

    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        if not Fecha.fecha_correcta(value, self.__mes, self.__anio):
            raise Fecha_incorrecta(f"Día asignado {value} incorrecto")
        self.dia = value

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        if not Fecha.fecha_correcta(self.__dia, value, self.__anio):
            raise Fecha_incorrecta(f"Mes asignado {value} incorrecto")
        self.__mes = value

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, value):
        if not Fecha.fecha_correcta(self.__dia, self.__mes, value):
            raise Fecha_incorrecta(f"Año asignado {value} incorrecto")
        self.__anio = value

    @staticmethod
    def fecha_correcta(dia, mes, anio):
        """
        Método para validar la fecha
        :return:
        """

        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(anio, int):
            raise ValueError
        if anio < 0:
            return False
        if mes < 1 or mes > 12:
            return False
        if dia < 1 or dia > 31:
            return False
        return 0 < dia and dia <= Fecha.dias_anio(mes, anio)

    @staticmethod
    def dias_anio(mes, anio):
        """
        Calcula el último día de cada mes del año, incluyendo si es bisiesto
        :return:
        """
        dias_anio = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if Fecha.es_bisiesto(anio):
            dias_anio[1] = 29
        return dias_anio[mes - 1]

    @staticmethod
    def es_bisiesto(anio):
        """
        Método para saber si un año es bisiesto.
        :return: devuelve verdadero si es bisiesto.
        """
        if not anio % 4 == 0 and not anio % 400 == 0:
            return False
        return True

    def fecha_mas_1dia(self):
        """
        Método para sumar 1 dia a la fecha.
        :return: devuelve la fecha más 1 día.
        """
        dia = self.__dia + 1
        mes = self.__mes
        anio = self.__anio

        if dia > Fecha.dias_anio(mes, anio):
            dia = 1
            mes += 1
            if mes > 12:  # nos pasamos de diciembre, año siguiente
                mes = 1
                anio += 1

        return Fecha(dia, mes, anio)

    def fecha_mas_ndia(self, dias):
        """
        Método para sumar n dias a la fecha
        :return: devuelve la fecha más n días
        """
        self.__dia += dias
        while self.__dia > Fecha.dias_anio(mes, anio):
            self.__dia -= Fecha.dias_anio(mes, anio)
            self.__mes += 1
            if self.__mes > 12:  # nos pasamos de diciembre, año siguiente
                self.mes = 1
                self.__anio += 1

        return Fecha(self.__dia, self.__mes, self.__anio)

    def fecha_menos_ndia(self, dias):
        """
        Método para restas n dias a la fecha
        :return: devuelve la fecha menos n días
        """

        self.__dia -= dias
        while self.__dia < 1:
            self.__dia += Fecha.dias_anio(mes, anio)
            self.__mes -= 1
            if self.__mes < 1:  # nos pasamos de diciembre, año siguiente
                self.mes = 12
                self.__anio -= 1

        return Fecha(self.__dia, self.__mes, self.__anio)



    def fecha_menos_1dia(self):
        """
        Este método calcula la fecha menos un día
        :return: devuelve la fecha menos un día
        """

        self.__dia -= 1

        if self.__dia == 0:
            self.__mes -= 1
            if self.__mes == 0:
                self.__mes = 12
                self.__anio -= 1
            dia = Fecha.dias_anio(mes, anio)
        return Fecha(self.__dia, self.__mes, self.__anio)


    # sobrecarga de los operadores para comparar las fechas
    def __eq__(self, other):
        """
        Método igual que.
        :param other:
        :return: Devolverá verdadero si la fecha es igual a otra
        """
        return self.__dia == other.__dia and self.__mes == other.__mes and self.__anio == other.__anio

    def __gt__(self, other):
        """
        Método mayor que.
        :param other:
        :return: Devolverá verdadero si la fecha es mayor que otra.
        """
        if self.__anio != other.anio:
            return self.__anio > other.anio
        if self.__mes != other.mes:
            return self.__mes > other.mes
        if self.__dia != other.dia:
            return self.__dia > other.dia

    def __ge__(self, other):
        """
        Método mayor o igual que.
        :param other:
        :return: Devolverá verdadero si la fecha es mayor o igual que otra.
        """
        if self.__anio != other.anio:
            return self.__anio >= other.anio
        elif self.__mes != other.mes:
            return self.__mes >= other.mes
        else:
            return self.__dia >= other.dia

    def __str__(self):
        """
        metodo str para crear la salida formateada
        :return:
        """
        return f"{self.__dia} de {self.nombre_mes()} de {self.__anio}"

    def nombre_mes(self):
        """
        Método para mostar el nombre del mes
        :return:
        """
        meses = (
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre",
        "Diciembre")
        return meses[self.__mes - 1]


if __name__ == '__main__':

    try:
        dia = int(input("Introduce el dia: "))
        mes = int(input("Introduce el mes: "))
        anio = int(input("Introduce el anio: "))

        f1 = Fecha(dia, mes, anio)
        f2 = Fecha(31, 3, 2020)
    except ValueError:
        print("Tipo de datos introducidos erroneos")

    except Fecha_incorrecta:
        print("Error al introducir la fecha")



    print(f"Fecha: ", f1)
    #print("¿La fecha introducida es correcta? ", f1.fecha_correcta())
    print("Fecha mas un dia es: ", f1.fecha_mas_1dia())
    print("Fecha menos un dia es: ", f1.fecha_menos_1dia())
    print("Fecha mas 10 dias es: ", f1.fecha_mas_ndia(10))
    print("Fecha menos 10 dias es: ", f1.fecha_menos_ndia(10))
    print(f"comparamos fechas, ¿Son iguales las fechas {f1} y {f2}:", f1 == f2)
    print(f"comparamos fechas, ¿Es mayor la fecha {f1} que {f2}:", f1 > f2)
    print(f"comparamos fechas, ¿Es menor la fecha {f1} que {f2}:", f1 < f2)