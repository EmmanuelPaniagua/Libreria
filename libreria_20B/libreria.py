from .libro import Libro
import json

class Libreria:
    def __init__(self):
        self.__libros = []
    
    def agregar_final(self, libro:Libro):
        self.__libros.append(libro)

    def agregar_inicio(self, libro:Libro):
        self.__libros.insert(0, libro)

    def mostrar(self):
        for libro in self.__libros:
            print(libro)

    def __str__(self):
        return "".join(
            str(libro) + '\n' for libro in self.__libros
        )

    def guardar(self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [libro.to_dict() for libro in self.__libros]
                print(lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

        


#l01 = Libro(titulo="Programación", autor="Deitel", publicado=2020, editorial="Pearson")
#l02 = Libro("Python", "Guido", "2010", "Planeta")
#libreria = Libreria()
#libreria.agregar_final(l01)
#libreria.agregar_inicio(l02)
#libreria.agregar_inicio(l01)
#libreria.mostrar()