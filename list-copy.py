#Python学习专用
#
#
#
#
l1 = [4,5,7,1,3,9,0]
l2 = l1

l2.sort()

for x in range(len(l1)):
    print(l1[x], l2[x])

print('-'*30)

l1 = [4,5,7,1,3,9,0]

l2 = l1.copy()

l1.sort()

l1.reverse()

for i in range(len(l1)):
    print(l1[i], l2[i])
