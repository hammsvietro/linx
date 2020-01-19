import time
import Queue

class Product():

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def timeStarter(self):
        self.startTime = time.time()


    #PRINT OBJETO
    def __str__(self):
        return str(self.__dict__)

    #COMPARAR OBJETOS IGUAIS
    def __eq__(self,other):
        if not isinstance(other, Product): #VERIFICAR SE NAO SAO CLASSES DIFERENTES
            return NotImplemented

        return self.id == other.id and self.name == other.name

    def isInQueue(self,queue):
        if not isinstance(queue,Queue.Queue): #VERIFICAR SE NAO SAO CLASSES DIFERENTES
            return NotImplemented


        for i in queue.queue:

            if i.id == self.id and i.name == self.name:
                print("403 Forbidden: wait ",600 - i.timeInQueue() ," seconds to do this")
                return True


        print("200 OK")
        return False

    def timeInQueue(self):
        totalTime = time.time() - self.startTime
        return int(totalTime)
