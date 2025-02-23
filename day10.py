import sys
if __name__=="__main__":
    list1=[]
    n,k=map(int,sys.stdin.readline().split())
    for i in range(1,n+1):
        list1.append(i)
    pindex=k-1
    list2 = list1.copy()
    result=[]
    while len(list1)>1:
        if pindex>len(list2):
            list2=list2+list1
        try:
            result.append(list2[pindex])
        except IndexError:
            list2=list2+list1
            result.append(list2[pindex])
        list1.remove(list2[pindex])
        list2.pop(pindex)

        pindex+=(k-1)
    result=result+list1
    del list2
    print(f'<',end='')
    for i in range(0,len(result)-1):
        print(f'{result[i]},',end='')
    print(f'{result[len(result)-1]}>')