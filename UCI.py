import ShakkiAIUCI
import threading
import time
import MinMaxTree
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
        #add conditions to check wether previous commands are done
        if True:
            print('readyok')
    elif command == 'ucinewgame':
        currentState = ShakkiAIUCI.board(pieces,True,[True,True,True,True])
    elif command.startswith('position '):
        splat = command.split(' ')
        moveCount = 0
        for s in range(currentMoveIndex, len(splat)):
            print("see " + splat[s])
            currentState.move(splat[s]) 
            moveCount += 1
        currentMoveIndex += moveCount
    elif command.startswith('go'):
        tim = time.time()
        puu : MinMaxTree.Node = MinMaxTree.Node(currentState)
        while True:
            if time.time()-tim > 1:
                break
            puu.sprout()
        puu.bestMove()



         


    