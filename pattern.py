1# n=int(input("Enter no. of rows:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()    
    
2# n=int(input("Enter no. of rows:"))

# for i in range(n,0,-1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()    

8# n=int(input("Enter no. of rows:"))
# for i in range(1,n+1):
#     if i==n:
#         continue
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()    
    

# for i in range(n,0,-1):
#     for j in range(0,i):
#         print("*", end=" ")
#     print()    
    
3# n=int(input("Enter number of rows:"))
# for i in range(n):
#     for j in range(n-1-i):
#         print(" ",end=" ")
#     for i in range(i+1):
#         print("*",end=" ")
#     print()    

#4# n=int(input("Enter number of rows:"))
# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for i in range(n-i):
#         print("*",end=" ")
#     print()    

n=int(input("Enter number of rows:"))
for i in range(n-2):
    for j in range(n-i-3):
        print(" ",end=" ")
    for i in range(n-i-4):
        print("*",end=" ")    
    print()    
    
    

    

