from collections import defaultdict 
  
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 


    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s):
        q2=[]
        if s:
            q2.append(s)
            a=self.graph[s]
            while a:
                b=a.pop(0)
                q2.append(b)
                p=self.graph[b]
                for i in range(0,len(p)):
                    x=g.graph[b][i]
                    if x not in q2:
                        if x not in a:
                            a.append(x)
        return q2

    def DFS(self, s):
        """
        :type s:int
        :rtype: list
        """

