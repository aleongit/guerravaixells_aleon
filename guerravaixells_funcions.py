#Aleix Leon
#FUNCIONS - La Guerra de Vaixells

import random

MIDAX= 10
MIDAY= 10
INDEXF= list('ABCDEFGHIJ')
AIGUA = "~"
VAIXELL= "@"
TOCAT = "X"
ENFONSAT = "#"
flota = [5,4,4,3,3,3,2,2]
#flota = [1,2,3]
dFlota = {}

def crearTauler():
    t=[]
    for i in range(MIDAX):
        fila=[]
        for j in range(MIDAY):
            fila.append([False, AIGUA])
        t.append(fila)  
    return t

def imprimeixTauler(t,dev=True):
    #separador
    s =" "
    #imprimer files índex
    print(s,*INDEXF,end=s)
    print()
    
    #imprimir matriu
    for i in range(len(t)):
        print(i,end=s)
        for j in range(len(t[0])):
            
            #control destapades
            if not t[i][j][0] and not dev:
                print(".", end=s)
            else:
                print(t[i][j][1],end=s)
        print()
        #comprovar si casella tapada o destapada
        
def printFlota():
    #diccionari flota
    #for el in dFlota:
    #  print(el,dFlota[el])

    #flota
    print()
    print(*flota,sep=" ")
    
    #enfonsats de la flota
    for el in dFlota.values():
        if el[-1] == ENFONSAT:
            print(ENFONSAT,end =" ")
        else:
            print('-',end =" ")
    print()
       
