def hazpana(n,chofen1,list,list1,k):
   for x in range(0,int(n)):
       if chofen1[x].isspace() == True:
           list1.append(' ')
       else:
           number1= list.index(chofen1[x])
           if number1+k> 25:
               nu= number1+k
               nu1 = nu-26
               list1.append(list[int(nu1)])
           else:
               list1.append(list[number1+k])


def pianuch(n1,chofen,list1,list,k,):
     for x in range(0,int(n1)):
         if chofen[x].isspace() == True:
             list1.append(' ')
         elif k <0 and chofen[x].isspace() == False:
             i =k*-1
             number2 = list.index(chofen[x])
             if number2+i > 25:
                 nu = number2 + i
                 nu1= nu -26
                 list1.append(list[nu1])
             else:
                list1.append(list[number2+i])
         else:
            number= list.index(chofen[x])
            list1.append(list[number-k])













a= 1
list1=[]
while 1==1:
    c= str(input('1= הצפנה 2=פענוח'))
    if c =='1' or c=='2':
        break
while int(c) == 2:
    chofen = str(input('please put the letter'))
    n1 =len(chofen)
    break
while int(c)==1:
    chofen1 = str(input('please put the letter'))
    n = len(chofen1)
    break
def check_k(k,v):
    for x in range(0,len(k)):
        if k[x] <= '9' and k[x] >= '0' or k[x]=='-':
            v = v+1
        else:
            return False
    if v == len(k):
        return True
v=0
while 1==1:
    k1 = str(input('please put the key '))
    if check_k(k1,v) == True:
        break
k = int(k1)



list= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while int(c)==2:
    pianuch(n1,chofen,list1,list,k)
    break
while int(c)==1:
    hazpana(n,chofen1,list,list1,k)
    break
st=''
for x in list1:
    st= st+x
print(st)
