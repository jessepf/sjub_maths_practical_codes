def addmod(a,b,n):
    return (a+b)%n
def multmod(a,b,n):
    return (a*b)%n

def subgroup(H,n,op):
    onestep = {op(a,b,n) for a in H for b in H if op(a,b,n) not in H}
    if onestep:
        print("H is not a subgroup of G. Elements missing are ",onestep)
    else:
        print("H is a subgroup of G")
        
subgroup({0,2,4},6,addmod)