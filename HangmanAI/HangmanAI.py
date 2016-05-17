#! python3
# Hangman AI - Figures out the word of your choosing

from string import ascii_lowercase
import random, collections
def countLength():
    count = 0
    for words in wordsList:
        count += 1
    print(count)


def isWordInList(word):
    found = False
    for words in wordsList:
        if word == words:
            found = True
    if found is True:
        print('Word has been found')
    else:
        print('Cannot find word')

def removeWordsAtSpot(letter,spot):
    wordsList[:] = [value for value in wordsList if value[spot] is letter]


def removeWords(letter):
    wordsList[:] = [value for value in wordsList if letter not in value]

def checkIfUsed(letter):
    if letter not in alreadyUsed:
        return False
    else:
        return True


def getMostCommonLet():
    cList = []
    toBeCounted = ''
    for words in wordsList:
        toBeCounted += words
    for values in range(26):
        if checkIfUsed(collections.Counter(toBeCounted).most_common(26)[values][0]) == False:
            return collections.Counter(toBeCounted).most_common(26)[values][0]



vowelsChecked = 0
alreadyUsed = []
letterToRemove = ''

alphabet = [chars for chars in ascii_lowercase]
vowels = ['a', 'e', 'i', 'o', 'u']
alphabet.remove('a')
alphabet.remove('e')
alphabet.remove('i')
alphabet.remove('o')
alphabet.remove('u')


wordsList = open('words.txt').readlines()
for words in range(len(wordsList)):
    wordsList[words] = wordsList[words].rstrip()
print('Think of a word. Any word!')
wordLength = int(input('How many letters are in your word?'))
wordsList[:] = [value for value in wordsList if len(value) == wordLength]

guess = [None] * wordLength
while len(wordsList) != 1:
    letGuess = ''
    letGuess = getMostCommonLet()
    if input('Is the letter '+letGuess+' in your word? (y/n)') == 'y':  #Letter is in word
        howMany = int(input('How many times does this letter appear in your word?'))

        if howMany > 1: #letter appears multiple times
            for i in range(howMany):
                spot = int(input('what spot is it in? Starting at 1')) - 1
                guess[spot] = letGuess
                removeWordsAtSpot(letGuess, spot)
            alreadyUsed.append(letGuess)


        else:   #letter appears once in word
            spot = int(input('what spot is it in? Starting at 1')) - 1
            guess[spot] = letGuess
            removeWordsAtSpot(letGuess, spot)
            alreadyUsed.append(letGuess)

    else:   #Letter is not in word
        letterToRemove = letGuess
        removeWords(letterToRemove)
        alreadyUsed.append(letGuess)


print('\n\nI got it! Your word is '+wordsList[0])
isCorrect = input('Was my guess correct?(y/n)')
if isCorrect == 'y':
    print('Shut up baby, I know it.')
else:
    CorrectWord = input('What was your word so I can add it to my dictionary')
    with open('words.txt','a') as theFile:
        theFile.write('\n'+CorrectWord)
        print(CorrectWord+" added to dictionary!")
