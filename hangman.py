class SimpleDictionary():
    def getWord(self):
        return 'Hangman'.lower()

class Hangman():
    STARTING_CHANCES_NUMBER = 6

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def startGame(self):
        self.word = self.dictionary.getWord()
        self.visibleWord = list('_' * len(self.word))
        self.chances = Hangman.STARTING_CHANCES_NUMBER

    def giveLetter(self, letter):
        result = False
        x = 0
        for char in self.word:
            if char == letter:
                self.visibleWord[x] = char
                result = True

            x += 1

        if not result:
            self.chances -= 1

        return result

    def getActualWord(self):
        return ''.join(self.visibleWord)

    def canPlay(self):
        return not self.win() and self.chances > 0

    def win(self):
        return self.getActualWord() == self.word

class Player():
    def __init__(self, letters):
        self.letters = list(letters)
        self.letters.reverse()

    def giveLetter(self):
        return self.letters.pop()

def game(player):
    hangman = Hangman(SimpleDictionary())
    hangman.startGame()

    while hangman.canPlay():
        hangman.giveLetter(player.giveLetter())

    return hangman.win()

print(game(Player('asdfghjklqwertyuiopzxcvbnm')))
