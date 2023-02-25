def addmod(a,b,n):
    return (a+b)%n
def multmod(a,b,n):
    return (a*b)%n

from sympy import Matrix, pprint
def cayley(G,n,op):
    table = Matrix([[op(a,b,n) for a in G] for b in G])
    print("Cayley table for G is")
    pprint(table)
    print("The operation is", "" if table.is_symmetric() else "not","commutative")
    
cayley({0,1,2,3,4,5},6,addmod)