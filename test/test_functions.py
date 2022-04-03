import unittest
from src.functions import is_anagram, invert, is_palidromo


class TestFunctions(unittest.TestCase):
    def setUp(self):
        self.listWordsCorrect: list[list[str]] = [['fresa', 'frase'], ['sentido', 'destino'],['rocoso', 'cosoro']]
        self.listWordsIncorrect: list[list[str]] = [['rocoso', 'cosaro'], ['frresa', 'frase'], ['senyido', 'destino']]
        self.palidromo: list[str] = ['radar', 'sacas', 'reconocer', 'añora la roña']
        pass

    def test_anagram(self):
        for _list in self.listWordsCorrect:
            with self.subTest():
                self.assertEqual(is_anagram(_list[0], _list[1]), True, 'Detección de anagrama: Passed')
        for _list in self.listWordsIncorrect:
            with self.subTest():
                self.assertEqual(is_anagram(_list[0], _list[1]), False)
    pass

    def test_invert(self):
        self.assertEqual(invert('Hola mundo'), 'odnum aloH')
        self.assertEqual(invert('estoy probando'), 'odnaborp yotse')
        
    def test_is_palindromo(self):
        for _list in self.palidromo:
            with self.subTest():
                self.assertEqual(is_palidromo(_list), True)
        self.assertEqual(is_palidromo('rosa'), False)


if __name__ == '__main__':
    unittest.main()
