# dealing with a graph as list of lists
graph = [[0,1,0,0,1,0],[1,0,1,0,1,0],[0,1,0,1,0,0],[0,0,1,0,1,1],[1,1,0,1,0,0],[0,0,0,1,0,0]]


#function determines the neighbors of a given vertex
def N(vertex):
    c = 0
    l = []
    for i in graph[vertex]:
        if i is 1 :
         l.append(c)
        c+=1
    return l

#the Bron-Kerbosch recursive algorithm
def bronk(r,p,x):
    if len(p) == 0 and len(x) == 0: # when no more possible neighbors are found, the max clique is printed
        print(r)
        return
    for vertex in p[:]: # iterates through all possible neigbors
        r_new = r[::]
        r_new.append(vertex)
        p_new = [val for val in p if val in N(vertex)] # p intersects N(vertex)
        x_new = [val for val in x if val in N(vertex)] # x intersects N(vertex)
        bronk(r_new,p_new,x_new) # recursiv call with new r, p and x
        p.remove(vertex)
        x.append(vertex)

bronk([], [0,1,2,3,4,5], [])