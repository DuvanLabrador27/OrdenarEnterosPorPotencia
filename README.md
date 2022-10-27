# ORDENAR ENTEROS POR POTENCIA :computer:

![version](https://juncotic.com/wp-content/uploads/2016/10/orden-3.png) 

## Tabla de Contenido

* [Explicacion del ejercicio :memo:](#Algoritmos)
* [Algoritmo en leetcode :memo:](#Algoritmos)
* [Algoritmo en VsCode :memo:](#Algoritmos)
* [Herramientas Utilizadas :memo:](#Herramientas)
* [Documentacion :memo:](#Documentacion)
* [Autores :memo:](#autores)
* [Conclusiones :memo:](#Conclusiones)

## Explicaion del ejercicio
 
El programa consiste en ordenar enteros por el valor de la potencia.
La potencia de un entero x se define como el número de pasos necesarios para 
transformar x en 1 usando los siguientes pasos:

    -if x is PAR entonces x = x / 2
    -if x is IMPAR entonces x = 3 * x + 1

    *PAR: 10/2=5
    *IMPAR: 5*3+1=16
    
 Para ver la explicacion más detallada se recomienda visualizar el documento:
 [Algoritmo ordenar enteros por potencia](https://drive.google.com/file/d/1VXDqfPXXJB3zkoH60x_QFmDeX8_B4Boa/view?usp=sharing)



## Algoritmo usado en leetcode
_Se anexa el metodo utilizado en la plataforma leetcode y caso de prueba aceptado:_
<p align="center">
 <img src="https://github.com/DuvanLabrador27/OrdenarEnterosPorPotencia/blob/main/img/code.png" width="500" height="500" margin-right: 20px><br>
 <img src="https://github.com/DuvanLabrador27/OrdenarEnterosPorPotencia/blob/main/img/casoPrueba.png" width="500" height="350" margin-right: 20px>
</p>


## Herramientas 

_Las herramientas utilizadas para el desarrollo del trabajo fueron:_

* [Python](https://www.python.org) - Lenguaje de Programación

<p
   align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" width="64" height="64" margin-right: 20px>
</p>
   


 ## Autores 
* CARLOS DUVAN LABRADOR H - 1151808

## Conclusiones
* Cuando nos excedemos del tamaño de la lista al aplicar la formula K=hi-lo+1, nos da error, ya que la salida esperada debe estar en el rango de esa lista.
* De las 3 implementaciones de ordenamiento en Javascript, Algoritmo de burbuja fue la que mayor tiempo de ejecución estuvo, este valor será incremental a medida que se aumente mayormente los datos.
* Se presentaron mayores tiempos de ejecución debido a que se tomaba en cuenta el tiempo que se gastaba al momento de ingresar los datos.


 
