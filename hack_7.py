"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    lista = []

    if result == [0]:
        return result
    else:
        for letra in result:
            indice = result.index(letra) + 1
            if indice % 2 != 0:
                indice_str = str(indice)
                lista.append(indice_str)
            else:
                lista.append(indice)

    result = lista
    return result

print(fn_hack_7(["a", "b", "c", "d", "e"]))  #  ["1", 2, "3", 4, "5"]
print(fn_hack_7([0]))                        #  [0]
