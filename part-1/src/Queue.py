class Queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def isEmpty(self):
        if self.size > 0:
            return False
        return True

    def __str__(self):
        return str(self.__dict__)

    def getSize(self):
        return self.size

    def push(self,element):

        self.queue.append(element)
        self.size += 1
        return True

    def pop(self):

        if(self.isEmpty()):
            print("Queue is empty")
            return None
        self.size -= 1
        return self.queue.pop(0)
