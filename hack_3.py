"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(s):
    result = s
    lista = []
    lista_2 = []
    vocales = {
        'a':'@',
        'e':'v',
        'i':'¡',
        'o':'0',
        'u':'v'
    }

    lista_vocales = ['a', 'e', 'i', 'o', 'u']

    for i in result:
        if i == result[0] and i not in lista_vocales:
            lista.append(i.upper())
        elif i == result[-1] and i not in lista_vocales:
            lista.append(i.upper())
        else:
            lista.append(i)
    
    result_1 = "".join(lista)

    for letra in result_1:
        if letra == 'a':
            lista_2.append(vocales['a'])
        elif letra == 'e':
            lista_2.append(vocales['e'])
        elif letra == 'i':
            lista_2.append(vocales['i'])
        elif letra == 'o':
            lista_2.append(vocales['o'])
        elif letra == 'u':
            lista_2.append(vocales['u'])
        else:
            lista_2.append(letra)

    result_2 = "".join(lista_2)
    return result_2

print(fn_hack_3("fooziman")) # F00z¡m@N
print(fn_hack_3("barziman")) # B@rz¡m@N
print(fn_hack_3("3q")) # 3Q
print(fn_hack_3("qu")) # Qv
print(fn_hack_3("qux")) # QvX
