class Guess:
    def __init__(self, word: str):
        self.secretWord = word
        self.guessedChars = []
        self.numTries = 0
        self.currentStatus = "_" * len(word)

    def display(self):
        print("Current:", self.currentStatus)
        print("Tries:", self.numTries)

    def guess(self, character):
        if character in self.secretWord:
            tmp = ""
            for index, one_character in enumerate(self.secretWord):
                if character == one_character:
                    tmp += one_character
                else:
                    tmp += self.currentStatus[index]
            self.currentStatus = tmp
        else:
            self.numTries += 1

        self.guessedChars.append(character)
        if "_" not in self.currentStatus:
            return True
        # 아직 빈칸을 다 못채웠다면
        else:
            return False
