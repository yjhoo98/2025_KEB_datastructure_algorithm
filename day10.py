def insertion_sort(l):
    for i in range(1,len(l)):
        value=l[i]
        while i>0 and l[i-1]>value:
            l[i]=l[i-1]
            i=i-1

        l[i]=value
    return l
def bubble_sort(a_list):
    list_length=len(a_list)-1
    for i in range(list_length):
        no_swap=True
        for j in range(list_length-i):

            if a_list[j]>a_list[ j+1]:
                a_list[j],a_list[j+1]=a_list[j+1],a_list[j]
                no_swap=False
        if no_swap:
            return a_list
    return a_list
print(bubble_sort([8,-11,9,1]))
print(insertion_sort([8,-11,9,1]))