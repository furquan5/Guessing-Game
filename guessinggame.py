import random
jackpot=random.randint(1,100)


guess=int(input('chal guess kar'))
counter=1
while guess!=jackpot:
    counter+=1
    
    if guess>jackpot:
        print('guess lower value')
        guess=int(input('chal guess kar'))
    else:
        print('guess higher value')
        guess=int(input('chal guess kar'))
    
print('Yayy. tum jeet gaye',counter)
