from time import *
import random as r

def mistake(partest,usertest):
    error=0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error= error
        except :
            error = error+1

 
            return error
        def speed_time(time_s,time_e,userinput):
            time_delay = time_e - time_s
            time_R = round(time_delay,2)
            speed = len(userinput)/time_R
            return round(speed)
        

        



# We can print multiple strings

# We make a variable
test = [
    "A paragraph is defined as 'a group of sentences or a single sentence that forms a unit' (Lunsford and Connors 116).",
    "My name is Dinesh Bhatt",
    "I read in class 13"
]

test1 = r.choice(test)
print("Typing speed")
print(test1)
print()
print()
time_1 = time()
testinput=input("Enter: ")
time_2 = time()



