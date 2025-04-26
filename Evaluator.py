import ShakkiAIUCI
import math
def evaluate(board : ShakkiAIUCI.board):
    score : float = 0
    score += pieceScore(board)
    score += (activity(board)/20)
    if not board.turn:
        score = score*-1
    return score

def turnBlindEvaluate(board : ShakkiAIUCI.board):
    score : float = 0
    score += pieceScore(board)
    score += (activity(board)/20)
    return score

#käytännössä jakaa pöydän ruutucontrollin mukaan 
def activity(board : ShakkiAIUCI.board):
    #tässä kestää kauan pitää varmaan keksiä parempi tapa mitata aktiivisuutta
    score : float= 0
    for i in range(0,8):
            for j in range(0,8):
                localScore = 0 
                if knightReach(board,i,j,"N"):
                    localScore +=3
                if knightReach(board,i,j,"n"):
                    localScore -=3
                localScore  += rookReach(board,i,j)
                localScore  += bishopReach(board,i,j)
                localScore += pawnReach(board,i,j)
                if localScore > 0:
                    score += 1
                elif localScore <0:
                    score -=1
    return score
                
    

#nämä reach funktiot on käytännössä kierrätettyjä ja vähän muutettuja versiota shakkiaiuci.py legalin varmistuksista
def knightReach(board : ShakkiAIUCI.board, i:int,j:int, s :str):
    return(
        board.onBoard(i+2,j+1) and board.pieces[i+2][j+1] == s or board.onBoard(i+2,j-1) and board.pieces[i+2][j-1] == s 
        or board.onBoard(i-2,j+1) and board.pieces[i-2][j+1] == s or board.onBoard(i-2,j-1) and board.pieces[i-2][j-1] == s
        or board.onBoard(i+1,j+2) and board.pieces[i+1][j+2] == s or board.onBoard(i-1,j+2) and board.pieces[i-1][j+2] == s 
        or board.onBoard(i+1,j-2) and board.pieces[i+1][j-2] == s or board.onBoard(i-1,j-2) and board.pieces[i-1][j-2] == s
    )

def rookReach(board : ShakkiAIUCI.board, i:int,j:int):
    score = 0
    for k in range(1,8):
        if not board.onBoard(i,j+k):
            break
        elif not board.pieces[i][j+k] == '0':
            score += scoreRookReacher(board.pieces[i][j+k])
            break
    for k in range(1,8):
        if not board.onBoard(i,j-k):
            break
        elif not board.pieces[i][j-k] == '0':
            score += scoreRookReacher(board.pieces[i][j-k])
            break
    for k in range(1,8):
        if not board.onBoard(i+k,j):
            break
        elif not board.pieces[i+k][j] == '0':
            score += scoreRookReacher(board.pieces[i+k][j])
            break
    for k in range(1,8):
        if not board.onBoard(i-k,j):
            break
        elif not board.pieces[i-k][j] == '0':
            score += scoreRookReacher(board.pieces[i-k][j])
            break
    return score

def bishopReach(board : ShakkiAIUCI.board, i:int,j:int):
    score = 0
    for k in range(1,8):
        if not board.onBoard(i+k,j+k):
            break
        elif not board.pieces[i+k][j+k] == '0':
            score += scoreBishopReacher(board.pieces[i+k][j+k])
            break
    for k in range(1,8):
        if not board.onBoard(i+k,j-k):
            break
        elif not board.pieces[i+k][j-k] == '0':
            score += scoreBishopReacher(board.pieces[i+k][j-k])
            break
    for k in range(1,8):
        if not board.onBoard(i-k,j+k):
            break
        elif not board.pieces[i-k][j+k] == '0':
            score += scoreBishopReacher(board.pieces[i-k][j+k])
            break
    for k in range(1,8):
        if not board.onBoard(i-k,j-k):
            break
        elif not board.pieces[i-k][j-k] == '0':
            score += scoreBishopReacher(board.pieces[i-k][j-k])
            break 
    return score

def pawnReach(board: ShakkiAIUCI.board, i:int,j:int):
    score = 0
    if(board.onBoard(i-1,j-1) and board.pieces[i-1][j-1] == 'p') or (board.onBoard(i-1,j+1) and board.pieces[i-1][j+1] == 'p'):
        score -=4
    if(board.onBoard(i+1,j-1) and board.pieces[i-1][j-1] == 'p') or (board.onBoard(i+1,j+1) and board.pieces[i-1][j+1] == 'P'):
        score +=4
    return score


#laitan nämä samaan paikkaan että voin helposti muokata arvoja tulevaisuudessa.
def scoreRookReacher(s :str):
    if s == 'r':
        return -2
    elif s == 'R':
        return 2
    elif s == 'q':
        return -1
    elif s == 'Q':
        return 1
    return 0

def scoreBishopReacher(s :str):
    if s == 'q':
        return -1
    elif s == 'Q':
        return 1
    elif s == 'b':
        return -3
    elif s == 'B':
        return 3
    return 0
def pieceScore(board : ShakkiAIUCI.board):
    
    score = 0
    
    for i in range(0,8):
            for j in range(0,8):
                suspect :str = board.pieces[i][j]
                if suspect == 'n' or suspect == 'b':
                    score -= 3
                elif suspect == 'N' or suspect == 'B':
                    score +=3
                elif suspect == 'p':
                    score -=1
                elif suspect == 'P':
                    score +=1
                elif suspect == 'q':
                    score -=9
                elif suspect == 'Q':
                    score +=9
                elif suspect == 'r':
                    score -=5
                elif suspect == 'R':
                    score +=5
    #kerrotaan vuoron perusteella joten ei tarvitse joka summauksessa tarkastaa vuoroa
   
    return score
