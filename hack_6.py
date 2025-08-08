"""
generic script

["1","-"] => type string
["0"] => type string

text: "["a","b","c","d","e"]" output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(s):
    result = s
    lista = []

    if(result == []):
        return ["0"]
    else:
        for letra in result:
            indice = lista2.index(letra)
            num_str = str(indice + 1)
            if indice % 2 != 0:
                num_str = "-"
                lista.append(num_str)
            else:
                lista.append(num_str)
    
    result = lista
    return result

lista2 = ["a","b","c","d","e"]

print(fn_hack_6(lista2)) # "["1","-","3","-","5"]" 
