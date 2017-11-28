class Guess:
    def __init__(self, word):
        self.numTries = 0
        self.guessedChars = []
        self.secretWord = word
        self.currentStatus = '*' * len(word)

    def display(self):
        # print(self.secretWord)
        print(self.guessedChars)
        print(''.join(self.currentStatus))

    def guess(self, character):
        self.guessedChars.append(character)
        _currentStatus = list(self.currentStatus)
        for idx, c in enumerate(self.secretWord):
            if character == c:
                _currentStatus[idx] = character
                self.currentStatus = ''.join(_currentStatus)
                if ''.join(self.currentStatus) == self.secretWord:
                    return True
        self.numTries += 1
        return False
