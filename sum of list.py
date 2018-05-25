a=int(input())
sum=0
l=[]
for i in range(1,a+1):
  n=int(input())
  l.append(n)
print (l) 
for j in l:
  sum=sum+j
  j=j+1
print (sum)
