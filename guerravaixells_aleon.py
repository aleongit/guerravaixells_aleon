#Aleix Leon
#La Guerra de Vaixells

from guerravaixells_funcions import *

#creem tauler
tauler=crearTauler()

#col·loquem flota a tauler
colocaFlota(tauler, flota)

#mentre partida no acabada
while not partidaAcabada():
    
    #imprimir tauler mode programador
    #imprimeixTauler(tauler)
    print()
    #imprimir tauler mode joc
    imprimeixTauler(tauler,False)
    
    #xuleta estat de la flota
    printFlota()
      
    #demanar coordenades tret
    fila = None
    while not filaOK(fila):
        try:
            fila = int(input("\nIntrodueix la fila 0-9: "))
        except ValueError:
            print("No és un dígit")
    
    col = None
    while not colOK(col):
        col = input("Introdueix la columna A-J: ").upper()
    
    #fem el tret
    tret(tauler,fila,col)

printFinal()
                