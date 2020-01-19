import json
import Queue
import Product
import time
import multiprocessing





def addProducts(file):
    json_data = []

    with open('test.json') as f:
       for line in f:
           json_data.append(line) #AGORA A LISTA JSON_DATA TEM TODOS OS ELEMENTOS JSON

    parsed_json = []
    for line in json_data:
        #time.sleep(1)
        parsed_json.append(json.loads(line))#OBJETO JSON MOTNADO

    return parsed_json

def addToQueue(product, queue):

    print("fazendo upload de ",product)

    temp_queue = Queue.Queue()

    while queue.empty() is False: #Troca multiprocessing.queue para queue implementada para poder acessar todos os elementos da fila
        temp_queue.push(queue.get())

    #print("queue substituida! p/ temp")
    if not product.isInQueue(temp_queue):
        product.startTime() # ADD VARIAVEL DE INICIO DE CRONOMETRO NO OBJETO
        temp_queue.push(product)

        print("200 OK")

    else:
        print("403 Forbidden")

    while temp_queue.isEmpty() is False:
        queue.put(temp_queue.pop())

    #print("voltou para multiprocessing.queue!!!")

def queueAdder(parsed_json,queue,lock,done):

    i = 0
    for lines in parsed_json:
        id = parsed_json[i]['id']
        name = parsed_json[i]['name']
        product = Product.Product(id,name)
        lock.acquire()
        addToQueue(product,queue)
        lock.release()
        time.sleep(2)
        i+=1

    done = 1
    if(done == 1):
        print("deu bom")

def queueCleaner(queue,lock,done):
    while True:

        temp_queue = Queue.Queue()
        lock.acquire()

        while queue.empty() is False:
            temp_queue.push(queue.get())

        if temp_queue.getSize() > 0:
            timeInQueue = temp_queue.queue[0].timeInQueue()

            if timeInQueue >= 6:
                print("POPADASSO")
                temp_queue.pop()

        while temp_queue.isEmpty() is not True:
                queue.put(temp_queue.pop())

        lock.release()
