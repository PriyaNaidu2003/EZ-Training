
#dijkstra-Greedy approach

graph = [
    [0, 4, -1, -1, -1, -1, -1, 8, -1],  # 0
    [4, 0, 8, -1, -1, -1, -1, 11, -1],  # 1
    [-1, 8, 0, 7, -1, 4, -1, -1, 2],    # 2
    [-1, -1, 7, 0, 9, 14, -1, -1, -1],  # 3
    [-1, -1, -1, 9, 0, 10, -1, -1, -1], # 4
    [-1, -1, 4, 14, 10, 0, 2, -1, -1],   # 5
    [-1, -1, -1, -1, -1, 2, 0, 1, 6],   # 6
    [8, 11, -1, -1, -1, -1, 1, 0, 7],   # 7
    [-1, -1, 2, -1, -1, 2, 6, 7, 0]   # 8
]
value={}
for i in range(len(graph)):
    value[i]=float('inf')
res=[float('inf')]*len(value)

start=0
value[start]=0
n=len(value)

while len(value)>0:
    min_key=min(value,key=value.get)
    min_value=value[min_key]

    value.pop(min_key)

    res[min_key]=min_value

    for i in range(n):
        if i in value.keys():

            if min_value+graph[min_key][i]<=value[i] and graph[min_key][i]>0:
                value[i]=min_value+graph[min_key][i]
print(res)