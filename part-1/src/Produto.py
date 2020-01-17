class Produto():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    #PRINT OBJETO
    def __str__(self):
        return str(self.__dict__)

    #COMPARAR OBJETOS IGUAIS
    def __eq__(self,other):
        if not isinstance(other, Produto): #VERIFICAR SE NAO SAO CLASSES DIFERENTES
            return NotImplemented

        return self.id == other.id and self.name == other.name
