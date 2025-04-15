import ShakkiAIUCI
import math
def evaluate(board : ShakkiAIUCI.board):
    score : float = 0
    score += pieceScore(board)
    score += (activity(board)/10)
    return score


def activity(board : ShakkiAIUCI.board):
    #tässä kestää kauan pitää varmaan keksiä parempi tapa mitata aktiivisuutta
    score : float= 0
    for i in range(0,8):
            for j in range(0,8):
                if knightReach(board,i,j,"N"):
                    score +=2.5
                if knightReach(board,i,j,"n"):
                    score -=2.5
                score += rookReach(board,i,j)
                score += bishopReach(board,i,j)
    if not board.turn:
        score = score*-1
    return score

#nämä reach funktiot on käytännössä kierrätettyjä ja vähän muutettuja versiota shakkiaiuci.py legalin varmistuksista
def knightReach(board : ShakkiAIUCI, i:int,j:int, s :str):
    return(
        board.onBoard(i+2,j+1) and board.pieces[i+2][j+1] == s or board.onBoard(i+2,j-1) and board.pieces[i+2][j-1] == s 
        or board.onBoard(i-2,j+1) and board.pieces[i-2][j+1] == s or board.onBoard(i-2,j-1) and board.pieces[i-2][j-1] == s
        or board.onBoard(i+1,j+2) and board.pieces[i+1][j+2] == s or board.onBoard(i-1,j+2) and board.pieces[i-1][j+2] == s 
        or board.onBoard(i+1,j-2) and board.pieces[i+1][j-2] == s or board.onBoard(i-1,j-2) and board.pieces[i-1][j-2] == s
    )

def rookReach(board : ShakkiAIUCI, i:int,j:int):
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

def bishopReach(board : ShakkiAIUCI, i:int,j:int):
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
#laitan nämä samaan paikkaan että voin helposti muokata arvoja tulevaisuudessa.
def scoreRookReacher(s :str):
    if s == 'r':
        return -3
    elif s == 'R':
        return 3
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
        return -2.5
    elif s == 'B':
        return 2.5
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
   
    if not board.turn:
        score = -1 *score
    return score