def printAigua():
    print("               __   __")
    print("              __ \ / __")
    print("             /  \ | /  \ ")
    print("                 \|/ ")
    print("            _,.---v---._")
    print("   /\__/\  /            \ ")
    print("   \_  _/ /              \ ") 
    print("     \ \_|           @ __| ")
    print("      \                \_")
    print("       \     ,__/       /")
    print("     ~~~`~~~~~~~~~~~~~~/~~~~")
    print("             AIGUA!            ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    input("Continua..")
    
def printTocat():
    print("                                ")
    print("             |    |    |        ")         
    print("             )_)  )_)  )_)      ")    
    print("            )___))___))___)\    ")
    print("          )____)____)_____)\\   ")
    print("         _____|____|____|____\\\__")
    print("---------\                   /---------")
    print("  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^ ^^^^^    ")
    print("   ^^^^     ^^^^     ^^^^     ^^^^     ")
    print("       ^^^^     TOCAT!    ^^^^     ^^^^")
    print("---------------------------------------\n")
    input("Continua..")
    
def printEnfonsat():
    print("                     ")
    print("     _.-^^---....,,--")       
    print(" _--                  --_")  
    print("<    B O O O O O O O M   >)")
    print("|                         |") 
    print(" \._                   _./")  
    print("    ```--. . , ; .--·'' ")      
    print("          | |   |")             
    print("       .-=||  | |=-.")   
    print("       `-=#$%&%$#=-'")   
    print("          | ;  :|")     
    print(" _____.,-#%&$@%#&#~,._____")
    print("===========================")
    print("      TOCAT I ENFONSAT     ")
    print("===========================\n")
    input("Continua..")
    
def printDestapada():
    print()
    print("                                                                  ")
    print("       .-'-.            .-'-.            .-'-.           .-'-.    ")
    print("     _/_-.-_\_        _/.-.-.\_        _/.-.-.\_       _/.-.-.\_  ") 
    print("    / __} {__ \      /|( o o )|\      ( ( o o ) )     ( ( o o ) ) ")
    print("   / //  ¨  \  \    | //  ¨  \  |      |/  ¨  \|       |/  ¨  \|  ")
    print("  / / \ --- / \ \  / / \ --- / \ \      \`/^\´/         \ --- /   ")
    print("  \ \_/ `'´ \_/ /  \ \_/ `'´ \_/ /      /`\ /´\         / `'´ \   ")
    print("   \           /    \           /      /  /|\  \       /       \  ")
    print("------------------------------------------------------------------")
    print("                       JA DESTAPADA!                              ")
    print("------------------------------------------------------------------")
    input("Torna a provar..")
    
def printFinal():
    print("""
       _____              __  __   ______        ____   __      __  ______   _____         
      / ____|     /\     |  \/  | |  ____|      / __ \  \ \    / / |  ____| |  __ \        
     | |  __     /  \    | \  / | | |__        | |  | |  \ \  / /  | |__    | |__) |       
     | | |_ |   / /\ \   | |\/| | |  __|       | |  | |   \ \/ /   |  __|   |  _  /        
     | |__| |  / ____ \  | |  | | | |____      | |__| |    \  /    | |____  | | \ \        
      \_____| /_/    \_\ |_|  |_| |______|      \____/      \/     |______| |_|  \_\       
                                                                                           
                                                                                           
  _____   _   _    _____   ______   _____    _______        _____    ____    _____   _   _ 
 |_   _| | \ | |  / ____| |  ____| |  __ \  |__   __|      / ____|  / __ \  |_   _| | \ | |
   | |   |  \| | | (___   | |__    | |__) |    | |        | |      | |  | |   | |   |  \| |
   | |   | . ` |  \___ \  |  __|   |  _  /     | |        | |      | |  | |   | |   | . ` |
  _| |_  | |\  |  ____) | | |____  | | \ \     | |        | |____  | |__| |  _| |_  | |\  |
 |_____| |_| \_| |_____/  |______| |_|  \_\    |_|         \_____|  \____/  |_____| |_| \_|
                                                                                           
                                                                                            """)


#si dins rang de 0 a 9
def filaOK(f):
    return f in range(MIDAY)

#si dins INDEXF
def colOK(c):
    return c in INDEXF
                                                                                                                                             
#fila és el mateix, columna aprofitem posició de la llista INDEXF
def tradueixIndex(f,c):
    return f,INDEXF.index(c)

#retornem si la posició és aigua (True) o no (False)
def aigua(t, f, c):
    return t[f][c][1] == AIGUA

#retornem si destapada
def destapada(t,f,c):
    return t[f][c][0]
    
#comprovem si el vaixell cap al tauler, de posicio inicial (col) + mida, inferior a longitud tauler
def hiCapH(t,c,mida):
    return c + mida - 1 < len(t[0])

#comprovem si el vaixell cap al tauler, de posicio inicial (fila) + mida, inferior a longitud tauler
def hiCapV(t,f,mida):
    return f + mida - 1 < len(t)

def areaBuida(t,x,y):
    #print(x,y)
    buida = True
    for i in range(x[0],y[0]+1):
        for j in range(x[1],y[1]+1):
            #print(i,j, end=" ")
            if t[i][j][1] != AIGUA:
                #print("hi ha algo!")
                buida = False
        #print()
    return buida
    
def comprovaAreaH(t,f,c,mida):
    ok = False
    
    #1r cal mirar si vaixell hi cap, sinó no cal fer res més
    if  hiCapH(t,c,mida):
        
        #depenent fila definim coordenades
        if f > 0 and f < len(t)-1: #fila 1 a 8
            fX = f - 1
            fY = f + 1
        elif f == 0:               #fila 0
            fX = f
            fY = f + 1
        elif f == len(t)-1:        #fila 9
            fX = f - 1
            fY = f
        
        #depenent columna definim coordenades 
        if c > 0 and c < len(t[0])-1: #col 1 a 8
            cX = c - 1
            #si c + mida supera tauler, col serà última
            if c+mida == len(t[0]):
                cY = len(t[0])-1
            #sinó el supera, col serà col + mida
            else:
                cY = c + mida
        elif c == 0:               #col 0
            cX = c
            cY = c + mida
        elif c == len(t[0])-1:     #col 9
            cX = c - 1
            cY = c
             
        if areaBuida(t,(fX,cX),(fY,cY)):
            #print("Buida!")
            ok = True
        #else: 
            #print("Hi ha algo!")
    #else:
        #print("No hi cap")
    return ok

def comprovaAreaV(t,f,c,mida):
    ok = False
    
    #1r cal mirar si vaixell hi cap, sinó no cal fer res més
    if hiCapV(t,f,mida):
        #print("Hi cap")
        
        #depenent columna definim coordenades
        if c > 0 and c < len(t[0])-1: #col 1 a 8
            cX = c - 1
            cY = c + 1
        elif c == 0:               #col 0
            cX = c
            cY = c + 1
        elif c == len(t[0])-1:     #col 9
            cX = c - 1
            cY = c
        
        #depenent fila definim coordenades 
        if f > 0 and f < len(t)-1: #fila 1 a 8
            fX = f - 1
            #si c + mida supera tauler, fila serà última
            if f+mida == len(t):
                fY = len(t)-1
            #sinó el supera, fila serà fila + mida
            else:
                fY = f + mida
        elif f == 0:            #fila 0
            fX = f
            fY = f + mida
        elif f == len(t)-1:     #fila 9
            fX = f - 1
            fY = f
             
        if areaBuida(t,(fX,cX),(fY,cY)):
            #print("Buida!")
            ok = True
        #else:
            #print("Hi ha algo!")
    #else:
        #print("No hi cap")
    return ok

def colocaVaixellHoritzontal(t,f,c,mida):
    ok = False
    
    #traduim índex
    f,c = tradueixIndex(f,c)
    
    #si comprovar àrea H
    if comprovaAreaH(t,f,c,mida):
        ok = True
        #col·loquem vaixell
        for col in range(c,c+mida):
            t[f][col][1] = VAIXELL
    #else:
        #print("Impossible col·locar")
    return ok

def colocaVaixellVertical(t,f,c,mida):
    ok = False
    
    #traduim índex
    f,c = tradueixIndex(f,c)
    
    #si comprovar àrea V
    if comprovaAreaV(t,f,c,mida):
        ok = True
        #col·loquem vaixell
        for fila in range(f,f+mida):
            t[fila][c][1] = VAIXELL
    #else:
        #print("Impossible col·locar")
    return ok

#guardem vaixell horitzontal, les seves posicions a un diccionari i orientació
#index = 1a pos + llista de posicions (tuples) + orientació H
def guardaVaixellH(f,c,m,ori):
    #traduim índex
    f,c = tradueixIndex(f,c)
    
    #dFlota[f,c] = [(f,INDEXF[i]) for i in range(INDEXF.index(c),INDEXF.index(c)+m)]
    ll = []
    for i in range(c,c+m):
        #afegim coordenades vaixell
        ll.append((f,i))
    #afegim orientació
    ll.append(ori)
    #afegim llista a diccionari
    dFlota[f,c] = ll

#guardem vaixell vertical, les seves posicions a un diccionari i orientació
#index = 1a pos + llista de posicions (tuples) + orientació V
def guardaVaixellV(f,c,m,ori):
    #traduim índex
    f,c = tradueixIndex(f,c)
    
    #dFlota[f,c] = [(i,c)for i in range(f,f+m)]
    ll = []
    for i in range(f,f+m):
        #afegim coordenades vaixell
        ll.append((i,c))
    #afegim orientació
    ll.append(ori)
    #afegim llista a diccionari
    dFlota[f,c] = ll

def colocaFlota(t, flota):
    #per cada vaixell de la flota
    for vaixell in flota:
        
        #orientació aleàtoria (True = Horitzontal / False = Vertical)
        ori = random.choice([True, False])
        
        ok = False
        while not ok:
            #guardem
            f = random.randint(0,MIDAX-1) #random fila
            c = random.choice(INDEXF)     #random columna
            
            #horitzontal
            if ori:
                ok = colocaVaixellHoritzontal(t,f,c,vaixell)
            #vertical
            else:
                ok = colocaVaixellVertical(t,f,c,vaixell)
            
        #guardem vaixell a diccionari (xuleta) si ok
        #si ok horitzontal
        if ori:
            guardaVaixellH(f,c,vaixell,ori)
        #si ok vertical
        else:
            guardaVaixellV(f,c,vaixell,ori)

#comprovar totes les caselles d'un vaixell horitzontal
def comprovaVaixellH(t,f,p,mida):
    ok = False
    cont = 0       
    
    #recorrem vaixell des de 1a posició (col) vaixell fins mida
    for i in range(p[1],p[1]+mida):
        #si TOCAT incrementa
        if t[f][i][1] == TOCAT:
            cont += 1
    
    #si totes estan tocades
    if cont == mida:
        #recorre vaixell per enfonsar
        for i in range(p[1],p[1]+mida):
            t[f][i][1] = ENFONSAT
        
        #marquem vaixell enfonsat a diccionari afegint # a final llista
        dFlota[(f,p[1])].append(ENFONSAT)
        
        ok = True
    return ok

#comprovar totes les caselles d'un vaixell vertical
def comprovaVaixellV(t,c,p,mida):
    ok = False
    cont = 0       
    
    #recorrem vaixell des de 1a posició (fila) vaixell fins mida
    for i in range(p[0],p[0]+mida):
        #si TOCAT incrementa
        if t[i][c][1] == TOCAT:
            cont += 1
    
    #si totes estan tocades
    if cont == mida:
        #recorre vaixell per enfonsar
        for i in range(p[0],p[0]+mida):
            t[i][c][1] = ENFONSAT
        
        #marquem vaixell enfonsat a diccionari afegint # a final llista
        dFlota[(p[0],c)].append(ENFONSAT)
        
        ok = True
    return ok

def tocatIEnfonsat(t,f,c):
    ok = False
    #per cada vaixell en diccionari dFlota (vaixell és la key dic)
    for vaixell in dFlota:
        #recorre posicions vaixell (llista de diccionari)
        for pos in dFlota[vaixell]:
            #quan troba la posició
            if (f,c) == pos:
                #guardem índex del diccionari (1a posició vaixell)(tupla coordenades)
                #pos1[0] = fila
                #pos1[1] = col
                pos1 = vaixell
                #orientació és la última posició del vaixell (llista) de diccionari
                #(si no ha estat enfonsat, sinó última pos és marca enfonsat #)
                ori = dFlota[vaixell][-1]
                #la mida és la longitud del vaixell (llista) de diccionari - 1
                mida = len(dFlota[vaixell])-1
    #cas horitzontal
    if ori:
        ok = comprovaVaixellH(t,f,pos1,mida)
    #cas vertical
    else:
        ok = comprovaVaixellV(t,c,pos1,mida)    
    return ok
           
def tret(t,f,c):
    f,c = tradueixIndex(f,c)
    
    if destapada(t,f,c):
        printDestapada()
    else:        
        #es destapa tret independentment de si aigua o vaixell
        t[f][c][0] = True
    
        #mirem si és aigua
        if aigua(t,f,c):
            printAigua()
        else:
            #marquem TOCAT
            t[f][c][1] = TOCAT
            
            if tocatIEnfonsat(t,f,c):
                printEnfonsat()
            else:
                printTocat()

def partidaAcabada():
    #return len([el[-1] for el in dFlota.values() if el[-1] == ENFONSAT]) == len(flota)

    enfonsats = []
    for el in dFlota.values():
        if el[-1] == ENFONSAT:
            enfonsats.append(el[-1])
    
    return len(enfonsats) == len(flota)

    