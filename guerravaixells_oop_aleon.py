#Aleix Leon

""" Tasca 4.3. Batalla Naval

Fes un joc de batalla naval per jugar contra l'ordinador.

Especificacions:

. Taulell de 10x10 posicions.

. Hi col·locarem aleatòriament els següents vaixells 
( no es poden tocar entre ells):
1 portaavions de 4 caselles.
2 cuirassats de 3 caselles.
3 fragates de 2 caselles.
4 patrulleres d'1 casella.

. A cada pas es mostrarà la matriu indicant 
les cel·les ocultes, tocades i buides.

. L'usuari introduirà fila i columna.

. Quan s'enfonsin tots els vaixells la partida s'acaba 
i sortim del programa (amb un missatge de congratulations!).

. Opció en català, anglès i alguna altra llengua.

. Cal que puguis jugar diverses partides simultànies 
(diferents taulells). 
El jugador ha de poder anar canviant entre les diverses partides 
i reprendre on l'ha deixat.

. Cal fer-ho amb OOP i, per tant, primer cal definir els objectes 
i les estructures de dades 
i decidir com utilitzar-les en el codi principal. 
Com a mínim, heu d'implementar les següents classes: 
class Tauler(), class Vaixell() i class Casella().
 """

import random

X = 10
Y = 10
AIGUA = " ~"
TAPA = " ."
VAIXELL= " @"
TOCAT = " X"
ENFONSAT = " #"
SEP = " "
LINIA = "_"*12
NOU = '+'
LANG = 'i'
EXIT = 'x'

TIPUS = ['POR', 'CUI', 'FRA', 'PAT']
#MENU = "MENÚ => [FC]Tirada | J[0-9]canvi joc | [+]nou joc | [i]idioma | [x]sortir\n"
IDIOMES = ['ca', 'es', 'en']

partides = []

missatges = {
    "ca": {
        "jocs": "\nJOCS =>",
        "joc": "JOC",
        "menu": "MENÚ => [FC]Tirada | J[0-9]canvi joc | [+]nou joc | [i]idioma | [x]sortir\n",
        "tira": "TIRA! : ",
        "hola": "BENVINGUT !!!",
        "aigua": "AIGUA !!!",
        "tocat": "TOCAT !!!",
        "enfonsat": "ENFONSAT !!!",
        "fi": "ENHORABONA !",
        "error": "\n* FATAL ERROR * opció no vàlida\n",
        "idioma": "Tria idioma"
    },
    "es": {
        "jocs": "\nJUEGOS =>",
        "joc": "JUEGO",
        "menu": "MENÚ => [FC]Jugada | J[0-9]cambio juego | [+]nuevo juego | [i]idioma | [x]salir\n",
        "tira": "DALE! : ",
        "hola": "BIENVENIDO !!!",
        "aigua": "AGUA !!!",
        "tocat": "TOCADO !!!",
        "enfonsat": "HUNDIDO !!!",
        "fi": "ENHORABUENA !",
        "error": "\n* FATAL ERROR * opción no válida\n",
        "idioma": "Elige idioma"
    },
    "en": {
        "jocs": "\nGAMES =>",
        "joc": "GAME",
        "menu": "MENU => [FC]Play | J[0-9]change game | [+]new game | [i]language | [x]exit\n",
        "tira": "PLAY! : ",
        "hola": "WELCOME !!!",
        "aigua": "WATER !!!",
        "tocat": "TOUCHED !!!",
        "enfonsat": "SUNK !!!",
        "fi": "CONGRULATIONS !",
        "error": "\n* FATAL ERROR * invalid option\n",
        "idioma": "Choose a language"
    },
}

# funcions ___________________________________________________

def crea_joc():
    joc = Tauler()
    joc.crea_flota()
    joc.posa_flota()
    partides.append(joc)
    return joc

def partida_acabada(joc):
    print(missatges[lang]["fi"])
    partides.remove(joc)

def print_joc(partida):
    partida.print_titol_joc()
    #partida.print_ocea('con')
    #partida.print_ocea('barco')
    partida.print_ocea('joc')
    partida.print_titol_joc()
    partida.print_flota_joc()
    #partida.print_flota_info()
    print_jocs()
    print(missatges[lang]['menu'])


def print_jocs():
    #print('\nJOCS =>',end =" ")
    print(missatges[lang]['jocs'],end =" ")
    for joc in partides:
        #print(jocs.index(joc), end ="=>[")
        print(joc.id, end ="=>[")
        joc.print_estat_joc()
        print(end ="] ")
    print()

