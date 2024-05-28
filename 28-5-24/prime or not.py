num=int(input())
#1
count=0
for deno in range (1,num):
    if num% deno ==0:
        count+=1
if count == 2:
    print("Prime")
else:
    print("Not a Prime")

#2 O(1) O(n)
for deno in range(2,num):
   if num % deno == 0:
       print("Not a Prime")
       break
else:
    print("Prime")
#3 reducing the iterations O(n/2)
for deno in range(2,(num//2)+1):
   if num % deno == 0:
       print("Not a Prime")
       break
else:
    print("Prime")
 
#4 O(sqrt(n)) efficient code
for deno in range(2,int(num**0.5)+1):
   if num % deno == 0:
       print("Not a Prime")
       break
else:
    print("Prime")
