print("Welcome to the translator!")
inp=input("Enter the input:")
op=" "
for i in inp:
    
   if i in ["a","e","i","o","u"]:
       op=op+"t"
       
   elif i in ["A","E","I","O","U"]:
        op=op+"T"
        
   else:
       op=op+i
       

print(op)
