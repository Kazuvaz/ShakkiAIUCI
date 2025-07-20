import ShakkiAIUCI
import random
import MinMaxTree
import Evaluator
import unittest
import MiniMax
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

    def test_LoytaaMatinSyvyys1(self):
        pieces =[['0' for i in range(8)] for j in range(8)]
        pieces[0] = ["r","n","b","q","k","0","0","r"]
        pieces[1] = ["p","p","p","p","0","p","p","p"]
        pieces[2] = ["0","0","0","0","0","n","0","0"]
        pieces[3] = ["0","0","b","0","p","0","0","Q"]
        pieces[4] = ["0","0","B","0","P","0","0","0"]
        pieces[5] = ["0","0","0","0","0","0","0","0"]
        pieces[6] = ["P","P","P","P","0","P","P","P"]
        pieces[7] = ["R","N","B","0","K","0","N","R"]
        customPosition =  ShakkiAIUCI.board(pieces,True,[False,False,False,False])
        self.assertEqual(MiniMax.minimaxFirst(customPosition, 2,-99999,99999)[0],"h5f7 end")
    def test_LoytaaMatinSyvyys2(self):
        pieces =[['0' for i in range(8)] for j in range(8)]
        pieces[0] = ["k","0","0","0","0","0","0","r"]
        pieces[1] = ["p","p","0","0","0","0","0","0"]
        pieces[2] = ["N","0","0","0","0","0","0","0"]
        pieces[3] = ["0","0","0","0","0","0","0","0"]
        pieces[4] = ["0","0","0","0","0","0","0","0"]
        pieces[5] = ["q","0","0","0","0","0","Q","0"]
        pieces[6] = ["r","0","0","0","0","0","0","0"]
        pieces[7] = ["0","0","0","0","0","0","K","0"]
        customPosition =  ShakkiAIUCI.board(pieces,True,[False,False,False,False])
        self.assertEqual(MiniMax.minimaxFirst(customPosition, 4,-99999,99999)[0],"g3b8 h8b8 a6c7 end")
    def test_puolustaaSyvyyden2sisällä(self):
        #tilanne on jokatapuksessa hävitty mutta löytääkö AI selviämisen syvyytensä sisällä
        pieces =[['0' for i in range(8)] for j in range(8)]
        pieces[0] = ["0","0","0","0","0","0","0","0"]
        pieces[1] = ["0","0","0","0","0","0","0","0"]
        pieces[2] = ["0","0","0","0","0","0","0","0"]
        pieces[3] = ["0","0","q","0","0","0","0","0"]
        pieces[4] = ["0","0","0","0","0","0","0","0"]
        pieces[5] = ["0","k","0","p","0","0","0","0"]
        pieces[6] = ["0","0","0","P","0","0","0","r"]
        pieces[7] = ["0","0","0","0","K","R","0","0"]
        customPosition =  ShakkiAIUCI.board(pieces,True,[False,False,False,False])
        self.assertEqual(MiniMax.minimaxFirst(customPosition, 4,-99999,99999)[0].split(' ')[0],"e1d1")
    

