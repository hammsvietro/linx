import queue
import time
import Product

''' PYTHON 3  '''
abacate = Product.Product(123,"abacate")
melancia = Product.Product(321,"melancia")
fila = queue.Queue()

print(abacate)
print(abacate.isInQueue(fila))
abacate.addToQueue(fila)
print(abacate.isInQueue(fila))
print(abacate)
