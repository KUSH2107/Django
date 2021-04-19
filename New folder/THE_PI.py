PT = input("Enter PT:")
K = input("Enter K:")
newK = []
P = []

if (len(K)<len(PT)):
    for i in range(len(PT)):
        newK.append(K[i%len(K)])
elif(len(K)>len(PT)):
    for i in range(len(PT)):
        newK.append(K[i%len(K)])
else:
    for i in range(len(PT)):
        newK.append(K[i%len(K)])

for i in range(len(PT)):
    P.append(PT[i])

P1 = [ord(character) for character in P]     
newK1 = [ord(character) for character in newK]

Sum = [] 
for i in range(0, len(P1)): 
    Sum.append(P1[i] + newK1[i])

CT = ''.join(map(chr, Sum))
print ("Resultant string", str(CT)) 

