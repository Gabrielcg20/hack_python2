"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(s):
    result = s
    lista = []

    if(len(result) > 3):
        for letra in result:
            if letra == result[0]: # Ignora el primer caracter de la cadena
                continue
            elif letra == result[-1]: #Ignora el último caracter de la cadena
                continue
            else:
                lista.append(letra) # La lista se va llenando solo con los caracteres intermedios.
        
        result = "".join(lista)
    return result


print(fn_hack_4("fooziman")) # oozima
print(fn_hack_4("barziman")) # arzima
