def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n

n = int(input("Enter number:"))
print(cal_sum(n)) 


