def afficher_combinaisons():
    combinaisons = []
    for i in range(10):
        for j in range(i, 10):
            for k in range(j, 10):
                if i != j and i != k and j != k:
                    combinaisons.append(str(i) + str(j) + str(k))
    
    print(", ".join(combinaisons))

afficher_combinaisons()

