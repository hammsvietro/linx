import Product
import Queue
import Functions
import time
import json
import multiprocessing
import os

''' PYTHON 3  '''


os.chdir('..')
os.chdir('test')

queue = multiprocessing.Queue()
lock = multiprocessing.Lock()


parsed_json = Functions.addProducts("test.json")



p1 = multiprocessing.Process(target=Functions.queueAdder,args=(parsed_json,queue,lock,))
p2 = multiprocessing.Process(target=Functions.queueCleaner,args=(queue,lock,))

p1.start()
p2.start()

p1.join()

p1.terminate()
p2.terminate()
