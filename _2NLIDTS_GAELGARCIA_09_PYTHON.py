class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_nodo(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        elementos = []
        while actual is not None:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" ".join(elementos))

    def borrar_lista(self):
        self.cabeza = None
        print("Elemento borrado")

# Función principal
if __name__ == "__main__":
    lista = ListaEnlazada()
    
    try:
        tamanolista = int(input("Ingrese la cantidad de elementos que desea agregar a la lista: "))
    except ValueError:
        print("Entrada no válida")
        exit()
        
    if tamanolista <= 0:
        print("Cantidad de elementos no valida")
    else:
        for i in range(tamanolista):
            valor = int(input(f"Ingrese dato {i + 1}: "))
            lista.agregar_nodo(valor)
        
        print("Imprimiendo Lista de numeros")
        lista.imprimir_lista()
        lista.borrar_lista()