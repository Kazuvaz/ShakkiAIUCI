import ShakkiAIUCI
import Evaluator

def minimax(board :  ShakkiAIUCI.board, depth : int,alpha, beta):
    if depth == 0:
        #tämä sotku tarkistaa eka että onko shakissa ja sitten matin, matin tarkastus on raskas prosessi joten se täytyy erikseen vain tilenteissa josa on shakki
        board.turn = not board.turn
        if board.impossible():
            board.turn = not board.turn
            if len(board.trimmedContinuations()) == 0:
                if board.turn:
                    return 99999
                else:
                    return -99999
        board.turn = not board.turn
        return Evaluator.turnBlindEvaluate(board)
    continuations : list = board.trimmedContinuations()
    if len(continuations) == 0:
        board.turn = not board.turn
        if board.impossible():
            if board.turn:
                return 99999
            else:
                return -99999
        return 0
    if board.turn:
        value = -999999
        for b in continuations:
            tempValue = minimax(b, depth-1,alpha,beta)
            if tempValue > value:
                value = tempValue
                cast : ShakkiAIUCI.board = b
            if value >= beta:
                break
            alpha = max(value, alpha)
        return value
    else:
        value = 999999
        for b in continuations:
            tempValue = minimax(b, depth-1,alpha,beta)
            if tempValue < value:
                value = tempValue
                cast : ShakkiAIUCI.board = b
            if value <= alpha:
                break
            beta = max(value, beta)
        return value
#päätin tehdä ekan kerroksen erikseen jottei siirtojen tietoja tarvi palautella jokakerroksella
def minimaxFirst(board :  ShakkiAIUCI.board, depth : int,alpha, beta):
    if depth == 0:
        #tämä sotku tarkistaa eka että onko shakissa ja sitten matin, matin tarkastus on raskas prosessi joten se täytyy erikseen vain tilenteissa josa on shakki
        board.turn = not board.turn
        if board.impossible():
            board.turn = not board.turn
            if len(board.trimmedContinuations()) == 0:
                if board.turn:
                    return ('end',99999)
                else:
                    return ('end',-99999)
        board.turn = not board.turn
        return ('end', Evaluator.turnBlindEvaluate(board))
    continuations : list = board.trimmedContinuations()
    if len(continuations) == 0:
        board.turn = not board.turn
        if board.impossible():
            if board.turn:
                return ('end',99999)
            else:
                return ('end',-99999)
        return ('draw',0)
    if board.turn:
        value = ("",-999999)
        moveSyntax = ''
        for b in continuations:
            tempValue = minimaxFirst(b, depth-1,alpha,beta)
            
            if tempValue[1] > value[1]:
                value = tempValue
                cast : ShakkiAIUCI.board = b
                moveSyntax = cast.prev
            if value[1] >= beta:
                break
            alpha = max(value[1], alpha)
        return (moveSyntax +" " + value[0],value[1])
    else:
        moveSyntax = ''
        value = ("",999999)
        for b in continuations:
            tempValue = minimaxFirst(b, depth-1,alpha,beta)
            if tempValue[1] < value[1]:
                value = tempValue
                cast : ShakkiAIUCI.board = b
                moveSyntax =cast.prev
            if value[1] <= alpha:
                break
            beta = max(value[1], beta)
        return (moveSyntax+" " + value[0],value[1])

