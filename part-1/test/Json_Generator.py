# {"id": "", "name": ""}
import random

f = open("test.json","a")

items = ['cadeira','mesa','computador','notebook','lampada','luminaria','copo','caneca','microfone','guitarra','caderno','caneta','post-it','celular','processador','hdd','placa de video','monitos','mouse','teclado','fonte','ssd','camiseta','casaco','tenis','bermuda','chinelo','meia','arroz','feijao','ovo','agua','refrigerante','suco','banana','manga','melancia','abacate','morango','chocolate','nozes','biscoito']
test = ""
repeated_numbers = []
size = len(items)

for i in range(140):

    newId = False
    id = 0

    while True:
        if newId == True:
            repeated_numbers.append(id)
            break


        id = random.randint(100,1000)

        newId = True
        for j in repeated_numbers:
            if j == id:
                newId = False


    random_json = '{"id": "%i", "name": "%s"}\n' % (id,items[random.randint(0,size-1)])
    test+=random_json

test*=3
print(140*3,"produtos criados em test.json")
f.write(test)




f.close()
