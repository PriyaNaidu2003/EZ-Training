def encode(num):
    rev = 0
    while num > 0:
        rem = num % 10
        rem1 = rem * rem
        digit = 0
        while rem1 > 0:
            digit += 1
            rem1 = rem1 // 10
        rev = rev * 10 ** digit + rem * rem
        num = num // 10
    print(rev)
num=int(input())
rev=0
temp=0
while num>0:
    rem=num%10
    rev=rev*10+rem
    num=num//10
encode(rev)

#167
#output:13649
