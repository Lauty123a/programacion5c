import random		
IMAGENES_AHORCADO = ['''		
  +---+		
  |   |		
      |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
      |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
  |   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|   |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
      |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 /    |		
      |		
  =========''', '''		
  +---+		
  |   |		
  O   |		
 /|\  |		
 / \  |		
      |		
  =========''']		
palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo cebra'.split()

def OptenerPalabras(ListaDePalabras):
    x=random.randint(0,len(ListaDePalabras)-1)
    PalabraSecreta=ListaDePalabras[x]
    return PalabraSecreta
def JugarDeNuevo():
    print('¿quiere jugar de nuevo?(si o no)')
    return input("ingrese su respuesta: ").lower().startswith('s')

def mostrarTablero(IMAGENES_AHORCADOletrasCorrectas,letrasIncorrectas,palabraSecretas):
    print(IMAGENES_AHORCADO[len(palabrasIncorectas)])
    print()
    print("lestras incorresctas:", end=" ")
    for letra in letrasIncorrectas:
        print(letra, end=" ")
    print()

    espaciosVacios= "_"* len(palabrasSecretas)
    
    for i in range(len(palabraSecretas)):
        espaciosVacios= espaciosVacios[:i]+palabrasSecretas[i]+ espaciosVacios[i+1]

    for letra in espaciosVacios:
        print(letra, end=" ")
        print
        
def intentos(letrasProbadas):
    print("adivina la letra")
    intento= input()
    if intento != 1:
        print("por favor introdusca una letra")
    elif intento in letrasProbasdas:
        print("ya has probado esta letrea, pruebe con otra")
    elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
        print("por favor ingrese una letra")
    else:
        return intento
        
        
        
print(OptenerPalabras(palabras))    
print(JugarDeNuevo())