def ids_joc():
    return [joc.get_id() for joc in partides]

#classes objecte ______________________________________________

#classe tauler
class Tauler(object):
    total = 0
    #constructor per defecte
    def __init__(self):
        self.__class__.total += 1
        self.id = 'J' + str(self.total)
        self.MIDAX = X
        self.MIDAY= Y
        self.CASELLES = [] #ids totes les caselles
        #self.matriu on cada element matriu tipus casella
        #self.ocea = [[Casella() for i in range(self.MIDAX)] for j in range(self.MIDAY)]
        self.ocea = self.crea_ocea()
        self.flota = {} #diccionari de barcos del tauler
        self.flota_def = ['POR','CUI','CUI','FRA','FRA','FRA','PAT','PAT','PAT','PAT']
        #self.idioma ='CAT'
    
    #contrucció
    def crea_ocea(self):
        ocea=[]
        for i in range(self.MIDAX):
            fila=[]
            for j in range(self.MIDAY):
                fila.append(Casella(i,j)) #crea casella
                self.CASELLES.append(str(i)+str(j)) #agafeix llista caselles
            ocea.append(fila)  
        return ocea

    def conta_tipus(self,tipus):
        conta = 0
        for k,v in self.flota.items():
            if v.prefix == tipus:
                conta += 1
        return conta

    def conta_tipus_tocats(self,tipus):
        conta = 0
        for k,v in self.flota.items():
            if v.prefix == tipus and v.vida == 0:
                conta += 1
        return conta

    def conta_tocats(self):
        return len([v for k,v in self.flota.items() if v.vida == 0])

    def conta_barcos(self):
        return len([v for k,v in self.flota.items()])
            
    #crea_barco dins tauler
    def crea_barco(self,tipus):

        #comptador tipus
        n = self.conta_tipus(tipus) + 1

        #envio número barcos x tipus a tauler per id barco
        if tipus == 'BAR':
            barco = Vaixell(n)
        elif tipus == 'POR':
            barco = PortaAvions(n)
        elif tipus == 'CUI':
            barco = Cuirassat(n)
        elif tipus == 'FRA':
            barco = Fragata(n)
        elif tipus == 'PAT':
            barco = Patrullera(n)

        #agafeix a diccionari flota
        self.flota[barco.id] = barco

    #crea_flota
    def crea_flota(self):
        for tipus in self.flota_def:
            self.crea_barco(tipus)

    #generar llista ids caselles
    def caselles_possibles(self,ori,fila,col,mida):
        ll = []
        #cas hori
        #i = col
        if (ori):
            for i in range(col, col + mida):
                casella = str(fila)+ str(i)
                ll.append(casella)
        #cas verti
        #i = fila
        else:
            for i in range(fila, fila + mida):
                casella = str(i)+ str(col)
                ll.append(casella)
        return ll
    
    def caselles_voltant(self,ori,fila,col,mida):
        ll = []
        #cas hori
        if (ori):
            for i in range(fila -1 , (fila + 1) + 1):
                for j in range(col - 1, col + mida + 1):
                    casella = str(i)+ str(j)
                    #filtrem caselles 'fora límit'
                    if casella in self.CASELLES:
                        ll.append(casella)
        #cas verti
        else:
            for i in range(fila - 1, fila + mida + 1):
                for j in range(col - 1, (col + 1) + 1):
                    casella = str(i)+ str(j)
                    #filtrem caselles 'fora límit'
                    if casella in self.CASELLES:
                        ll.append(casella)
        return ll

    #recuperar objectes caselles a llista
    def recupera_caselles(self,caselles):
        ll = []
        for el in caselles:
            ll.append(self.ocea[int(el[0])][int(el[1])])
        return ll
    
    def get_casella(self,c):
        return self.ocea[int(c[0])][int(c[1])]

    def posa_barco(self,barco):
        
        ok = False
        #fins no trobar una col·locació ok
        while not ok:

            #orientació aleàtoria (True = Horitzontal / False = Vertical)
            ori = random.choice([True, False])
            fila = random.randint(0,self.MIDAY-1) #random fila
            col = random.randint(0,self.MIDAX-1) #random col
            mida = barco.mida
        
            #print(ori,fila,col,mida)

            #podem saber caselles, les generem a llista
            #exemple: 
            #hori 57,58,59,60
            #verti 57,67,77,87

            possibles = self.caselles_possibles(ori,fila,col,mida)           
            #print(possibles)

            #caselles en CASELLES ?
            #si estan fora límit, repetir random
            ok = all(casella in self.CASELLES for casella in possibles)
            #print(ok)
            
            #si ok, recupero objectes caselles tauler
            if ok:
                reals = self.recupera_caselles(possibles)

                #si totes atribut 'ok' per col·locar
                #sinó repetir random
                ok = all(casella.ok for casella in reals)
                if ok:
                    #per cada casella real
                    for real in reals:                    
                        #update caselles reals
                        real.ok = False
                        real.barco = barco.id
                        real.contingut = VAIXELL

                    #update barco
                    barco.posicions = list(possibles)
                    barco.update_vida()
                    
                    #print(fila,col)
                    
                    #marcar caselles del voltant (atribut 'ok' a false)
                    #generem llista ids del voltant i fintrant els 'fora límits'
                    voltant = self.caselles_voltant(ori,fila,col,mida)
                    #print(voltant)

                    #recuperem objectes caselles reals
                    reals = self.recupera_caselles(voltant)

                    #per cada casella real
                    for real in reals:                    
                        #update caselles reals si 'ok' a true
                        if real.ok:
                            real.ok = False
     
    def posa_flota(self):
        #t3.posa_barco(t3.flota['POR1'])
        for k in self.flota.keys():
            self.posa_barco(self.flota[k])

    def tirada(self,c):
        #get casella
        casella = self.get_casella(c)

        #si casella no tocada i hi ha una id barco
        #print(self.get_ids_flota())
        if not casella.tocada:
            if casella.barco in self.get_ids_flota():
                #recupera barco de flota
                barco = self.flota[casella.barco]
                #print(barco)

                #casella no estarà a tocs, perquè no tenia marca tocada
                
                #update barco
                barco.tocades.append(c)
                barco.update_vida()

                #update casella
                casella.tocada = True
                casella.contingut = TOCAT
                print(missatges[lang]["tocat"])

                #barco enfonsat, mirem vides
                if barco.vida == 0:
                    #recupera caselles barco
                    caselles = self.recupera_caselles(barco.posicions)
                    for cas in caselles:
                        #marquem enfonsat
                        cas.contingut = ENFONSAT
                    print(missatges[lang]["enfonsat"])

                #tots els barcos enfonsats? partida acabada
                if self.conta_tocats() == self.conta_barcos():
                    partida_acabada(self)
            else:
                #aigua
                #update casella
                casella.tocada = True
                casella.contingut = AIGUA
                print(missatges[lang]["aigua"])
    #gets
    def get_id(self):
        return self.id

    def get_CASELLES(self):
        return self.CASELLES

    def get_ids_flota(self):
        return [barco.id for k,barco in self.flota.items()]

    #print objecte
    #def __str__(self):
        #return "%s %s %s %s" %(self.nom, self.cognoms, self.data_n, self.tlf)

    #print
    def print_ocea(self,op):
        opcio = op
        print()
        #print llegenda cols
        print(SEP,end=SEP)
        print(*[SEP +str(i) for i in range(self.MIDAY)])
        for i in range(self.MIDAX):
            #print llegenda files
            print(i, end=SEP)
            for j in range(self.MIDAY):
                if opcio == 'con':
                    print(self.ocea[i][j].contingut,end=SEP)
                elif opcio == 'id':
                    print(self.ocea[i][j].id,end=SEP)
                elif opcio == 'barco':
                    print(self.ocea[i][j].barco,end=SEP)
                elif opcio == 'ok':
                    print(self.ocea[i][j].ok,end=SEP)
                elif opcio == 'joc':
                    if self.ocea[i][j].tocada:
                        print(self.ocea[i][j].contingut,end=SEP)
                    else:
                        print(TAPA,end=SEP)
            print()
        print()
    
    #diccionari flota
    #def print_flota(self):
    #    for k,v in self.flota.items():
    #        print("%s -> %s" %(k,v))

    def print_flota_info(self):
        for k,v in self.flota.items():
            print(k, '=>', end =SEP)
            v.print_id()
            v.print_mida()
            v.print_pos()
            v.print_tocs()
            v.print_vida()
            print()

    def print_flota_joc(self):
        for tipus in TIPUS:
            tocats = self.conta_tipus_tocats(tipus)
            totals = self.conta_tipus(tipus)
            if tipus == TIPUS[-1]:
                print("%s: %s/%s" %(tipus,tocats,totals), end ='')
            else:
                print("%s: %s/%s" %(tipus,tocats,totals), end =' - ')
        print()

    def print_titol_joc(self):
        print('%s* %s %s *%s' %(LINIA,missatges[lang]['joc'],self.id,LINIA))

    def print_estat_joc(self):
        print(f"{self.conta_tocats()}/{self.conta_barcos()}",end ="")

