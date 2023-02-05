testWords = ["how does the character feel?",["upset","cheerful","angry"],"what is the summary of this story?",["he goes shopping","she goes to the cinema","he stays at home"],"who is the nicest",["mum","dad","brother",],"what is the weather",["sunny","raining","cold"],"why did he want to stay",["play","draw","sing"]]
answers = ["B","C","A","C","A"]
skills = ["emotions","summarising","inferencing","fact recall","understanding"]
improvement = []
emotions = 0
summarising = 0
inferencing = 0
factRecall = 0
understanding = 0


correctAnswersCounter = 0
j = 0
k = 0
for i in range(0,10,2):
    
    print(testWords[i])
    print("A:",testWords[i+1][k])
    print("B:",testWords[i+1][k+1])
    print("C:",testWords[i+1][k+2])

    testWordsUserAnswers = input("Enter your answer here: ").upper()

    if answers[j] != testWordsUserAnswers:
        improvement.append(skills[j])

    else:
        correctAnswersCounter = correctAnswersCounter + 1

    j = j+1

if correctAnswersCounter < 5:
    print("The reading skills you need to improve are:")
    for i in range(len(improvement)):
        print(improvement[i])

        
    improvementArray = []

    for i in range(len(improvement)):
        if improvement[i] == "emotions":
            emotions = emotions + 1

        elif improvement[i] == "summarising":
            summarising = summarising + 1

        elif improvement[i] == "inferencing":
            inferencing = inferencing + 1

        elif improvement[i] == "understanding":
            understanding = understanding + 1

        else:
            factRecall = factRecall + 1

    improvementArray.append(emotions)
    improvementArray.append(summarising)
    improvementArray.append(inferencing)
    improvementArray.append(factRecall)
    improvementArray.append(understanding)

    largest = 0
    for i in range(5):
        if improvementArray[i] > largest:
            largest = improvementArray[i]
            
    if largest > 0:
        largestCounter = 0
        improvementArrayiValues = []
        for i in range(5):
            if improvementArray[i] == largest:
                largestCounter = largestCounter + 1
                improvementArrayiValues.append(skills[int(i)])

        print("Your main skill to work on is",improvementArrayiValues)
