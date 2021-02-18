def segmentacionAtomos(formula):
    ''' 
       Esta funcion calcula el numero de atomos en una expresion de quimica. 

       [formula]: La formula quimica a analizar 

       retorna un diccionario con el numero de cada atomos 
    '''
    signosRaros = []
    i = 0
    atomos = {}
    number = ''
    componente = ''

    while i < len(formula):
        cur = formula[i]

        if cur.isupper():
            try:
                componente += cur
                for j in formula[i+1:]:
                    if j.isupper():
                        break
                    elif j.islower():
                        componente += j
                        i += 1
                    elif j.isdigit():
                        number += j
                        i += 1
                    else:
                        break
                
                atomos[componente] = (int(number) if number else 1)
                componente = ''
                number = ''
            except Exception:
                break
        elif cur.islower():
            print('formula mal escrita! ')
            break

        i += 1

    return atomos
        
class Calculator():

    def operate(self, num):
        if not num:
            return 0

        number = ''
        operar = []
        lista = '+-*/'

        parenthesis = []


        operaciones = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        current  = 0
        last = 0
        for i in num + ' ':

            if i.isdigit():
                number += i
            else:
                if number:
                    operar.append(int(number))
                    number = ''
                
                if i != ' ' and i in lista + ['(', ')']:
                    operar.append(i)
                
               

            current += 1
        
        j = 0
        while j < len(operar):
            cur = operar[j]

            if cur == '(':
               inicio = j
            if cur == ')':
               final
               
        def operarPro(operar):            
            for i in lista:      
                j = 0
                while j <  len(operar):
                    o = operar[j]
                    if o == i:                
                        try:
                            operar[j-1] = operaciones[o](operar[j-1], operar[j+1])  
                            operar.pop(j)
                            operar.pop(j)
                        except Exception as e:
                            print('Operacion en mal formato', e)
                            break
                    else:
                        j += 1
        
           
        

        operar = operarPro(operar)
        
        return operar[0]

            



def run():
    formula = input(': ')
    
    a = operate(formula)
    print(a)


if __name__ == '__main__':
    run()