import ShakkiAIUCI
import random
import MinMaxTree
import Evaluator
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

def evaluate(n :int,lauta : ShakkiAIUCI.board):
    start : MinMaxTree.Node = MinMaxTree.Node(lauta)
    for i in range(0,n):
        start.sprout()
    for i in start.children:
        nod : MinMaxTree.Node = i
        #print(nod.board.prev + " " + str( nod.value))
    start.bestLine()




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
pieces[4] = ["0","0","0","0","0","0","p","0"]
pieces[5] = ["0","0","0","0","0","0","0","r"]
pieces[6] = ["0","0","0","0","0","K","P","0"]
pieces[7] = ["0","0","0","0","0","0","0","0"]
customPosition =  ShakkiAIUCI.board(pieces,True,[False,False,False,False])

#allMoves(opening)
#randomMoves(600,opening)

#allMoves(customPosition)
#randomMoves(3000,customPosition)


#evaluate(500,opening)

#customPosition.move("g2h3")
evaluate(50,opening)

'''


customPosition.move("g2h3")
customPosition.move("g4h3")
customPosition.prints()
print( Evaluator.evaluate(customPosition))
'''