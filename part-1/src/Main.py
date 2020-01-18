import queue
import time
import Product
import json

''' PYTHON 3  '''


fila = queue.queue()

json_data = []

with open('test.json') as f:
   for line in f:
       json_data.append(line)

parsed_json = []
i = 0
for line in json_data:
    #time.sleep(1)
    parsed_json.append(json.loads(line))

produto = Product.Product(parsed_json[0]['id'],parsed_json[0]['name'])
produto.addToQueue(fila)
print(produto)
