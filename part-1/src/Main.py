import Product
import Queue
import Functions
import time
import json
import multiprocessing

''' PYTHON 3  '''



queue = multiprocessing.Queue()
lock = multiprocessing.Lock()
done = multiprocessing.Value("i",0)
parsed_json = Functions.addProducts("test.json")



p1 = multiprocessing.Process(target=Functions.queueAdder,args=(parsed_json,queue,lock,done,))
p2 = multiprocessing.Process(target=Functions.queueCleaner,args=(queue,lock,done,))
p1.start()
p2.start()
