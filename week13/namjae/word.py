import random

class Word:

    def __init__(self, filename):

        self.words = []
        self.count = 0

        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.words = [line.rstrip() for line in lines]
        self.count = len(self.words)

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self):

        r = random.randrange(self.count)
        return self.words[r]
