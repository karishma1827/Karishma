# f=open("test.txt")
# print(f.read())
# f.close()

# with open("test.txt","r") as f:
#     print(f.read())
    
# with open("test.txt","w") as f:
#     f.write("I love watching cricket")
    
# with open("hello.txt","r") as f:
#     f.read()
    
# with open("hello.txt","w") as f:
#     f.write("HELLO!")
    
# with open("hello.txt","a") as f:
# #     f.write("\nWELCOME")

# with open("test.txt") as f:
#     for l in f.readlines():
#         print("username:",l[0:6])
#         print("password:",l[6:])
    
##########################
#readline

# f=open(r"hello.txt")

import json

# with open ("myjson.json") as f:
#     data=json.load(f)
# print(data)
    
# for i in data["emp_details"]:
#     print (i["emp_name"])
    
# data["emp_details"].remove(data["emp_details"][1])
# # data["emp_details"][1]["emp_name"]=""
# print(data)
# with open("myjson.json","w") as outfile:
#    json.dump(data,outfile,indent=3)
   
   
def write_json(new_data,filename='myjson.json'):
    with open(filename,'r') as file:
        file_data=json.load(file)
    with open(filename,"w") as file:
        file_data["emp_details"].append(new_data)
        json.dump(file_data,file,indent=3)
        
y={"emp_name":"Abar",
   "emp_add":"Chennai",
   "emp_age":"19"
   }
write_json(y)
    
