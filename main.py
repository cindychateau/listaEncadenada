from Nodo import Nodo
from ListaEncadenada import ListaEncadenada

listaPersonas = ListaEncadenada()

persona1 = Nodo("Alex", "Mtz", 1)
persona2 = Nodo("Ben", "Frank", 2)
persona3 = Nodo("Carlos", "Hdz", 3)
persona4 = Nodo("Diana", "Montoya", 4)

listaPersonas.insertaNodo(persona1) #Alex es el head
listaPersonas.insertaNodo(persona2) #Alex.next = Ben; Ben.next = None
listaPersonas.insertaNodo(persona3) #Alex.next = Ben; Ben.next = Carlos; Carlos.next = None
listaPersonas.insertaNodo(persona4) #Alex.next = Ben; Ben.next = Carlos; Carlos.next = Diana; Diana.next = None

listaPersonas.imprimeLista()

# array = ["Alex", "Ben", "Carlos", "Diana"]

# array[4] = array[3]
# array[3] = array[2]
# array[2] = array[1]
# array[1] = array[0]
# array[0] = "Angel"