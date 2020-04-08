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
import pickle
import sys


class DimensionRectanguloError(Exception):

    """
    :exception que se lanza cuando o la base o la altura exceden de los limites establecidos
    """

    def __init__(self, mensaje_error):
        Exception.__init__(self)
        self.mensaje_error = mensaje_error



class Rectangulo:

    # definimos constantes
    LADO_MAXIMO = 10
    NUM_RECTANGULOS = 0

    # creamos el constructor


    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        Rectangulo.NUM_RECTANGULOS += 1


    # esto sería el getter (observador) en java
    @property
    def base(self):
        return self.__base

    # esto sería el setter (modificador) en java
    @base.setter
    def base(self, base):
        Rectangulo.__comprueba_lado(base)
        self.__base = base


    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, altura):
        Rectangulo.__comprueba_lado(altura)
        self.__altura = altura

    # Creacion de los métodos

    def __str__(self):
        """
        Método para mostrar el rectángulo
        :return:
        """
        str = ""
        for i in range(self.altura):
            str += "*" * self.base
            str += "\n"
        return str


    def perimetro(self):
        """
        Método para calcular el perimetro
        :return:
        """
        return  2 * (self.__base + self.altura)

    def area(self):
        """
        Método para calcular el área
        :return:
        """
        return self.__base * self.__altura

    def es_gemelo(self, otro_rectangulo):
        """
        Método para saber si los rectángulos son iguales
        Para saber si son gemelos comparamos la base y altura de uno con el otro
        :param otro_rectangulo:
        :return: true o false
        """
        return self.__altura == otro_rectangulo.altura and self.__base == otro_rectangulo.base

    def compara_area(self,otro_rectangulo):
        """
        Para comparar 2 rectangulos debemos restar sus áreas
        :param otro_rectangulo:
        :return:
        """
        return self.area() - otro_rectangulo.area()


    @staticmethod
    def rectangulos_creados():
        """
        Método para saber el número de rectangulos creados
        para ello declaramos una constante y en el constructor la iniciamos y allí será donde se vayan sumando
        :return: numero de rectángulos
        """
        return Rectangulo.NUM_RECTANGULOS
    
    @staticmethod
    def __comprueba_lado(value):
        if not isinstance(value, int):
            raise TypeError
        elif value < 0 or value > Rectangulo.LADO_MAXIMO:
            raise DimensionRectanguloError(f"{value} no está dentro de las dimensiones.")

    # sobrecarda de operadores

    def __mul__(self, other):
        """
        sobrecarga para el operador multiplicacion
        :param other:
        :return:
        """
        assert isinstance(other, int) and other > 0  # operando correcto
        assert self.__base * other <= Rectangulo.LADO_MAXIMO or self.__altura * other <= Rectangulo.LADO_MAXIMO
        if self.__base * other <= Rectangulo.LADO_MAXIMO:
            return Rectangulo(self.__base * other, self.__altura)
        else:
            return Rectangulo(self.base, self.altura * other)
        return self.area()*other()
    def __rmul__(self, other):
        """
        sobrecarga cuando para el operador multiplicacion cambiando el orden
        :param other:
        :return:
        """
        return other() * self.area()

    def __lt__(self, other):
        """
        sobrecarga para cuando el rectangulo es menor que otro
        :param other:
        :return:
        """
        assert isinstance(other, Rectangulo)
        return self.area() < other()

    def __le__(self, other):
        """
        sobrecarga cuando el rectangulo es menor o igual a otro
        :param other:
        :return:
        """
        assert isinstance(other, Rectangulo)
        return self.area() <= other()
    def __eq__(self, other):
        """
        sobrecarga cuando los rectangulos son iguales
        :param other:
        :return:
        """
        assert isinstance(other, Rectangulo)
        return self.area() == other()





    # Tenga un método (guardar) para guardar en un fichero el objeto actual usando pickle.
    def guarda(self, fichero):
        """
        método (guardar) para guardar en un fichero el objeto actual usando pickle.
        :param fichero:
        :return:
        """
        try:
            fichero = open(fichero, "wb")
            pickle.dump(self,fichero)
            fichero.close()
            return True
        except:
            print("No se ha podido guardar el fichero.", fichero,file = sys.stderr)
            return False

    #Tenga un método (recuperar) para recuperar un objeto Rectángulo almacenado en un fichero usando pickle.
    def recupera(self, fichero):
        try:
            fichero = open(fichero,"rb")
            r = pickle.load(fichero)
            fichero.close()
            # asignamos el estado al objeto actual
            self.base = r.base
            self.altura = r.altura
            return True
        except:
            print("No se ha podido recuperar el fichero.", fichero, file = sys.stderr)
            return False


if __name__ == '__main__':


    # creamos un objeto de la clase rectangulo

    try:
        b1 = int(input("base: "))
        h1 = int(input("altura: "))
        r1 = Rectangulo(b1, h1)

        b2 = int(input("base: "))
        h2 = int(input("altura: "))
        r2 = Rectangulo(b2, h2)
    except ValueError:
        print("Solo puede poner valores enteros entre 1 y 10.")
        exit(1)
    except DimensionRectanguloError as exc:
        print("Dimensiones incorrectas.")
        print("Mensaje error:", exc.mensaje_error)
        exit(2)




    print("Test para comprobar lo métodos de la clase Rectángulo")
    print("Mostramos r1")
    print(r1)
    print("-----------------------------------------------------")
    print("Mostramos r2")
    print(r2)
    print("-----------------------------------------------------")
    print("Perímetro del rectángulo r1:", r1.perimetro())
    print("Perímetro del rectángulo r2:", r2.perimetro())
    print("-----------------------------------------------------")
    print("Área de r1: ",r1.area())
    print("Área de r2: ",r2.area())
    print("-----------------------------------------------------")
    print("¿Son los dos rectángulos iguales? ", r1.es_gemelo(r2))
    print("-----------------------------------------------------")
    print("Resultado de comparar el área de los rectángulos: ", r1.compara_area(r2))
    print("-----------------------------------------------------")
    print("¿Cuantos rectángulos tenemos? ", Rectangulo.NUM_RECTANGULOS)
    print("-----------------------------------------------------")
    print("Guarda fichero: ",r1.guarda("rectangulo.bin"))
    print("-----------------------------------------------------")
    print("Recuperamos fichero: ",r1.recupera("rectangulo.bin"))




