import ShakkiAIUCI
import threading
import time
import MinMaxTree
import MiniMax
#alkutilanne
pieces =[['0' for i in range(8)] for j in range(8)]
pieces[0] = ["r","n","b","q","k","b","n","r"]
pieces[1] = ["p","p","p","p","p","p","p","p"]
pieces[6] = ["P","P","P","P","P","P","P","P"]
pieces[7] = ["R","N","B","Q","K","B","N","R"]
currentMoveIndex : int = 2
currentState : ShakkiAIUCI.board 

while True:
    command = input()
    command = command.lower()

    if command =='quit':
        break
    elif command == 'uci':
        print('id name TBD')
        print('id author Santeri K')
        print('only supports startpos')
        print('uciok')
    elif command == 'isready':
        #encroissaant ei pyydä ucinewgame ollenkaan joten alustan pelin tässä myös 
        currentState = ShakkiAIUCI.board(pieces,True,[True,True,True,True])
        #add conditions to check wether previous commands are done
        if True:
            print('readyok')
    elif command == 'ucinewgame':
        currentState = ShakkiAIUCI.board(pieces,True,[True,True,True,True])
    elif command.startswith('position '):
        splat = command.split(' ')
        temp : int = 0
        if splat[1] == 'fen':
            temp = 7
        moveCount = 0
        for s in range(currentMoveIndex + temp, len(splat)):
            currentState.move(splat[s]) 
            moveCount += 1
        currentMoveIndex += moveCount
    elif command.startswith('go'):
        move = (MiniMax.minimaxFirst(currentState,3,-99999,99999)[0])
        splat = move.split(' ')
        #tämä on vaan encroissanttia varten koska se ottaa parhaan siirron evaluonnista eika "bestmove " palautteesta evaluonnin teksti ei ole todenpitävä
        print("info depth 3 seldepth 2 multipv 1 score cp 0 nodes 20 nps 20000 hashfull 0 tbhits 0 time 1 pv " + splat[0])
        print("bestmove " +splat[0])

        



         


    