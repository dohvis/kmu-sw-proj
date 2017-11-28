class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.guessedChars = []
        self.secretWord = word
        self.currentStatus = '_ ' * len(word)
        pass


    def display(self):
        print("Current:", self.currentStatus)
        print("Tries:", self.numTries)
        print("Answer:", self.secretWord)


    def guess(self, character):
        self.guessedChars.append(character)
        self.setCurrent()
        if character not in self.secretWord:
            self.numTries += 1
        return '_' not in self.currentStatus

    def setCurrent(self):
        self.currentStatus = ''
        for char in self.secretWord:
            if char in self.guessedChars:
                self.currentStatus += char + ' '
            else:
                self.currentStatus += '_ '
