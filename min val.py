a=int(input())
sum=0
l=[]
for i in range(1,a+1):
  n=int(input())
  l.append(n)
print (l) 
min=l[0]
for i in l:
  if i<min:
    min=i
print(min)
