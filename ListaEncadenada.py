from Nodo import Nodo
class ListaEncadenada:
    def __init__(self):
        self.head = None

    # HEAD -> BEN
    # BEN -> NEXT CARLOS
    # CARLOS -> NEXT DIANA
    # DIANA -> NEXT NONE

    # INSERTANODO (EDUARDO)

    # aux = BEN
    # BEN.next = CARLOS

    # aux = BEN.next -> CARLOS
    # CARLOS.next = DIANA

    # aux = CARLOS.next -> DIANA
    # DIANA.next = NONE

    # DIANA.next = EDUARDO
    
    def insertaNodo(self, nuevoNodo):
        if self.head == None:
            self.head = nuevoNodo
        else :
            aux = self.head 
            while aux.next != None:
                aux = aux.next
            aux.next = nuevoNodo
    
    def imprimeLista(self):
        aux = self.head
        while aux != None:
            print(aux.nombre, aux.apellido)
            aux = aux.next

    
