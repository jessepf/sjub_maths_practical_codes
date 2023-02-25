import sympy as sp
def addmod(a,b,n):
    return (a+b)%n
def multmod(a,b,n):
    return (a*b)%n

def cayley(G,op,n):
    table = sp.Matrix([[op(a,b,n) for a in G] for b in G])
    return table
def closure(G,op,n):
    table = cayley(G,op,n)
    for i in table:
        if i not in G:
            print("Closure not satisfied")
            return False
    return True

def Associative(G,op,n):
    no_asso = [(a,b,c) for a in G for b in G for c in G if op(op(a,b,n),c,n)!= op(a,op(b,c,n),n)]
    if no_asso:
        print("Associativity axiom not satisfied.")
        return False
    return True

def identity(G,op,n):
    table = cayley(G,op,n)
    for i in range(len(G)):
        if list(table[i,:]) == G:
            return G[i]
    print("No identity found")
    return None

def has_inverses(G,op,n):
    table = cayley(G,op,n)
    iden = identity(G,op,n)
    if iden != None:
        for i in range(len(G)):
            if iden not in table[i,:]:
                print("No inverse for",G[i])
                return False
        return True
    return False

def commutativity(G,op,n):
    table = cayley(G,op,n)
    return True if table.is_symmetric() else False

def check_group(G,op,n):
    iden = None
    table = cayley(G,op,n)
    sp.pprint(table)
    if closure(G,op,n) and Associative(G,op,n):
        iden = identity(G,op,n)
        if iden != None and has_inverses(G,op,n):
            print("G is a group under the given operation with identity",iden)
    else:
        print("G is not a group under the given operation.")
        
check_group([0,1,2,3],addmod,4) #Input set as a list