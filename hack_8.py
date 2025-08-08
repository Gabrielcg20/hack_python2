"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    result = s
    texto = len(result)
    lista = []

    if(texto % 2 == 0):
        for letra in result:
            indice = result.index(letra) + 1
            indice_str = str(indice)
            lista.append(indice_str)
        lista.reverse()
    else:
        for letra in result:
            indice = result.index(letra) + 1
            mensaje = f'{letra}-{indice}'
            lista.append(mensaje)
        
        lista.reverse()

    return lista

print(fn_hack_8(["a", "b", "c", "d", "e"]))   #  ["e-5","d-4","c-3","b-2","a-1"]
print(fn_hack_8(["a", "b", "c"]))             #  ["c-3","b-2","a-1"]
print(fn_hack_8(["a", "b", "c", "d"]))        #  ["4", "3", "2", "1"]
print(fn_hack_8(["a", "b"]))                  #  ["2", "1"]
