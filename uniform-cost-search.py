
#Uniform Cost Search

graph = {'A': {'C': 5, 'D': 1, 'E': 2}, 'B': {'H': 4 ,'G': 3}, 'C': {'I': 2, 'D': 3, 'A': 5},
         'D': {'C': 3,  'H': 2}, 'E': {'A': 2, 'F': 3},
         'F': {'E': 3, 'G': 1}, 'G': {'F': 1, 'B': 3, 'H': 2}, 'H': {'I': 1, 'D': 2, 'B': 3, 'G': 2},
         'I': {'C': 2, 'H': 2}}


# TO CHECK IF THE KEY EXISTS IN THE LETTER'S DICTIONARY
pq=[]
que=[]
visited={}
ext=[]

   
def pque(q,listt):
    arr=[]
    arr.clear()
    for i in listt:
        arr.append(listt[i])
    arr.sort(reverse=True)
    
    for i in range(len(arr)):
        for j in listt:
            if(arr[i]==listt[j]):
                q.append(j)

# FOR THE MINIMUM KEY IN THE GRAPH WE USE AN ARRAY


def get_cost(letter,z,cost):
    
    for i in letter:
        if(i==z):
            return cost+letter[i]
            print(letter[i])

    return cost
def ucf(start,goal,graphlist):
    
    cost=0
    que.append(start)
    z=que.pop()
    o=z
    while z:
#         z=que.pop()
        print("The popped values are: ",z)
        print("The visited values are: ",visited)
        
        if(z==goal):
            print("Found Goal: ",z)
            cost=get_cost(graphlist[o],z,cost)
            return cost
            
        
        if z not in visited:

            cost=get_cost(graphlist[o],z,cost)   
            
            print("Exapnding ",z)
            pque(que,graphlist[z])
            visited[o]=cost
            o=z
            z=que.pop()
        print("The value of O: ",o)
#         print("The value of Z: ",z)

ucf('A','I',graph)
