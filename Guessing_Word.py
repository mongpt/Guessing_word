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

