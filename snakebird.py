def snake_bird(n,k):
    fruits=list(map(int, input().split()))
    fruits.sort()
    for i in range(len(fruits)):
        if k>=fruits[i]:
            k+=1
        else:
            break
    return k

n,k=map(int,input().split())
print(snake_bird(n,k))