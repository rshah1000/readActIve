# survey
userName = input("What's your name: ")
userAge = int(input("How old are you: "))

# average reading level test

testWords = ["happy",["upset","cheerful","angry"],"always",["never","sometimes","every time"],"mother",["mum","dad","brother",],"corner",["face","side","point"],"capture",["take","return","stay"]]
answers = ["B","C","A","C","A"]
correctAnswerCounter = 0

j = 0
k = 0

for i in range(0,10,2):
    
    print("What does",testWords[i],"mean?")
    print("A:",testWords[i+1][k])
    print("B:",testWords[i+1][k+1])
    print("C:",testWords[i+1][k+2])

    testWordsUserAnswers = input("Enter your answer here: ").upper()

    if answers[j] == testWordsUserAnswers:
        correctAnswerCounter = correctAnswerCounter + 1

    j = j+1

if correctAnswerCounter <= 2:
    level = "beginner"

elif correctAnswerCounter <= 4:
    level = "medium"

else:
    level = "advanced"

print("Thank you for doing this survey, we will use it to optimise your learning with us!")

print(level)
