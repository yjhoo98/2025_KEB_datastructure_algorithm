def is_even(n)->bool:
    """
    짝수 판정 함수
    :param n: integer
    :return: even->return True/odd-> return False
    """
    return not n&1
    # if n%2==0:
    #     return True
    # return False

# a=10
# b=11
# print(a&b)
# print(a|b)
# print(a^b)

def to_oct(n):
    if n==0:
        return ""
    else:
        return to_oct(n//8)+str(n%8)

n=int(input())
print(to_oct(n))
