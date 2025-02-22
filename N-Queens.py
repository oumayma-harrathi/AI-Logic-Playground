def verif_but(etat, n):
    return len(etat) == n

def est_valide(etat, colonne, ligne):
    for i in range(len(etat)):
        if etat[i] == colonne or abs(etat[i] - colonne) == abs(i - ligne):
            return False
    return True

def succ(etat, n):
    ligne = len(etat)
    if ligne >= n:
        return []

    successeurs = []
    for colonne in range(n):
        if est_valide(etat, colonne, ligne):
            successeurs.append(etat + [colonne])

    return successeurs

def resolution(n):
    def recherche(etat):
        if verif_but(etat, n):
            return [etat]

        solutions = []
        for successeur in succ(etat, n):
            solutions += recherche(successeur)
        return solutions

    return recherche([])

n = 8
solutions = resolution(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
for solution in solutions:
    print(solution)