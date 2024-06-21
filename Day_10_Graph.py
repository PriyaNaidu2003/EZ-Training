def dfs_graph(dict,visited_dic,s,ele):
    if visited_dic[ele]=="F":
        s.append(ele)
        visited_dic[ele]="T"

    else:
        return
    for i in dict[ele]:
        dfs_graph(dict,visited_dic,s,i[1])
    print(s.pop())

def bfs_graph(graph, e):
    Q=[e]
    v={}
    for i in graph.keys():
        v[i]=False
    v[e]=True
    while len(Q)!=0:
        curr=Q.pop(0)
        print(curr)

        for i in graph[curr]:
            if v[i[1]]==False:
                Q.append(i[1])
                v[i[1]]=True

if __name__=="__main__":

    dict={1:[(1,2,0),(1,3,0)],
      2:[(2,1,0),(2,5,0)],
      3:[(3,1,0),(3,4,0),(3,6,0)],
      4:[(4,3,0)],
      5:[(5,2,0),(5,7,0),(5,10,0),(5,13,0)],
      6:[(6,3,0),(6,7,0)],
      7:[(7,5,0),(7,6,0),(7,8,0),(7,9,0)],
      8:[(8,7,0)],
      9:[(9,7,0),(9,12,0)],
      10:[(10,5,0),(10,11,0)],
      11:[(11,10,0)],
      12:[(12,9,0),(12,13,0)],
      13:[(13,5,0),(13,12,0)]}
    visited_dic={1:"F",2:"F",3:"F",4:"F",5:"F",6:"F",7:"F",8:"F",9:"F",10:"F",11:"F",12:"F",13:"F"}
    s=[]
    print("DFS TRAVERSAL")
    for i in dict:
        dfs_graph(dict,visited_dic,s,i )
    print("BFS TRAVERSAL")
    bfs_graph(dict, 1)
