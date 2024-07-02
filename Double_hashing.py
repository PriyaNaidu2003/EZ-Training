
def isPrime(n):
    flag=0
    i=2
    if n<=1:
        return False
    else:
        while (i*i<n):
            if n%i==0:
                flag=1
            i+=1
        if(i*i>n):
            flag=0
    return flag
k=[20,34,45,70,56,81,104,37,46,39]

while True:
    prime_num=int(input("enter the prime number greater than 11"))
    if prime_num>=11:
        if isPrime(prime_num)==0 :
            num=int(input("enter a num less than prime number entered before "))
            max=0
            s=isPrime(num)
            sum=s+prime_num

            if isPrime(sum)==0:
                res = [False] * prime_num
                for i in k:
                    j = 0
                    h1_key = i % prime_num
                    h2_key = num - (i % num)
                    h = h1_key
                    while res[h] != False and j < prime_num:
                        h = (h1_key + h2_key * j) % prime_num
                        j += 1

                    res[h] = i

                print(res)
                break
            else:
                print("invalid number")




    else:
        print("enter a valid prime number")


# k=[20,34,45,70,56,81,104,37,46,39]
# res = [False] * 13
# for i in k:
#     j=0
#     h1_key=i%13
#     h2_key=10-(i%10)
#     h=h1_key
#     while res[h] != False and j<13:
#
#
#         h=(h1_key+h2_key*j)%11
#         j += 1
#
#     res[h]=i
#
# print(res)