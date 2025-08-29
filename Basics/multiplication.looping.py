def mul(n,l): 
    for i in range(1,l+1):
        print(n,"*",i,"=",n*i)
        
n=input("enter a number")
if n.isdigit():
    k=int(n)
    limit=int(input("enter a limit"))
    mul(k,limit)
else:
    s=n[1:]
    if s.isdigit():
        limit=int(input("enter a limit"))
        mul(int(s),limit)
    else:
        print("invalid input")
  