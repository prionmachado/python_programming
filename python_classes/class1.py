#Find prime numbers be n1 and n2
class Prime:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    def cal_prime(self):
        print("Prime numbers between",self.n1,"and",self.n2,"are:")
        for i in range(self.n1,self.n2+1):
            if i > 1:
                p=0
                for j in range(2,i):
                    if i%j==0:
                        p=1
                        break
                if p==0:
                    print(i," ")

n1 = int(input('Enter lower limit: '))
n2 = int(input('Enter upper limit: '))
p = Prime(n1, n2)
p.cal_prime()
