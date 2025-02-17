memo=dict()
def fibonacci_memo(n)->int:
    if n in memo:
        return memo[n]
    elif n<=1:
        return n
    else:
        memo[n]=fibonacci_memo(n-2)+fibonacci_memo(n-1)
        return memo[n]
def fibonacci_recursion(n):
    """
    fibonacci sequence using recurion
    :param n:integer
    :return:fibonacci sequence
    """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci_recursion(n-1)+fibonacci_recursion(n-2)
def fibonacci_repetition(n)->int:
    n_list=[0,1]
    for i in range(n+1):
        n_list.append(n_list[i]+n_list[i+1])
    return n_list[n]
num=int(input("number:"))
print(fibonacci_repetition(num))
print(fibonacci_recursion(num))
n=int(input())
print(fibonacci_memo(n))
