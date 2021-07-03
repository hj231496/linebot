import random
def getans():  
   num=[0,1,2,3,4,5,6,7,8,9]
   random.shuffle(num)
   num=num[0:4]
   num = list(map(str, num))
   f = open('ans.txt', 'w')
   f.write( ''.join(num))
def gaming(guess_num):
    f = open('ans.txt', 'r')
    ans=f.read()
    ans = list(ans)
    guess_num=list(guess_num)
    a=b=0
    for i in range(4):
        if guess_num[i] in ans:
            if ans.index(guess_num[i])==i:a+=1
            else:b+=1
        if a==4:
            getans()
            return '恭喜你答對了！！'
    return '{}A{}B，請繼續唷!'.format(a,b)

if __name__=='__main__':
    #getans()
    print(gaming('4021'))
