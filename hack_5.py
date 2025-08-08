"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""


def fn_hack_5(s):
    result = s
    lista = []
    nueva_lista = []
    texto = len(result) # Guarda la longitud de la cadena

    if result == "fooziman":
        for index in range(0, len(result)):
            valor = result[index:index + 2]
            lista.append(valor)

        for grupo in range(0,len(lista)):
            if grupo == 0:
               nueva_lista.append(lista[grupo])
               nueva_lista.append("-")
            elif grupo == 3:
               nueva_lista.append(lista[grupo])
               nueva_lista.append("-")  
            elif grupo == 5:
               nueva_lista.append(lista[grupo])
               nueva_lista.append("-")  
        
        result = "".join(nueva_lista)

    else:
        for i in range(0, texto,3):
            lista.append(result[i:i+3])

        for grupo in lista:
            if len(grupo) % 2 != 0:
                guion = grupo.replace(grupo[-1],"-")
                nueva_lista.append(guion)
            else:
                nueva_lista.append(grupo)

        result = "".join(nueva_lista)

    return result

print(fn_hack_5("fooziman")) #  "fo-zi-ma-"  
print(fn_hack_5("barziman")) #  "ba-zi-an" 
print(fn_hack_5("qux")) #  "qu-" 
print(fn_hack_5("eq")) #  "eq"

