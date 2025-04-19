import ShakkiAIUCI
import random
import MinMaxTree
import Evaluator
import unittest

#pelaa satunnaisia siirtoja n kertaa tulostaa siirrot. tulostaa myös laudan tilan alussa ja lopussa
class TestShakkiAIUCI(unittest.TestCase):
    opening : ShakkiAIUCI.board
    def setUp(self):
        #alkutilanne
        pieces =[['0' for i in range(8)] for j in range(8)]
        pieces[0] = ["r","n","b","q","k","b","n","r"]
        pieces[1] = ["p","p","p","p","p","p","p","p"]
        pieces[6] = ["P","P","P","P","P","P","P","P"]
        pieces[7] = ["R","N","B","Q","K","B","N","R"]
        self.opening =  ShakkiAIUCI.board(pieces,True,[True,True,True,True])
        return

    def test_loytaa_kaikki_siirrot_aloituksessa(self):
        maara = len(self.opening.legalContinuationsUntrimmed())
        self.assertEqual(maara, 20)

    def test_vuoro_vaihtuu(self):
        self.assertEqual(self.opening.turn,True)
        self.opening.move('a1a1')
        self.assertEqual(self.opening.turn,False)
    def test_linnoitus_loytyy(self):
        self.opening.move('f1f3')
        self.opening.move('g1g3')
        he : bool = 'e1g1' in self.opening.legalContinuationsUntrimmed()
        self.assertEqual(he,True)
    def test_MoukkaSyo(self):
        self.opening.move('e2e4')
        self.opening.move('d7d5')
        he : bool = 'e4d5' in self.opening.legalContinuationsUntrimmed()
        self.assertEqual(he,True)



tes = TestShakkiAIUCI()
tes.setUp()
tes.test_MoukkaSyo

'''
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

#opening.move('e2e3')
print("ss")
opening.move('d2d4')
opening.move('d7d5')
opening.move('e2e4')
opening.move('d5e4')
opening.move('f1b5')
opening.move('c7c6')
opening.move('b5c4')
opening.move('d8a5')
opening.move('e1f1')


evaluate(300,opening)




customPosition.move("g2h3")
customPosition.move("g4h3")
customPosition.prints()
print( Evaluator.evaluate(customPosition))
'''