"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    lista = []
    for dict in result:
        for tupla in dict.items():
            lista2 = list(tupla)
            for valor in lista2:
                lista.append(valor)
    
    texto = len(lista) + 1

    nueva_lista = [i for i in range(1, texto)]
    impares = [str(i) for i in nueva_lista if i % 2 != 0]
    pares = [str(i) for i in nueva_lista if i % 2 == 0]

    result = []

    i = 0
    while(i < len(pares)):
        dict = {}
        dict[impares[i]] = pares[i]
        result.append(dict)
        i += 1
    return result

lista_2 = [{"a":"b"},{"c":"d"},{"e":"f"}]

print(fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}]))  # Salida: [{"1":"2"},{"3":"4"},{"5":"6"}]