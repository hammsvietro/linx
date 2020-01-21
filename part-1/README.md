# Pedro Henrique Hamms Vietro



### Part-1

Resolvi implementar o desafio 1 com multiprocessing.

O primeiro core lê o arquivo json de produtos, que será gerado aleatoriamente, e checa se ele existe em uma fila, se ele não existir, é retornado o codigo 200 OK que permite a requisição, caso contrário, se ele já estiver na lista, significa que nos ultimos 10 minutos, o mesmo produto ja foi inserido, então é retornado o código 403 Forbidden, negando a requisição.

O segundo core controla a fila, assim que o primeiro elemento estiver há 10 minutos na fila, ele é removido, permitindo novamente a requisição do produto.

o multriprocessing foi implementado com multiprocessing.queue e multiprocessing.lock, a fila e o semáforo já implementados pela biblioteca permitem segurança ao manipular a mesma memória sem erros, podendo receber uma quantidade "infinita" de requisições sem ocorrer problemas.


## Como Rodar

O primeiro passo é entrar na pasta test/ e rodar o scrpit Json_Generator.py com Python 3 este criará um arquivo test.json com 140 produtos diferentes, porem vai repetí-los 3 vezes durante a lista ou seja, 420 objetos json.

Agora só basta rodar o arquivo Main.py com Python 3 na pasta src/

A main irá acessar o test.json gerado aleatóriamente e ira inserir um produto entre 3.5 a 4.3 segundos, isso garantirá que na segunda iteração de requisição que todos eles retornarão 403 Forbidden (ou quase se random.unifrom() gerar sempre ~4.3 passará mais de 10 minutos até a segunda iteração) mas a probabilidade é quase nula.

Na terceira e última iteração será retornado 200 OK pois nao existirao mais requisições em "cooldown"
