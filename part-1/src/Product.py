import time
import Queue

class Product():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def startTime(self):
        self.startTime = time.time()


    #PRINT OBJETO
    def __str__(self):
        return str(self.__dict__)

    #COMPARAR OBJETOS IGUAIS
    def __eq__(self,other):
        if not isinstance(other, Product): #VERIFICAR SE NAO SAO CLASSES DIFERENTES
            return NotImplemented

        return self.id == other.id and self.name == other.name

    def isInQueue(self,fila):
        if not isinstance(fila,Queue.Queue): #VERIFICAR SE NAO SAO CLASSES DIFERENTES
            return NotImplemented

        for i in fila.queue:
            if i == self:
                return True

            return False

    def timeInQueue():
        return int(time.time()-self.startTime)
