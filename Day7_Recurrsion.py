#Fibonacci

# def fibo(n):
#     if n==1:
#         return 0
#     if n==2:
#         return 1
#     return fibo(n-1)+fibo(n-2)
#
# if __name__=="__main__":
#     n=int(input())
#     print(fibo(n))

#Factorial

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
if __name__=="__main__":
    n=int(input())
    print(fact(n))
# power
def pow(n,m):
    if m==0:
        return 1
    return n*pow(n,m-1)
res=pow(3,3)
print(res)
