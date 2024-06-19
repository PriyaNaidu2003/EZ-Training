def count_vowels(stm):
    dic={'a':0,'e':0,'i':0,'o':0,'u':0}
    for i in stm:
        if i=='a'or i=='A':
            dic['a']+=1
        elif i=='e'or i=='E':
            dic['e']+=1
        elif i=='i'or i=='I':
            dic['i']+=1
        elif i=='o'or i=='O':
            dic['o']+=1
        elif i=='u'or i=='U':
            dic['u']+=1
    x=max(dic.values())
    result=[]
    for i,j in dic.items():
        if j==x:
            result.append(i)
    return result

i_p=[
    ["Alex","i enjoy hicking in the mountains"],
    ["Sam","A lovely sunny day at the beach"],
    ["Jamie","Reading a book is my favourite pass time"],
    ["Taylor","I love playing video games on week ends"],
    ["Chris","Exploring new cities is exiting and fun"]
    ]
o_p={}
for i in i_p:
    o_p[i[0]]=count_vowels(i[1])

print(o_p)
