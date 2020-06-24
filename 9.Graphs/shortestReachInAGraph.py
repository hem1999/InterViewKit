
def neighbours(i,matrix):
    neigh = []
    for n in range(len(matrix[i])):
        if matrix[i][n]:
            neigh.append(n)
    return neigh
def find_all_distances(s,matrix):
    visited = [s]
    distances=[0 for i in range(len(matrix))]
    queue  = []
    queue.append(s)
    cur_distance = 6
    while(len(queue)>0):
        # print('##########')
        # print("Cur_dista",distances)
        # print("Queue:",queue)
        # print("visited: ",visited)
        # print("##################")
        k = queue.pop(0)
        updist = 0
        for i in neighbours(k,matrix):
            if i not in visited:
                visited.append(i)
                queue.append(i)
                distances[i] = distances[k]+6

    # print("visited: ",visited)

    for i in range(len(distances)-1):
        if i!=s:
            if distances[i]==0:
                print(-1,end=" ")
            else:
                print(distances[i],end=" ")
    if s!=n-1:
        if distances[-1]==0:
            print(-1)
        else:
            print(distances[-1])

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = [[False for i in range(n)] for i in range(n)]
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph[x-1][y-1]=True
        graph[y-1][x-1]=True
    # print(graph)
    # print("Graph: ")
    # for n in graph:
    #     print(n)
    s = int(input())
    find_all_distances(s-1,graph)
    #Worst Case: O(n^3)
