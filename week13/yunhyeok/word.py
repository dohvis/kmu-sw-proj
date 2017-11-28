import random


class Word:
    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        print('%d words in DB' % self.count)

    def randFromDB(self):
        # r = random.randrange(self.count) 이렇게 하면 구간의 끝도 포함하는 난수가 생성되기 때문에 인덱스 에러가 발생할 수 있지 않나?
        r = random.randrange(self.count - 1)
        return self.words[r]
