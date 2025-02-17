#)guess number 예제 자동화,로그파일(guess.txt)
import random

def guess_num(low,high,answer,chance)->int:
    mid=(low+high)//2
    print(f'guess numberis {mid}')
    fp.write(f'guess numberis {mid}')
    while chance != 0:

        if mid == answer:
            # print(f'You win. Answer is {answer}')
            with open('guess.txt', 'w') as fp:
                fp.write(f'You win. Answer is {answer}(chance:{chance})')
            break
        elif mid > answer:
            chance = chance - 1
            print(f'{mid} is bigger. Chance left : {chance}')
            fp.write(f'{mid} is bigger. Chance left : {chance}')
            return guess_num(low,mid-1,answer,chance)
        else:
            chance = chance - 1
            print(f'{mid} is lower. Chance left : {chance}')
            fp.write(f'{mid} is lower. Chance left : {chance}')
            return guess_num(mid+1,high,answer,chance)
    else:
        print(f'You lost. Answer is {answer}')
        fp.write(f'You lost. Answer is {answer}')
if __name__=="__main__":
    low=1
    high=100
    ans=random.randint(1,100)
    chance=7
    with open('guess.txt', 'w') as fp:
        guess_num(low, high, ans, chance)
