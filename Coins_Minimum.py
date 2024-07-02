#greedy Approach
# coin=[1,5,7]
# bill_amount=18
# re={1:0,5:0,7:0}
# while bill_amount>0:
#     ma=coin.pop(coin.index(max(coin)))
#     c=bill_amount//ma
#     re[ma]+=c
#     bill_amount=bill_amount%ma
# print(re)

#DP_memoization
def calculate(coins,amt):

    res=[float('inf')]*(amt+1)
    res[0]=0

    for i in range(1,amt+1):
        for co in coins:
            if i-co>=0:
                res[i]=min(res[i],res[i-co]+1)
        print(res)
    print("\n")
    return res[amt] if res[amt]!=float('inf') else -1

coins=[1,5,7]
amt=18
print(calculate(coins,amt))