class queue:
    def __init__(self):
        self.queue = []
        self.size = 0

    def isEmpty(self):

        if self.size == 0:
            return True
        return False

    def size(self):

        return self.size()

    def push(self,element):

        self.queue.append(element)
        return True

    def pop(self):

        if(self.isEmpty()):
            print("Queue is empty")
            return None
        return self.pop(0)
