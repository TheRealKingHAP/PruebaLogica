def convertToRoman(number):
    '''
    Hacemos un listado con los simbolos y sus respectivos valores númericos
    para la conversián a números romanos
    '''
    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    symbols = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    i = 12
    computedSymbols = []
    result = ''
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            '''
            Añadimos cada simbolo a un array, para despues unirlos
            y guardarlos en la variable result, que sera el texto generado
            '''
            computedSymbols.append(symbols[i])
            div -= 1
        i -= 1
    
    result = ''.join(computedSymbols)

    return result

def convertToAUC(date):
    bc = 753
    ad = 1
    auc = 1
    '''
    Separamos las fechas a partir del -
    '''
    computed = date.split('-')
    date1 = computed[0]
    date2 = computed[1]

    '''
    Separamos las ultimas 2 letras y las guardamos en una variable
    para posteriormente saber si es BC o AD
    '''
    date1Key = str(date1)[len(date1) - 2]+str(date1)[len(date1) - 1]
    date2Key = str(date2)[len(date2) - 2]+str(date2)[len(date2) - 1]
    '''
    Juntamos los puros números en un array para la conversión a tipo a.u.c
    '''
    dateNum = [int(date1.split(date1Key)[0]), int(date2.split(date2Key)[0])]
    result = []
    
    '''
    Si la fecha es de tipo BC restamos, hacemos un while y vamos restando
    1 a la cantidad de BC hasta llegar a la fecha esperada, a la par le sumamos 
    a AUC un 1 en cada iteración, de esta forma obtenemos la conversión
    '''
    if(date1Key == 'BC'):
        auc = 1
        bc = 753
        while bc:
            if(bc == dateNum[0]):
                result.append(auc)
            
            auc += 1
            bc -= 1
    '''
    Para AD es mas o menos similar, solo que ahora a la fecha
    se le resta un 1 en cada iteracián y a auc se le suma 1 pero esta vez
    empezando por 754 que es el equivalente de 1 AD
    '''
    if(date1Key == 'AD'):
        auc = 754
        while dateNum[0]:
            if(ad == dateNum[0]):
                result.append(auc)
            
            auc += 1
            dateNum[0] -= 1
    
    '''
    Hacemos lo mismo que el paso anterior 
    solo que para la segunda fecha
    '''
    if(date2Key == 'BC'):
        auc = 1
        bc = 753
        while bc:
            if(bc == dateNum[1]):
                result.append(auc)
            auc += 1
            bc -= 1

    if(date2Key == 'AD'):
        auc = 754
        while dateNum[1]:
            if(ad == dateNum[1]):
                result.append(auc)
            auc += 1
            dateNum[1] -= 1
    
    return result

'''
Se puede sustituir este array por las fechas a testear
'''
dates = ['1BC-1AD','753BC-747BC','2000AD-2012AD']

'''
Se hacen las pruebas correspondientes y se imprime
el número que tenga la mayor cantidad de simbolos
esto quiere decir que es el espacio minimo necesario para alojar
esa fecha
'''

for date in dates:
    result = convertToAUC(date)

    maxResult = max(len(convertToRoman(result[0])), len(convertToRoman(result[1])))

    print('Minimum space to reserve: ', maxResult)