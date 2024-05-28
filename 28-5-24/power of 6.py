num=int(input())
while num != 1:
    if num%6==0:
        num//=6
    else:
        print("False")
        break
else:
    print("True")
