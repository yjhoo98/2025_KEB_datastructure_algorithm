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
n=int(input())
print(is_even(n))