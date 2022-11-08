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
                resultList.insert(i,guess)
                resultList.pop(i+1)
    print("A new word =",resultList)
print(">>>>>>>",randomWord,"<<<<<<<")
```
Output console:
```
A new word = ['_', '_', '_', '_', '_', '_']
Guess a letter of this word: e
A new word = ['_', '_', '_', '_', '_', '_']
Guess a letter of this word: a
A new word = ['_', 'a', '_', 'a', '_', 'a']
Guess a letter of this word: b
A new word = ['b', 'a', '_', 'a', '_', 'a']
Guess a letter of this word: n
A new word = ['b', 'a', 'n', 'a', 'n', 'a']
>>>>>>> banana <<<<<<<
```
