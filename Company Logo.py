from collections import Counter 

s = input()
count_S = Counter (s)
n = len(count_S)
mC_s = count_S.most_common()
for i in range(n):
    for j in range(i+1, n):
        if mC_s[i][1] == mC_s[j][1] and ord(mC_s[i][0]) > ord(mC_s[j][0]):
            c = mC_s[i]
            mC_s[i] = mC_s[j]
            mC_s[j] = c
                
                
                
for x,y in mC_s[:3] :
    print(x,y)