#classe casella
class Casella(object):
    #constructor per defecte
    def __init__(self,fila,col):
        #self.fila = fila
        #self.col = col
        #self.id = str(fila)+str(col) # coordenades string fila x col (00, 01, ...)
        self.ok = True #ok per col·locar
        self.tocada = False #tocada en joc
        self.barco = AIGUA * 2  #id barco
        self.contingut = AIGUA # string per aigua, tocat, enfonsat (~, @, X, #)
    
#class vaixell
class Vaixell(object):
    #total = 0 #variable de classe comptador vaixells

    #constructor
    def __init__(self,n):
        #self.__class__.total += 1
        self.prefix = "BAR"
        #self.id = self.prefix + str(self.__class__.total)
        self.id = self.prefix + str(n)
        self.mida = 2
        self.posicions = [] #id posicions a tauler
        self.tocades = [] #id posicions tocades
        self.vida = 0

    def update_vida(self):
        #print(self.posicions)
        #print(self.tocades)
        #print(len(self.posicions),len(self.tocades))
        self.vida = len(self.posicions) - len(self.tocades) #inici la mida, final 0

    #print
    def print_id(self):
        print('ID:', self.id, end=SEP)

    def print_mida(self):
        print('MIDA:',self.mida, end=SEP)

    def print_pos(self):
        print('POS:',self.posicions, end=SEP)

    def print_tocs(self):
        print('TOCS:',self.tocades, end=SEP)

    def print_vida(self):
        print('VIDA:',self.vida, end=SEP)

    def print_info_barco(self):
        print(self.id)
        print(self.mida)
        print(self.posicions)
        print(self.tocades)
        print(self.vida)

