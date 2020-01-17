import Produto
import time



class Produto_Para_Queue(Produto.Produto):
    def __init__(self, id, name, put_time):
        super().__init__(id,name)
        self.put_time = put_time

    def __str__(self):#PARA PRINTAR
        return str(self.__dict__)
"""
    def on_queue(self,other):#COMPARAR COM PRODUTO PARA CHECAR NA QUEUE
        if not isinstance(other, Produto): #VERIFICAR SE CLASSE EH PRODUTO
            return "Nao eh instancia de produto"
        return self.id == other.id and self.name == other.name
"""


if __name__ == '__main__':
    x = Produto_Para_Queue(123,"abacate",time.time

    print(abacate)
