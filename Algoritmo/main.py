from potencia import getKth
import time
inicio = time.time()

lo=int(input())
hi=int(input())
k=int(input())
def mostrar(lista):
  return lista
lista=getKth(lo,hi,k)
print(mostrar(f"Salida: {lista}"))

#Imprimir tiempo
fin = time.time()
print(fin-inicio) 