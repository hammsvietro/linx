import Queue
import time
import Product
import json
import Functions
import multiprocessing

''' PYTHON 3  '''



queue = Queue.Queue()#Cria objeto fila
parsed_json = Functions.addProducts("test.json")

p1 = multiprocessing.Process(target=Functions.queueAdder,args=(parsed_json,queue,))
p2 = multiprocessing.Process(target=Functions.queueCleaner,args=(queue,))
p1.start()
p2.start()

p1.join()
