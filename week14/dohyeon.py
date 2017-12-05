import unittest

from guess import Guess


class TestGuess(unittest.TestCase):

    def setUp(self):
        self.g1 = Guess('default')

    def tearDown(self):
        pass

    def testDisplayCurrent(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('f')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u _ t ')
        self.g1.guess('l')
        self.assertEqual(self.g1.displayCurrent(), 'd e f a u l t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

    def testGuess(self):
        self.assertTrue(self.g1.guess('d'))
        self.assertFalse(self.g1.guess('z'))
        # 리턴값이 올바른가?

        self.assertEqual('de%s' % ("_" * (len('default') - 2)), self.g1.currentStatus)

        # 부분적으로 맞추어진 단어의 상태가 올바르게 유지되는가?
        self.assertEqual({'e', '', 'n', 'd', 'z'}, self.g1.guessedChars)
        # 이용된 글자들의 집합을 나타내는 데이터는 올바르게 유지되는가?

        for c in "efault":
            self.g1.guess(c)
        is_finished = self.g1.finished()
        self.assertTrue(is_finished)
        # 단어의 전체를 다 맞춘 경우에 대한 처리가 올바른가?

        if __name__ == '__main__':
            unittest.main()

