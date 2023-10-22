#import module
import time 

#taking input from user
seconds= input("enter time in seconds : ")

#creating function
def countDownTimer(seconds):
    while seconds > 0:
        min= int(seconds / 60)
        sec= int(seconds % 60)

        timer=f'{min}:{sec}'
        print(timer)

        seconds-=1
    print("times up")    

#calling function
countDownTimer(int(seconds))    