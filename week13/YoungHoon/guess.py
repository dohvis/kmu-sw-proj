class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.guessedChars = set()
        self.numTries = 0
        self.wordList = ["_" for i in range(len(word))]
        self.currentStatus = "".join(self.wordList)


    def display(self):
        print("Current:", self.currentStatus)
        print("Tries: %d" % self.numTries)


    def guess(self, character):
        self.guessedChars.add(character)  # 집합에 단어 추가
        idx = 0

        if character in self.secretWord:  # 존재 할 경우
            for chr in self.secretWord:  # 위치 찾기
                if chr == character:
                    self.wordList[idx] = self.secretWord[idx]
                    idx += 1
                else:
                    idx += 1

            self.currentStatus = "".join(self.wordList)  # 현재 상태 업데이트

            if self.currentStatus == self.secretWord:  # 정답 체크
                return True
        else:
            self.numTries += 1  # 존재하지 않을 경우

            if self.numTries == 6:  # 기회 모두 소진
                return False
