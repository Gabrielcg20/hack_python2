"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    texto = [s[i:i+3] for i in range (0, len(s), 3)]

    resultado_texto = []

    for text in texto:
        if len(text) == 3:
            nuevo_texto = f"{text[0]}{text[1].upper()}{text[2]}"
            resultado_texto.append(nuevo_texto)
        else:
            resultado_texto.append(text)
        
    return "".join(resultado_texto)

print(fn_hack_1("fooziman"))  #fOozIman
print(fn_hack_1("qux"))  #qUx
print(fn_hack_1("eq"))  #eq