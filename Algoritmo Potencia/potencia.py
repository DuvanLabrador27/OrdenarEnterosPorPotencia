    
"""
El programa consiste en ordenar enteros por el valor de la potencia.
La potencia de un entero x se define como el número de pasos necesarios para 
transformar x en 1 usando los siguientes pasos:

    -if x is PAR entonces x = x / 2
    -if x is IMPAR entonces x = 3 * x + 1

    *PAR: 10/2=5
    *IMPAR: 5*3+1=16
-------EJEMPLO--------
   (para 5)
    5*3+1=16 (Primera Iteración)
    16/2=8   (Segunda Iteración)
    8/2=4    (Tercer Iteración)
    4/2=2    (Cuarta Iteración)
    2/2=1    (Quinta Iteración)

5 repeticiones para llegar a (1)
----------------------
##Requerimientos
    * El programa funciona para numeros <= 10^3
    * K= hi - lo + 1, esto quiere decir que es el tamaño de la lista

lo = Numero menor de la lista
hi = Numero mayor de la Lista
K = El tamaño de la lista

##Ejemplo de caso de prueba ACCEPTED
Lista=[3,4,5,6]

(ENTRADAS)
lo=3
hi=6
k= 6-3+1= 4 (K puede ser 1,2,3,4)--> si se excede de 4 da ERROR!!!!!

Lista=[3,4,5,6] --> Esta es la lista original
ListaValorPow=[7,2,5,8 ]-->Esta lista da el número de repeticiones según la lista original
ListaOrdenada=[4,5,3,6] --> Esta lista está ordenada en orden ascendente según la lista original y la lista valorPow la cual contiene el valor de las potencias.


-------RESULTADO---------
(ENTRADAS)
lo=3
hi=6
k=4

(SALIDA)
6--> Esta salida se da porque K=4 y en la lista ordenada el cuarto elemento es 6
ListaOrdenada=[4,5,3,6]
"""
import time
inicio = time.time()
def getKth(lo: int, hi: int, k: int):                       
        lista = []
        for i in range(lo,hi+1):
            j = i            
            count = 0
            while i != 1:
                if i%2 == 0:
                    i = i//2
                    count += 1
                else:
                    i = 3*i + 1
                    count += 1
            lista.append([count,j])
        lista.sort()
        return lista[k-1][1] 

lo=int(input())
hi=int(input())
k=int(input())
def mostrar(lista):
  return lista
lista=getKth(lo,hi,k)
print(mostrar(f"Salida: {lista}"))
#Imprimir el tiempo
fin = time.time()
print(fin-inicio) 