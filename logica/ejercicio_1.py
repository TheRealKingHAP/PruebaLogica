"""
Ejercicio 1 de Prueba Lógica Hector Aviña
"""

def getDirection():
    #Añadir los valores deseados dentro del array de esta forma [1,1], [2,2] etc
    testmap = [[1,1], [2,2], [3,1], [3,3]]

    """
    #Quitar las comillas de comentario, para utilizar la funcián de input dentro de la consola
    
    tests = int(input("Ingresa el número de pruebas a realizar: "))
    testmap = []
    for x in range(tests):
        n,m = map(int, input("Test " + str(x+1) + ": ").split())
        testmap.append([int(n), int(m)]) 
    
    """
    
    for test in testmap:
        n = test[0]
        m = test[1]
        if(n > m):
            if(m %2 == 0):
                print('U')
            else:
                print('D')
        else:
            if(n %2 == 0):
                print('L')
            else:
                print('R')
    return

getDirection()