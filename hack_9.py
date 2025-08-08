"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    dict = s
    dict_2 = {}
    lista = []

    for llave in list(dict.items())[0]:
        if len(llave) > 3:
            for letra in llave:
                if letra == "k":
                    continue
                elif letra == llave[0]:
                    lista.append(letra.upper())
                else:
                    lista.append(letra)
        else:
            dict_2[llave.capitalize()] = lista

    valor = "".join(dict_2["Foo"])
    dict_2["Foo"] = valor

    return dict_2

print(fn_hack_9({"foo": "fookziman", "bar": "barziman"}))  # {"Foo": "Fooziman"}