
def top_3_words(text):
    auxiliar = ''
    word = {}
    palabras = []
    
    for i in text.lower() + ' ':
        if i.isalpha() or i == "'" and auxiliar:
            auxiliar += i
        
        elif i == ' ' and auxiliar:
            try:
                word[auxiliar] += 1
            except KeyError:
                word[auxiliar] = 1
            
            length = len(palabras)
            j = length - 1
            last = auxiliar

            while j >= 0:
                if word[palabras[j]] < word[auxiliar]:
                    j -= 1
                else:
                    break
            
            j += 1

            while j < length:
                palabras[j], last = last, palabras[j]
                j += 1
            
            if not palabras or len(palabras) <  3:
                palabras.append(last)
            
            auxiliar = ''
                
    return palabras


if __name__ == '__main__':
    msg = input(': ')

    print('top3: ' , top_3_words(msg))
    