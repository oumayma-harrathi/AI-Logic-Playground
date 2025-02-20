etat_init=[4,5,2,3,1,6,7,0,8]
etat_but=[1,2,3,4,5,6,7,8,0]
def gene_succ(etat_init):
  pos=etat_init.index(0)
  x=pos//3
  y=pos%3

  mouv=[(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
  succ=[]
  for direction,(new_x,new_y) in mouv.items():
    if (0<new_x<3  & 0<new_y<3  ):
      new_pos=new_y*3+new_x
      new_etat=etat_init[:]
      new_etat[pos]=new_etat[new_pos]
      new_etat[new_pos]=new_etat[pos]
      succ.append(new_etat,direction)
  return succ 
def est_but(etat_courant):
    return etat_courant == etat_but




def recherche(etat_but,etat_init):
  chemin = []  
  pile = [(etat_init, chemin)]
  visit = set()
  visit=set()
  while pile :
    etat_courant,chemin=pile.pop()
    if est_but(etat_courant):
      return chemin+[etat_courant]
      visit.add(tuple(etat_courant))
      for succ in gene_succ(etat_courant):
        if (tuple(succ)not in visit):
          pile.append(succ,chemin+[etat_courant])
  return None 


etat_init = [4, 5, 2, 3, 1, 6, 7, 0, 8]
etat_but = [1, 2, 3, 4, 5, 6, 7, 8, 0]

chemin_solution = recherche(etat_but, etat_init)

if chemin_solution is not None:
  print("Solution trouvée :")
  for etat in chemin_solution:
    print(etat)
  else:
    print("Aucune solution trouvée.")