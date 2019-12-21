from collections import defaultdict 
  
class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 


    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s):
        q2=[]
        if s in self.graph:
            q2.append(s)
            a=self.graph[s]                        
            while a:
                b=a.pop(0)                        
                q2.append(b)
                p=self.graph[b]
                for i in range(0,len(p)):   #走訪下一個連結
                    x=g.graph[b][i]
                    if x not in q2:         #如果不在q2
                        if x not in a:      #如果不在a
                            a.append(x)     #則加入
        return q2

    def DFS(self, s):
        q2=[]
        if s in self.graph:
            q2.append(s)
            a=self.graph[s]
            while a:
                b=a.pop(-1)
                q2.append(b)
                p=self.graph[b]
                for i in range(0,len(p)):
                    x=g.graph[b][i]
                    if x not in q2:
                        if x not in a:
                            a.append(x)
        return q2
        """
        :type s:int
        :rtype: list
        """
#參考資料:老師課堂投影片
