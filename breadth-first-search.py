#MY CODE FOR BREADTH FIRST SEARCH USING PYTHON


#CREATE A GRAPH
graph = {
    "A":["B","D"],
    "B":["A","C"],
    "C":["B"],
    "D":["A","E","F"],
    "E":["D","F","G"],
    "F":["D","E","H"],
    "G":["E","H"],
    "H":["G","F"]
}

#INITIALIZE LEVEL,AN ARRAY FOR VISITED NODES, AND A QUE LIST TO INSERT VALUES

level={}
visited = [] # List to keep track of visited nodes.
que=[]


#MAKE A FUNCTION
def bfs(visited, graph, node):
    
    #APPEND THE NODE IN VISITED
    visited.append(node)
    #APPEND THE NODE IN QUE LIST
    que.append(node)
    #VALUE OF THE LEVELS
    level[node]=0
    
    
    while que:

        #POP THE VALUE AND INSERT IT IN S
        s = que.pop(0) 
        print ("Popped ",s, end = " \n") 
        
        for i in graph[s]:
            if i not in visited:
                
                visited.append(i)
                print( "Visited: ",visited, "\n" )
                que.append(i)
                print( "QUEUEING: ",que, "\n" )
                level[i]=level[s]+1
                print("Level: ", level[i]," where s is: ",i)
#             else:
#                 print("Letter: ",s," alrady visited")


bfs(visited, graph, 'A')
print(level)
