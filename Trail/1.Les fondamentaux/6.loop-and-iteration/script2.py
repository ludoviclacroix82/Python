tableau = [12, 11, 13, 5, 6,3,20,18,39,1,2,9,8]

print(tableau)

tabLen = len(tableau)
for i in range(tabLen):
    for j in range(0, tabLen-1):
        if tableau[j] > tableau[j+1]:
            tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
            
print(tableau)