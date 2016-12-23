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
            if not letter in self.misses:
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
    def __init__(self, name, letters):
        self.name = name
        self.letters = list(letters)
        self.letters.reverse()

    def giveLetter(self):
        return self.letters.pop()

    def getName(self):
        return self.name

class HumanPlayer():
    def __init__(self, name):
        self.name = name

    def giveLetter(self):
        from getch import getch
        print('Your turn (please provide letter): ')
        return getch()

    def getName(self):
        return self.name

def game(players):
    hangman = Hangman(SimpleDictionary())
    hangman.startGame()

    playersCount = len(players)
    turns = 0
    while hangman.canPlay():
        player = players[turns % playersCount]
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
        turns += 1

    if hangman.win():
        print('%s guess the word "%s" and win' % (player.getName(), hangman.getActualWord()))
    else:
        print('%s lost' % player.getName())

game([HumanPlayer('Mr. Brown'), Player('Mr. White', 'asdfghjklqwertyuiopzxcvbnm')])
