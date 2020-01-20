import os
import json


def createJson():

    os.chdir("..")
    os.chdir("test")

    json_data = []

    with open("input-dump") as f:
       for line in f:
           json_data.append(line) #AGORA A LISTA JSON_DATA TEM TODOS OS ELEMENTOS JSON

    parsed_json = []
    for line in json_data:
        parsed_json.append(json.loads(line))#OBJETO JSON MOTNADO


    f.close()
    
    os.chdir("..")
    os.chdir("src")

    return parsed_json


def imageStatus(image_name):
    if image_name % 5 == 0:
        return "Halt 404. There's no such image"
    return 'You got a 200'






def getImageName(product): #CRIA LISTA COM INDICE 0 = NOME DO ARQUQIVO E INDICE 1 CONTEM O OBJETO

    image = product['image']


    image = image.split('/')
    image = image[4]
    image = image.split('.')
    image = image[0]
    image_name = image

    image_status = imageStatus(int(image_name))

    image = []

    image.append(product)
    image.append(image_status)

    return image


def GetDump():
    dump = createJson()
    final = []
    for lines in dump:
        final.append(getImageName(lines))


    return final
