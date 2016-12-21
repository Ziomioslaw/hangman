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
        self.misses = []

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
            self.misses.append(letter)

        return result

    def getChances(self):
        return self.chances

    def getMisses(self):
        return self.misses

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

    def getName(self):
        return 'Mr. White'

def game(player):
    hangman = Hangman(SimpleDictionary())
    hangman.startGame()

    while hangman.canPlay():
        print('Word: "%s" Chances: %d' % (hangman.getActualWord(), hangman.getChances()))
        print('Misses: %s' % ', '.join(hangman.getMisses()))
        letter = player.giveLetter()

        print('%s gives letter: "%c"' % (player.getName(), letter))
        result = hangman.giveLetter(letter)
        if result:
            print('The letter "%c" found' % letter)
        else:
            print('Letter "%c" not present in word' % letter)

        print

    if hangman.win():
        print('%s win' % player.getName())
    else:
        print('%s lost' % player.getName())

game(Player('asdfghjklqwertyuiopzxcvbnm'))
