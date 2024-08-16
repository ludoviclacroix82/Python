tableau = [12, 11, 13, 5, 6]

n = len(tableau)
for i in range(n):
    for j in range(0, n-1):
        print("range {}".format(n-i-1))
        print("hors if {} > {}".format(tableau[j],tableau[j+1]))
        if tableau[j] > tableau[j+1]:
            tableau[j], tableau[j+1] = tableau[j+1], tableau[j]
            
        print(tableau)
