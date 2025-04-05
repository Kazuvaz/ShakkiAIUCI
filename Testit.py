import ShakkiAIUCI
import random
#pelaa satunnaisia siirtoja n kertaa tulostaa siirrot. tulostaa myös laudan tilan alussa ja lopussa
def randomMoves(n : int, lauta : ShakkiAIUCI.board):
    print()
    lautab : ShakkiAIUCI.board= lauta
    lautab.prints()
    for i in range(0,n):
        con : list=  lautab.trimmedContinuations()
        #jos kuningas puuttuu pöydältä 
        test = False
        for l in range(0,8):
            if 'k' in lautab.pieces[l]:
                test = True
        if not test:
            print("what?")
            break
                

        if len(con) == 0:
            print("mate")
            break 
        lautab = con[random.randrange(0,len(con))]
        print(lautab.prev )
    lautab.prints()

#kaikki mahdolliset siirrot tilanteesta lauta
def allMoves(lauta : ShakkiAIUCI.board):
    con : list=  lauta.trimmedContinuations()
    for a in con:
        p : ShakkiAIUCI.board = a
        print(p.prev)
        



#alkutilanne
pieces =[['0' for i in range(8)] for j in range(8)]
pieces[0] = ["r","n","b","q","k","b","n","r"]
pieces[1] = ["p","p","p","p","p","p","p","p"]
pieces[6] = ["P","P","P","P","P","P","P","P"]
pieces[7] = ["R","N","B","Q","K","B","N","R"]
opening =  ShakkiAIUCI.board(pieces,True,[True,True,True,True])

#tilanne custom
pieces[0] = ["0","0","0","0","0","0","0","0"]
pieces[1] = ["0","k","0","0","0","0","0","0"]
pieces[2] = ["0","0","0","0","0","0","0","0"]
pieces[3] = ["0","0","0","0","0","0","0","0"]
pieces[4] = ["0","0","0","0","0","0","0","0"]
pieces[5] = ["0","0","0","0","0","0","0","0"]
pieces[6] = ["0","0","0","0","0","K","P","0"]
pieces[7] = ["0","0","0","0","0","0","0","0"]
customPosition =  ShakkiAIUCI.board(pieces,True,[False,False,False,False])

#allMoves(opening)
randomMoves(600,opening)

#allMoves(customPosition)
#randomMoves(3000,customPosition)