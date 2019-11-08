class Solution():   
    new=[]
    def merge_sort(self,a):
        if len(a)>1: 
            l=a[:len(a)//2]
            r=a[len(a)//2:]
            self.merge(l,r)
            self.merge_sort(l),self.merge_sort(r) 
            return l,r

    def merge(self,l,r):
        p,q=0,0
        self.new=[]
        while p<len(r) and q<len(l):
            if r[p]<l[q]:
                self.new.append(r[p])
                p+=1
            elif r[p]>l[q]:
                self.new.append(l[q])
                q+=1
            if p==len(r):
                self.new.append(l[q])
            elif q==len(l):
                self.new.append(r[p])
                #print(self.new)                  
            return self.new
