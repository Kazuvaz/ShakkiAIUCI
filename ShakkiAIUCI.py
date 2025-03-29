    
def deAlphabetize(se:chr):
    if se == 'a':
        return '0'
    elif se == 'b':
        return '1'
    elif se == 'c':
        return '2'
    elif se == 'd':
        return '3'
    elif se == 'e':
        return '4'
    elif se == 'f':
        return '5'
    elif se == 'g':
        return '6'
    else:
        
        return 7

def alphabetize(se):
    if se == 0:
        return 'a'
    elif se == 1:
        return 'b'
    elif se == 2:
        return 'c'
    elif se == 3:
        return 'd'
    elif se == 4:
        return 'e'
    elif se == 5:
        return 'f'
    elif se == 6:
        return 'g'
    else:
        return 'h'



class board():
    #luodaan pelikentta nappulat merkataan isolla kirjaimella jos ne on valkoisia ja pienellä jos ne on mustia
    #r=torni, n=ratsu, b=lähetti, q=kuningatar, k= kuningas, p=sotilas, 0 = tyhjä
    pieces =[[0 for i in range(8)] for j in range(8)]
    #kumman vuoro TRUE = valkoinen
    turn = True
    #linnoitus oikeudet [musta kuningattaterpuoli, kuninkaan puoli, valkoinen kuningattaren puoli, kuninkaan puoli]
    castling = [True,True,True,True]
    def __init__(self, pieces, turn, castling):
        #luodaan pöytä tietyssä tilanteessa
        self.pieces = pieces[:]
        self.turn = turn
        self.castling = castling[:]
    
    #siirtää siirto syntaxin mukaan
    def move(self, syntax):
        froms = [int(syntax[1])*-1+8,int(deAlphabetize(syntax[0]))]
        tos = [int(syntax[3])*-1+8,int(deAlphabetize(syntax[2]))]
        #korotukset
        if len( syntax) > 4:
            if self.turn:
                self.pieces[tos[0]][tos[1]] = str(syntax[4]).capitalize()
            else:
                self.pieces[tos[0]][tos[1]] = str(syntax[4]).capitalize()
        else:
            self.pieces[tos[0]][tos[1]] = self.pieces[froms[0]][froms[1]]
        self.pieces[froms[0]][froms[1]] = '0'
    #siirtää koordinaattejen mukaan, muista että koordinaatit alkavat vasen yläkulma
    def moveInt(self, afro,bfro,ato,bto):
        froms = [afro,bfro]
        tos = [ato,bto]

        self.pieces[tos[0]][tos[1]] = self.pieces[froms[0]][froms[1]]
        self.pieces[froms[0]][froms[1]] = '0'
    #muuttaa koordinaatti notaation uci formattiin
    def convertUCI(self, afro,bfro,ato,bto):
        return (alphabetize(bfro) +str(afro*-1+7+1)+ alphabetize(bto) +str(ato*-1+7+1))
    #tarkastaa onko koordinaatit pöydällä
    def onBoard(self,a,b):
        return a >= 0 and a < 8 and b >= 0 and b < 8
    
    #palauttaa kaikki mahdolliset pöydät jotka voivat jatkua nykyisestä tilanteesta
    def Friendly(self, a,b):
        if not self.onBoard(a,b):
            return True
        if self.turn and self.pieces[a][b] in ['N','P','R','B','K','Q']:
            return True
        if not self.turn and self.pieces[a][b] in ['n','p','r','b','k','q']:
            return True
        return False
    

    def lahetti(self, i,j):
        legals = []
        
        for k in range(1,8):
            if not self.onBoard(i+k,j+k):
                break
            if self.pieces[i+k][j+k] == '0':
                legals.append((i,j,i+k,j+k))
            elif self.Friendly(i+k,j+k):
                break
            else:
                legals.append((i,j,i+k,j+k))
                break

        for k in range(1,8):
            if not self.onBoard(i-k,j-k):
                break
            if self.pieces[i-k][j-k] == '0':
                legals.append((i,j,i-k,j-k))
            elif self.Friendly(i-k,j-k):
                break
            else:
                legals.append((i,j,i-k,j-k))
                break
        
        for k in range(1,8):
            if not self.onBoard(i-k,j+k):
                break
            if self.pieces[i-k][j+k] == '0':
                legals.append((i,j,i-k,j+k))
            elif self.Friendly(i-k,j+k):
                break
            else:
                legals.append((i,j,i-k,j+k))
                break
        
        for k in range(1,8):
            if not self.onBoard(i+k,j-k):
                break
            if self.pieces[i+k][j-k] == '0':
                legals.append((i,j,i+k,j-k))
            elif self.Friendly(i+k,j-k):
                break
            else:
                legals.append((i,j,i+k,j-k))
                break
                    
        return legals
    def torni (self,i,j):
        legals = []
        for k in range(1,8):
            if not self.onBoard(i,j+k):
                break
            if self.pieces[i][j+k] == '0':
                legals.append((i,j,i,j+k))
            elif self.Friendly(i,j+k):
                break
            else:
                legals.append((i,j,i,j+k))
                break
        
        for k in range(1,8):
            if not self.onBoard(i,j-k):
                break
            if self.pieces[i][j-k] == '0':
                legals.append((i,j,i,j-k))
            elif self.Friendly(i,j-k):
                break
            else:
                legals.append((i,j,i,j-k))
                break
        
        for k in range(1,8):
            if not self.onBoard(i+k,j):
                break
            if self.pieces[i+k][j] == '0':
                legals.append((i,j,i+k,j))
            elif self.Friendly(i+k,j):
                break
            else:
                legals.append((i,j,i+k,j))
                break
        
        for k in range(1,8):
            if not self.onBoard(i-k,j):
                break
            if self.pieces[i-k][j] == '0':
                legals.append((i,j,i-k,j))
            elif self.Friendly(i-k,j):
                break
            else:
                legals.append((i,j,i-k,j))
                break
                    
        return legals
    def legalContinuations(self):
        legals = []
        converted = []
        for i in range(0,8):
            for j in range(0,8):
                #onko i,j nappula joka voi liikkua?
                if self.Friendly(i,j):
                    #sotilas
                    if self.pieces[i][j] in ['p','P']:
                        #koska sotilaiden väri määrittää niiden suunnan käytän kerrointa
                        direction = 1
                        if self.turn:
                            direction = -1
                        if self.pieces[i+direction][j] == '0':
                            
                            if i+direction in [0,7]:
                                #korota
                                
                                converted.append(self.convertUCI((i,j,i+direction,j)) + 'r')
                                converted.append(self.convertUCI((i,j,i+direction,j)) + 'q')
                                converted.append(self.convertUCI((i,j,i+direction,j)) + 'b')
                                converted.append(self.convertUCI((i,j,i+direction,j)) + 'n')

                                
                            else:
                                legals.append((i,j,i+direction,j))
                            #tuplasiirto
                            if i == 6 and self.pieces[i+2*direction][j] == '0':
                                legals.append((i,j,i+2*direction,j))
                        #syö
                        if self.onBoard(i+direction,j+1):
                            if self.turn and self.pieces[i+direction][j+1] in ['n','p','r','b','k','q'] or not self.turn and self.pieces[i+direction][j+1] in ['N','P','R','B','Q']:
                                legals.append((i,j,i+direction,j+1))
                            if  self.turn and self.pieces[i+direction][j-1] in ['n','p','r','b','k','q'] or not self.turn and self.pieces[i+direction][j-1] in ['N','P','R','B','Q']:
                                legals.append((i,j,i+direction,j-1))
                                
                    #ratsu siirrot
                    if self.pieces[i][j] in ['n','N']:

                        
                        if not self.Friendly(i+2,j+1):
                            legals.append((i,j,i+2,j+1))
                        if not self.Friendly(i+2,j-1):
                            legals.append((i,j,i+2,j-1))
                        
                        if not self.Friendly(i-2,j+1):
                            legals.append((i,j,i-2,j+1))
                        if not self.Friendly(i-2,j-1):
                            legals.append((i,j,i-2,j-1))

                        if not self.Friendly(i+1,j+2):
                            legals.append((i,j,i+1,j+2))
                        if not self.Friendly(i-1,j+2):
                            legals.append((i,j,i-1,j+2))

                        if not self.Friendly(i+1,j-2):
                            legals.append((i,j,i+1,j-2))
                        if not self.Friendly(i-1,j-2):
                            legals.append((i,j,i-1,j-2))
                    
                    #Lähetti siirrot
                    if self.pieces[i][j] in ['b','B']:
                        for s in self.lahetti(i,j):
                            legals.append(s)
                    #torni siirrot
                    if self.pieces[i][j] in ['r','R']:
                        for s in self.torni(i,j):
                            legals.append(s)
                    #kuningatar
                    if self.pieces[i][j] in ['q','Q']:
                        for s in self.torni(i,j):
                            legals.append(s)
                        for s in self.lahetti(i,j):
                            legals.append(s)
                    #kuningas 
                    if self.pieces[i][j] in ['q','Q']:
                        for k in range(0,3):
                            for l in range(0,3):
                                if not( k == 1 and l == 1):
                                    if not self.Friendly(i+k-1,j+l-1):
                                        legals.append((i,j,i+k-1,j+l-1))
        for le in legals:
            converted.append (self.convertUCI(le[0],le[1],le[2],le[3]))
        for co in converted:
            print(co)
    #tarkistaa että onko vastustaja shakissa siirron alussa
    #tämä vaihe olisi voitu suorittaa legal continuationin kanssa, mutta tämä on erillinen funktion tulevaisuuden optimoimista varten. 
    def impossible(self):
        for i in range(0,8):
            for j in range(0,8):
                #löytää vastustajan kuninkaan
                if self.turn and self.pieces[i][j] == 'k'or not self.turn and self.pieces[i][j] == 'K':
                    #ratsu shakit
                    target = 'n'
                    if self.turn:
                        target = 'N'
                    if (
                        self.Friendly(i+2,j+1) and self.pieces[i+2][j+1] == target or self.Friendly(i+2,j-1) and self.pieces[i+2][j-1] == target 
                        or self.Friendly(i-2,j+1) and self.pieces[i-2][j+1] == target or self.Friendly(i+2,j-1) and self.pieces[i-2][j-1] == target
                        or self.Friendly(i+1,j+2) and self.pieces[i+1][j+2] == target or self.Friendly(i-1,j+2) and self.pieces[i-1][j+2] == target 
                        or self.Friendly(i+1,j-2) and self.pieces[i+1][j-2] == target or self.Friendly(i-1,j-2) and self.pieces[i-1][j-2] == target
                    ) :
                        return True
                    #tornishakit
                    target = 'r'
                    target2 = 'q'
                    if self.turn:
                        target = 'R'
                        target2 = 'Q'
                    for k in range(1,8):
                        if self.Friendly(i,j+k) and (self.pieces[i][j+k] == target or self.pieces[i][j+k] == target2):
                            return True
                        elif not (self.onBoard(i,j+k) and self.pieces[i][j+k] == '0'):
                            break
                    for k in range(1,8):
                        if self.Friendly(i,j-k) and (self.pieces[i][j-k] == target or self.pieces[i][j-k] == target2):
                            return True
                        elif not (self.onBoard(i,j-k) and self.pieces[i][j-k] == '0'):
                            break
                    for k in range(1,8):
                        if self.Friendly(i+k,j) and (self.pieces[i+k][j] == target or self.pieces[i+k][j] == target2):
                            return True
                        elif not (self.onBoard(i+k,j) and self.pieces[i+k][j] == '0'):
                            break
                    for k in range(1,8):
                        if self.Friendly(i-k,j) and (self.pieces[i-k][j] == target or self.pieces[i-k][j] == target2):
                            return True
                        elif not (self.onBoard(i-k,j) and self.pieces[i][j-k] == '0'):
                            break
                    #lahetti shakit
                    target = 'b'
                    target2 = 'q'
                    if self.turn:
                        target = 'B'
                        target2 = 'Q'
                    for k in range(1,8):
                        if self.Friendly(i+k,j+k) and (self.pieces[i+k][j+k] == target or self.pieces[i+k][j+k] == target2):
                            return True
                        elif not (self.onBoard(i+k,j+k) and self.pieces[i+k][j+k] == '0'):
                            break
                    for k in range(1,8):
                        if self.Friendly(i+k,j-k) and (self.pieces[i+k][j-k] == target or self.pieces[i+k][j-k] == target2):
                            return True
                        elif not (self.onBoard(i+k,j-k) and self.pieces[i+k][j-k] == '0'):
                            break
                    for k in range(1,8):
                        if self.Friendly(i+k,j-k) and (self.pieces[i+k][j-k] == target or self.pieces[i+k][j-k] == target2):
                            return True
                        elif not (self.onBoard(i+k,j-k) and self.pieces[i+k][j-k] == '0'):
                            break
                    for k in range(1,8):
                        if self.Friendly(i-k,j-k) and (self.pieces[i-k][j-k] == target or self.pieces[i-k][j-k] == target2):
                            return True
                        elif not (self.onBoard(i-k,j-k) and self.pieces[i-k][j-k] == '0'):
                            break 

                    return False
        return False



                           



                


    
    def prints(self):
        #pöydän tulostus testaus tarkoituksiin
        for i in range(0,8):
            print (self.pieces[i])
    
   
            







    


#alkutilanne
pieces =[['0' for i in range(8)] for j in range(8)]
pieces[0] = ["r","n","b","q","k","b","n","r"]
pieces[1] = ["p","p","p","p","p","p","p","p"]
pieces[6] = ["P","P","P","0","P","P","P","P"]
pieces[7] = ["R","N","B","Q","K","B","N","R"]
b =  board(pieces,True,[True,True,True,True])

b.move("a1a3")
b.moveInt(1,1,5,1)
b.legalContinuations()
b.prints()
