Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ## stories

import time
import openai

openai.api_key = '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'
class ReadActIve():

    def __init__(self,question,answer,points):
        self.question=question
        self.answer=answer
        self.points=points

    def create(level):

        book=input('what book or tv show do you want to read about >>> ')
        genre=input('what genre do you want to read >>> ')

        model_engine = "text-davinci-003"
       if level=='easy':
            prompt = "write a "+genre+" story for a baby year old about "+book+" with 5 multiple choice questions with answers at the end"
        elif level=='medium':
            prompt = "write a "+genre+" story for a 6 year old about "+book+" with 5 multiple choice questions with answers at the end"
        else:
            prompt = "write a "+genre+" story for a 9 year old about "+book+" with complex vocab and 5 multiple choice questions with answers at the end"

        print(prompt)

        completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

        response = completion.choices[0].text
        print(response)

        story=''

        n = 0

        answerFlag = False

        words=[]
        answer=[]

        temp=''
        remove=False

        a=2
        b=0

        for i in range(len(response)):
            dollar=False

            if remove==False:

                if response[i]!=' ' and response[i]!='\n':
                    temp+=response[i]
                else:
                    #words.append(' ')
                    if response[i]=='\n':
                        dollar=True
                    if temp !='Answer:':
                        words.append(temp)
                        if dollar:
                            words.append('$')
                    else:
                        remove=True
                    temp=''

            else:
                b+=1
                try:
                    if int(response[i])==a:
                        b=0
                        a+=1
                        remove=False
                        words.append(response[i])
                        
                except:
                    if b==1:
                        answer.append(response[i])
                        
                    
##                if int(response[i]).isnumber():
##                    remove=False

        #print(str(words))

        temp1=''

        for i in range (len(words)):
            if words[i]=='$':
                print(temp1)
                temp1=''
                #print('')
            else:
                temp1+=words[i]+' '


##        words1=[]
##
##        for i  in range (len(words)):
##            if words[i]!='Answers:':
##                words1.append(words[i])
                
            

        question=['what is your answer to question 1 >>> ','what is your answer to question 2 >>> ','what is your answer to question 3 >>> ','what is your answer to question 4 >>> ','what is your answer to question 5 >>> ']
        points=0

        ReadActIve.test(ReadActIve(question,answer,points))#,0))

    def test(self):
        second=time.time()
        moveOn=input(''''
press enter when you have finished reading''')
        print('''
you took''',round((time.time()-second),2),'seconds')
        for i in range(len(self.question)):
            print(self.question[i])
            count=0
            ans=''
            while count<2 and ans!=self.answer[i]:
                ans=input('what is the answer >>> ')
                count+=1

                if ans!=self.answer[i] and count<2:
                    print('try again')

            if ans==self.answer[i]:
                print('well done')
                if count==1:
                    self.points+=2
                elif count==2:
                    self.points+=1
            else:
                print('the correct answer was',self.answer[i])

        print( self.points)
        ReadActIve.nextLevel(self)

    def nextLevel(self):
        play='a'
        while play!='1' and play!='':
            play=input('press 1 for another go or enter to exit >>> ')

        if play=='1':
            print('you got',self.points,'points!')
            if self.points>8:
                print('you have moved to level: HARD')
                ReadActIve.create('hard')
            elif self.points<5:
                print('you have moved to level: EASY')
                ReadActIve.create('easy')
            else:
                print('you have moved to level: MEDIUM')
                ReadActIve.create('medium')
        
        
        

ReadActIve.create('medium')


