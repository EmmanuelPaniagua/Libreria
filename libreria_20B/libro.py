class Libro:
    def __init__(self, 
                titulo="", autor="", 
                publicado=0, editorial=""):
        self.__titulo = titulo
        self.__autor = autor
        self.__publicado = publicado
        self.__editorial = editorial
    
    def __str__(self):
        return (
            'Título: ' + self.__titulo + '\n' +
            'Autor: ' + self.__autor + '\n' +
            'Publicado: ' + str(self.__publicado) + '\n' +
            'Editorial: ' + self.__editorial + '\n'
        )

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor
    
    @property
    def publicado(self):
        return self.__publicado

    @property
    def editorial(self):
        return self.__editorial
    
    def to_dict(self):
        return {
            "titulo": self.__titulo,
            "autor": self.__autor,
            "publicado": self.__publicado,
            "editorial": self.__editorial
        }

# l01 = Libro(titulo="Programación", autor="Deitel", publicado=2020, editorial="Pearson")
# print(l01)
# l02 = Libro("Python", "Guido", "2010", "Planeta")
# print(l02)

