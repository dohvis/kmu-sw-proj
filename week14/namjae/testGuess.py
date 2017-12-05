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

        self.g1.guess('a')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('c')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('D')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('가')
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess(' ')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.g1.guess('*')
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')

    def testDisplayGuessed(self):
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.g1.guess('t')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.g1.guess('u')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')

        self.g1.guess('a')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.g1.guess('c')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')
        self.g1.guess('D')
        self.assertEqual(self.g1.displayGuessed(), ' D a c e n t u ')
        self.g1.guess('가')
        self.assertEqual(self.g1.displayGuessed(), ' D a c e n t u 가 ')
        self.g1.guess('d')
        self.assertEqual(self.g1.displayGuessed(), ' D a c d e n t u 가 ')
        self.g1.guess(' ')
        self.assertEqual(self.g1.displayGuessed(), '   D a c d e n t u 가 ')
        self.g1.guess('*')
        self.assertEqual(self.g1.displayGuessed(), '   * D a c d e n t u 가 ')

    def testGuess(self):
        self.assertEqual(self.g1.displayCurrent(), '_ e _ _ _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' e n ')
        self.assertTrue(self.g1.guess('a'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ _ ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n ')
        self.assertTrue(self.g1.guess('t'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a _ _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t ')
        self.assertTrue(self.g1.guess('u'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a e n t u ')
        self.assertFalse(self.g1.guess('c'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' a c e n t u ')
        self.assertFalse(self.g1.guess('D'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' D a c e n t u ')
        self.assertFalse(self.g1.guess('가'))
        self.assertEqual(self.g1.displayCurrent(), '_ e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' D a c e n t u 가 ')
        self.assertTrue(self.g1.guess('d'))
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), ' D a c d e n t u 가 ')
        self.assertFalse(self.g1.guess(' '))
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), '   D a c d e n t u 가 ')
        self.assertFalse(self.g1.guess('*'))
        self.assertEqual(self.g1.displayCurrent(), 'd e _ a u _ t ')
        self.assertEqual(self.g1.displayGuessed(), '   * D a c d e n t u 가 ')

        self.assertFalse(self.g1.finished())
        self.g1.guess('f')
        self.assertFalse(self.g1.finished())
        self.g1.guess('l')
        self.assertTrue(self.g1.finished())

if __name__ == '__main__':
    unittest.main()
