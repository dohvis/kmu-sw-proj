import unittest

from guess import Guess


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('minimum')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        # self.assertEqual(len(self.g1.displayCurrent()), 14)
        self.assertEqual(self.g1.displayCurrent(), '_ _ n _ _ _ _ ')
        # 중복되는 character도 정상적으로 추가되는지 확인
        self.g1.guess('m')
        self.assertEqual(self.g1.displayCurrent(), 'm _ n _ m _ m ')
        # secretword에 없는 character는 추가안되는 지 확인
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), 'm _ n _ m _ m ')
        # 중복되는 character도 정상적으로 들어나는 것을 이미 확인했으니 사실상 밑의 과정은 의미없다.
        self.g1.guess('i')
        self.assertEqual(self.g1.displayCurrent(), 'm i n i m _ m ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), 'm i n i m u m ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        # 정상적으로 추가되는지 확인
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        # 중복해서 추가안되는지 확인
        self.g1.guess("a")
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        # 밑의 테스트는 이미 'a'가 추가되는 것을 확인했으니 의미없지 않나? sort가 제대로 되는지 확인?
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

    def testGuess1(self):
        # 리턴 값이 올바른지 체크
        self.assertTrue(self.g1.guess("m"))
        self.assertFalse(self.g1.guess("t"))

    def testGuess2(self):
        # 부분적으로 맞추어진 단어의 상태가 올바르게 유지되는지 체크
        self.assertEqual(self.g1.currentStatus, "__n____")
        self.g1.guess("m")
        self.assertEqual(self.g1.currentStatus, "m_n_m_m")
        self.g1.guess("t")
        self.assertEqual(self.g1.currentStatus, "m_n_m_m")

    def testGuess3(self):
        # 이용된 글자들의 집합을 나타내는 guessedChars가 올바르게 유지되는지 체크
        self.assertEqual(self.g1.guessedChars, {"e", "", "n"})
        self.g1.guess("m")
        self.assertEqual(self.g1.guessedChars, {"e", "", "m", "n"})
        self.g1.guess("o")
        self.assertEqual(self.g1.guessedChars, {"e", "", "m", "n", "o"})
        self.g1.guess("o")
        self.assertEqual(self.g1.guessedChars, {"e", "", "m", "n", "o"})

    def testGuess4(self):
        # 단어를 다 맞춘 경우에 대한 처리가 올바른지 체크
        self.g1.guess("m")
        self.g1.guess("i")
        self.g1.guess("u")

        self.assertFalse(self.g1.guess("o"))
        self.assertTrue(self.g1.guess("m"))
        self.assertEqual(self.g1.currentStatus, "minimum")


if __name__ == '__main__':
    unittest.main()
