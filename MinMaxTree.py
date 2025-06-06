import ShakkiAIUCI
import Evaluator
import random
class Node():
    board :ShakkiAIUCI.board
    value : int = 0
    children = []
    scariest : int = -1
    exploreTime =0
    def __init__(self, board : ShakkiAIUCI.board):
        self.board = board
        self.value = Evaluator.evaluate(self.board)
        self.children = []
        self.exploreTime =1
    def sprout(self):
        self.exploreTime += 1
        #jos ei ole lapsia ne luodaan
        if len(self.children) == 0:
            possibleBoards = self.board.trimmedContinuations()
            for board in possibleBoards:
                self.children.append(Node(board))
            if len(self.children) == 0:
                self.value = -9999
                return 
        else:
            #viedään sprout lapselle joka vaikuttaa vaarallisimmalta
            #bestNode : Node = self.children[self.scariest]
            #bestNode.sprout()

            scary : float = 0
            best = -9999
            #exploration tekee hauta leveän 
            exploration = 999999
            for i in range(0,len(self.children)):
                a : Node = self.children[i]
                if a.exploreTime < exploration or a.exploreTime == exploration and (a.value*-1 > best or a.value*-1 == best and random.randint(0,1)== 0 ) :
                    best = a.value*-1
                    scary = i
                    exploration = a.exploreTime
            bestNode : Node = self.children[scary]
            bestNode.sprout()
        self.valueChildren()

    #antaa uuden arvon parhaan lapsen perusteella
    def valueChildren(self):
        best = -999999
        scary : float = 0
        for i in range(0,len(self.children)):
            a : Node = self.children[i]
            if a.value*-1 > best or a.value*-1 == best and random.randint(0,1)== 0:
                best = a.value*-1
                scary = i
        self.scariest = scary
        #laitetaan oma arvo paras lapsi kerrotaan -1 koska seuraavan vuoron hyvä arvo on huono tämäb vuoron pelaajalle
        self.value = best
    
    def bestLine(self):
        #testifunktio linjojen seuraukseen
        print(self.board.prev + " " + str(self.value) )
        if len(self.children) == 0:
            return
        bestNode : Node = self.children[self.scariest]
        
        bestNode.bestLine()
    def bestMove(self):
        if len(self.children) == 0:
            return
        bestNode : Node = self.children[self.scariest]
        #tämä prittaus on tässä vaan koska encroissant tarvitsee jonkin sortin evaluoinnin pelaamiseen ja ei jostain syystä ota siirtoa "bestmove: " palautteesta
        print("info depth 1 seldepth 2 multipv 1 score cp 0 nodes 20 nps 20000 hashfull 0 tbhits 0 time 1 pv "+ bestNode.board.prev)
        print ("bestmove " +bestNode.board.prev + " ponder " + bestNode.children[bestNode.scariest].board.prev)
        










    

