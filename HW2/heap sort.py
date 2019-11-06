import math
arr=[1,2,3,4,5,6]
n=len(arr)
h=int(math.log(n+1,2))#算tree的level
def Maxheap(arr):
    for i in range(h+1):
        if (n-1)%2==0:#皆有兩個子結點
            for i in range(0,(n)//2):
                l=2*i+1
                r=2*i+2
                if arr[l]>=arr[r]:
                    if arr[l]>=arr[i]:
                        arr[l],arr[i]=arr[i],arr[l]
                    #elif arr[r]>=arr[i]:
                        #arr[r],arr[i]=arr[i],arr[r]
                elif arr[r]>=arr[l]:
                    if arr[r]>=arr[i]:
                        arr[r],arr[i]=arr[i],arr[r]
                    #elif arr[l]>=arr[i]:
                        #arr[l],arr[i]=arr[l],arr[r]
        elif (n-1)%2!=0:#存在一個子結點
            for i in range(0,(n-1)//2):
                l=2*i+1
                r=2*i+2
                if arr[l]>=arr[r]:
                    if arr[l]>=arr[i]:
                        arr[l],arr[i]=arr[i],arr[l]
                    #elif arr[r]>=arr[i]:
                        #arr[r],arr[i]=arr[i],arr[r]
                elif arr[r]>=arr[l]:
                    if arr[r]>=arr[i]:
                        arr[r],arr[i]=arr[i],arr[r]
                    #elif arr[l]>=arr[i]:
                        #arr[l],arr[i]=arr[l],arr[r]

                if arr[n-1]>=arr[(n-1)//2]:
                    arr[n-1],arr[(n-1)//2]=arr[(n-1)//2],arr[n-1]
    return arr
print(Maxheap(arr))

#def sort(arr):
    

