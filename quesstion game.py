print("question game")
question=["q1; what is the output of 10 % 3",
          "q2; which is the keyword is used to define a function in python",
          "q3; what does html stands for",
          "q4; which symbol used to comments in the python",
          "q5; what is the full form of cpu"]
answers=["1","def","hyper text markup language","#","central processing unit"]
points=0
user_answers=[]
a=0
for key in question:
    print(key)
    answer=input("enter the answer: ")
    user_answers.append(answer)
    
    if answer.lower()==answers[a]:
        points=points+5
        print("correct")
    else:
        points=points-5
        print("wrong")
    a=a+1
            
    

print()
print(f"your points was {points}")
            
    
