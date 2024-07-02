#Dynamic programming-memoization
import sys
def cost(curr, visited, graph, dp):
    n = len(graph)
    if len(visited) == n:
        return graph[curr][0]
    visit = tuple(visited)
    if (curr, visit) in dp:
        return dp[(curr, visit)]
    #m = float('inf')
    m=sys.maxsize
    for i in range(n):
        if i not in visited:
            new_visit = visited + [i]
            new_cost = graph[curr][i] + cost(i, new_visit, graph, dp)
            m = min(m, new_cost)
    dp[(curr, visit)] = m

    return m


g=[
    [0,4,7,5,5],
    [4,0,2,3,8],
    [7,2,0,3,4],
    [5,3,3,0,6],
    [5,8,4,6,0]
]

dp={}
print("Minimum cost:-",cost(0,[0],g,dp))
for i in dp:
    print(i)


#Dynamic Programming-Tabulation
