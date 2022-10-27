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

## Algoritmo usado en VSCODE
_Se anexa el metodo utilizado en VSCODE y caso de prueba aceptado:_
<p align="center">
 <img src="https://github.com/DuvanLabrador27/OrdenarEnterosPorPotencia/blob/main/img/code2.png" width="500" height="700" margin-right: 20px><br>
 <img src="https://github.com/DuvanLabrador27/OrdenarEnterosPorPotencia/blob/main/img/caso2.png" width="500" height="350" margin-right: 20px>
</p>

## Herramientas 

_Las herramientas utilizadas para el desarrollo del trabajo fueron:_

* [Python](https://www.python.org) - Lenguaje de Programación
* [Pytest](https://pypi.org/project/pytest/) - Marco de prueba de Python

<p
   align="center"> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png" width="64" height="64" margin-right: 20px>
 <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/1200px-Pytest_logo.svg.png" width="64" height="64" margin-right: 20px>
</p>
   


 ## Autores 
* CARLOS DUVAN LABRADOR H - 1151808

## Conclusiones
* Cuando nos excedemos del tamaño de la lista al aplicar la formula K=hi-lo+1, nos da error, ya que la salida esperada debe estar en el rango de esa lista.


 
