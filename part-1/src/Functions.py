import json
import Queue
import Product
import time
import multiprocessing
import random



def addProducts(file):
    json_data = []

    with open(file) as f:
       for line in f:
           json_data.append(line) #AGORA A LISTA JSON_DATA TEM TODOS OS ELEMENTOS JSON

    parsed_json = []
    for line in json_data:
        parsed_json.append(json.loads(line))#OBJETO JSON MOTNADO


    f.close()

    return parsed_json





def queueAdder(parsed_json,queue,lock):

    i = 0
    for lines in parsed_json:
        time.sleep(random.uniform(3.5,4.3))
        id = parsed_json[i]['id']
        name = parsed_json[i]['name']
        product = Product.Product(id,name)
        lock.acquire()



        print("#",time.asctime())
        print("Produto: ",product)

        temp_queue = Queue.Queue()

        time.sleep(0.02)
        while queue.empty() is False: #Troca multiprocessing.queue para queue implementada para poder acessar todos os elementos da fila
            temp_queue.push(queue.get())



        if not product.isInQueue(temp_queue):
            product.timeStarter() # ADD VARIAVEL DE INICIO DE CRONOMETRO NO OBJETO
            temp_queue.push(product)



        while temp_queue.isEmpty() is False:
            queue.put(temp_queue.pop())
        print("")



        lock.release()
        i+=1

    return True


def queueCleaner(queue,lock):
    while True:

        lock.acquire()
        temp_queue = Queue.Queue()

        while queue.empty() is False:
            temp_queue.push(queue.get())

        if temp_queue.getSize() > 0:
            timeInQueue = temp_queue.firstTime()


            if timeInQueue >= 600:
                temp_queue.pop()


        while temp_queue.isEmpty() is not True:
                queue.put(temp_queue.pop())

        lock.release()
