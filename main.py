class FindPal:
    def __init__(self,PALABRAS,FRASES,archivo,palabras,frases):
        self.PALABRAS = PALABRAS
        self.FRASES = FRASES
        self.archivo = archivo
        self.palabras = palabras
        self.frases = frases

PALABRAS = "palabras.txt"
FRASES = "frases.txt"
archivo = open(PALABRAS ,"r")
palabras = {}
for linea in archivo:
    palabras[linea.strip()] = []
archivo.close()

archivo = open(FRASES, "r")
frases = []
for f in archivo:
    frases.append(f.strip())
    for p in palabras:
        palabras[p].append(f.lower().count(p))
archivo.close()
print("Lista de palabras: \n",palabras)
print("Frase: \n", frases)
print("Palabras en frases: \n", palabras)