#SUBCLASSES TIPUS DE VAIXELL
#prefix (PAT, FRA, CUI, POR)
#mides (1,2,3,4)
#fer un contador per prefix (PAT1, PAT2, )

#1 portaavions de 4 caselles.
#fill class vaixell
class PortaAvions(Vaixell):
    #constructor fill
    def __init__(self,n):
        super(PortaAvions,self).__init__(n)
        self.prefix = "POR" #portaavions
        self.mida = 4
        self.id = self.prefix + str(n)
        #self.posicions = [] #id posicions a tauler
        #self.tocades = [] #id posicions tocades
        #self.vida = len(self.posicions) - len(self.tocades) #inici la mida, final 0

#2 cuirassats de 3 caselles.
#fill class vaixell
class Cuirassat(Vaixell):
    #constructor fill
    def __init__(self,n):
        super(Cuirassat,self).__init__(n)
        self.prefix = "CUI" #cuirassat
        self.mida = 3
        self.id = self.prefix + str(n)

#3 fragates de 2 caselles.
#fill class vaixell
class Fragata(Vaixell):
    #constructor fill
    def __init__(self,n):
        super(Fragata,self).__init__(n)
        self.prefix = "FRA" #fragata
        self.mida = 2
        self.id = self.prefix + str(n)

#4 patrulleres d'1 casella.
#fill class vaixell
class Patrullera(Vaixell):
    #constructor fill
    def __init__(self,n):
        super(Patrullera,self).__init__(n)
        self.prefix = "PAT" #patrullera
        self.mida = 1
        self.id = self.prefix + str(n)


#programa ______________________________________________________________
if __name__ == "__main__":

    #inicialitzem
    lang = 'ca'
    #creem un 1r joc
    partida = crea_joc()
    print(missatges[lang]["hola"])
    
    op = ''
    while op.lower() != EXIT:
        print_joc(partida)
        #op = input("TIRA: ")
        op = input(missatges[lang]["tira"])

        if op in partida.get_CASELLES():
            #print("FILA-COL")
            partida.tirada(op)

        elif op.upper() in ids_joc():
            #print("canvi JOC")
            #print(ids_joc().index(op))
            partida = partides[ids_joc().index(op.upper())]
        elif op == NOU:
            #print("nou JOC")
            #crea i canvia de partida
            partida = crea_joc()
        elif op.lower() == LANG:
            #print("canvi IDIOMA")
            op = input("%s %s : " %(missatges[lang]["idioma"],IDIOMES))
            if op in IDIOMES:
                lang = op
            else:
                print(missatges[lang]["error"])
        elif op.lower() == EXIT:
            pass
        else:
            print(missatges[lang]["error"])
