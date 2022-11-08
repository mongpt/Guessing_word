# Guessing_word
Try to input single character that may in a guessing word until you have filled it
```python
import random

wordList = ["apple", "banana", "castle", "president", "engineer", "university", "school", "capital"]
randomWord = random.choice(wordList)
resultList = []
for i in randomWord:
    resultList.append("_")
print("A new word =",resultList)
while "_" in resultList:
    guess = input("Guess a letter of this word: ")
    if guess in randomWord:
        for i in range(len(randomWord)):
            if guess == randomWord[i]:
                resultList[i] = guess
    print("A new word =",resultList)
print(">>>>>>>",randomWord,"<<<<<<<")
```
Output console:
```
A new word = ['_', '_', '_', '_', '_', '_']
Guess a letter of this word: u
A new word = ['_', '_', '_', '_', '_', '_']
Guess a letter of this word: a
A new word = ['_', 'a', '_', '_', '_', '_']
Guess a letter of this word: c
A new word = ['c', 'a', '_', '_', '_', '_']
Guess a letter of this word: p
A new word = ['c', 'a', '_', '_', '_', '_']
Guess a letter of this word: s
A new word = ['c', 'a', 's', '_', '_', '_']
Guess a letter of this word: t
A new word = ['c', 'a', 's', 't', '_', '_']
Guess a letter of this word: l
A new word = ['c', 'a', 's', 't', 'l', '_']
Guess a letter of this word: e
A new word = ['c', 'a', 's', 't', 'l', 'e']
>>>>>>> castle <<<<<<<
```
