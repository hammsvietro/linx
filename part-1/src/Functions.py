import json
import Queue
import Product
import time




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
    if not isinstance(queue,Queue.Queue): #VERIFICAR SE NAO SAO CLASSES DIFERENTES
        return NotImplemented
    print("fazendo upload de ",product)
    if not product.isInQueue(queue):
        product.startTime() # ADD VARIAVEL DE INICIO DE CRONOMETRO NO OBJETO
        queue.push(product)
        
        print("200 OK")
        return True
    else:
        print("403 Forbidden")

def queueAdder(parsed_json,queue):
    i = 0
    for lines in parsed_json:
        id = parsed_json[i]['id']
        name = parsed_json[i]['name']
        product = Product.Product(id,name)
        addToQueue(product,queue)
        time.sleep(1)
        i+=1
    return True

def queueCleaner(queue):
    while True:
        if queue.getSize() > 0:
            print("oi")
            timeInQueue = queue.queue[0].timeInQueue()
            print(timeInQueue)
            if timeInQueue >= 2:
                print(popado)
                queue.pop()
