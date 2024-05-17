from mcq import Mcq
import json

with open ("quest.json") as f:
    data= json.load(f)
    
test=[]

for q in data ["ques"]:
    test.append(Mcq(q["prompt"],q["ans"]))
    
score=0

for ques in test:
    print(ques.prompt)
    ans=input("Enter your option[a,b,c]:")
    if ans==ques.ans:
        score+=1
        
print(test)

print(f"You score {score}/{len(test)}")
        
    