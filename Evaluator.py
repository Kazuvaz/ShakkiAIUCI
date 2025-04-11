import ShakkiAIUCI

def evaluate(board : ShakkiAIUCI.board):
    score : int = 0
    score += pieceScore(board)

    return score


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
