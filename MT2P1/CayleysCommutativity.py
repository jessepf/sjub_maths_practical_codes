def addmod(a,b,n):
    return (a+b)%n
def multmod(a,b,n):
    return (a*b)%n

def cayley(G,n,op):
    print("The Cayley's table for the group G =",G,"is")
    for i in G:
        for j in G:
            print(op(i,j,n),end="\t")
        print("\n")

def commutative(G,n,op):
    noncomm = [x for x in G for y in G if op(x,y,n)!=op(y,x,n)]
    if noncomm:
        print("The given operation is not commutative on the set",G)
        return
    print("The given operation is commutative on the set",G)
    
cayley({0,1,2,3,4,5},6,addmod)
commutative({0,1,2,3,4,5},6,addmod)