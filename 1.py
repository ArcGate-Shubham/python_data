# num = int(input())
# rev =0
# temp = num
# while(num!=0):
#     rem = num%10
#     rev = rev*10 + rem
#     num = num//10
# if(rev==temp):
#     print("plaindrome")
# else:
#     print("not")
num = input()
i,j = 0,len(num)-1
flag = True
while(i<=j):
    if(num[i]!=num[j]):
        print("not")
        flag = False
        break
    else:
        i+=1
        j-=1
if(flag):
    print("palindrome")