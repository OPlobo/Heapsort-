from collections import defaultdict

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)]
        self.g1=defaultdict(list)
        
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
    def cost(self,s,f):
        self.g1[s].append(f)
        return f

    #def getmin(self,x):
        
    
    def Dijkstra(self, s):
        a=[]
        b=[]
        m=[]
        a.extend(self.graph)
        b=self.cost(s,a[s])
        print(b)
        
        '''
        for i in b:
            if i!=0:
                m.append(i)
        n=min(m)
        print(n)
        '''
    def get(self,x):
        a=self.graph
        b=self.cost(x,a[x])
        x=[]
        for i in range(self.V):
            if b[i]!=0:
                x.append(i)
        return x
                
        #for i in range(0,len(a)):
            #print(i,self.cost(i,a[i]))
        """
        :type s: int
        :rtype: dict
        """
    
    '''
    def Dijkstra(self, s):
        a=[]
        a.extend(self.graph)
        self.graph_matrix[0]=a[s]
        for i in range(0,len(a)):
            if (a[s])[i]!=0:
                print(i)
                b=min((a[s])[i])
                print(b)
        print(self.graph_matrix)
    '''        
    def Kruskal(self):
        """
        :rtype: dict
        """
g=Graph(9)
g.graph=[[0,4,0,0,0,0,0,8,0],
         [4,0,8,0,0,0,0,11,0],
         [0,8,0,7,0,4,0,0,2],
         [0,0,7,0,9,14,0,0,0],
         [0,0,0,9,0,10,0,0,0],
         [0,0,4,14,10,0,2,0,0],
         [0,0,0,0,0,2,0,1,6],
         [8,11,0,0,0,0,1,0,7],
         [0,0,2,0,0,0,6,7,0]]
#print(g.graph)
print(g.get(0))
#print("Dijkstra",g.Dijkstra(0))
