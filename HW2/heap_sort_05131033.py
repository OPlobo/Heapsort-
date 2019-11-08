import math
class Solution():    
    def Minheap(self,arr):
        n=len(arr)
        h=int(math.log(n+1,2))#算tree的level
        for i in range(h+1):
            if (len(arr)-1)%2==0:#皆有兩個子結點
                for i in range(0,len(arr)//2):
                    l=2*i+1
                    r=2*i+2
                    if arr[l]<=arr[r]:#比較子節點
                        if arr[l]<=arr[i]:
                            arr[l],arr[i]=arr[i],arr[l]
                    elif arr[r]<arr[l]:#比較子節點
                        if arr[r]<arr[i]:
                            arr[r],arr[i]=arr[i],arr[r]
            elif (len(arr)-1)%2!=0:#存在一個子結點
                if arr[len(arr)-1]<=arr[(len(arr)-1)//2]:
                    arr[-1],arr[(len(arr)-1)//2]=arr[(len(arr)-1)//2],arr[-1]
                for i in range(0,(len(arr)-1)//2):
                    l=2*i+1
                    r=2*i+2
                    if arr[l]<=arr[r]:#比較子節點
                        if arr[l]<=arr[i]:
                            arr[l],arr[i]=arr[i],arr[l]
                    elif arr[r]<arr[l]:#比較子節點
                        if arr[r]<arr[i]:
                            arr[r],arr[i]=arr[i],arr[r]           
        return arr
    def heap_sort(self,arr):
        heapsort=[]
        if len(arr)==0:
            return []
        else:
            for i in range(len(arr)-1):
                self.Minheap(arr)
                arr[-1],arr[0]=arr[0],arr[-1]        
                a1=arr.pop(-1)
                heapsort.append(a1)        
            heapsort.append(arr[-1])
        return heapsort

