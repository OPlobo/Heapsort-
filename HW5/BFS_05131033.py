from collections import defaultdict 
  
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 


    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        #print(self.graph[u])

    def BFS(self, s):
        q2=[]
        if s:
            q2.append(s)
            #print(q2)
            a=self.graph[s]
            #print(a,q2)
            while a:
                b=a.pop(0)
                #print(a,b,q2)
                q2.append(b)
                #print(a,b,q2)
                p=self.graph[b]
                for i in range(0,len(p)):
                    x=g.graph[b][i]
                    if x not in q2:
                        if x not in a:
                            #print(x)
                            a.append(x)
                    #print(a,b,q2)
        return q2
        """
        :type s: int
        :rtype: list
        """
    def DFS(self, s):
        """
        :type s:int
        :rtype: list
        """
g=Graph()
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,2)
g.addEdge(1,5)
g.addEdge(2,4)
g.addEdge(2,6)
g.addEdge(3,5)
g.addEdge(4,1)
g.addEdge(4,5)
g.addEdge(5,0)
g.addEdge(6,4)
#print(g.graph[2])
print(g.BFS(2))
