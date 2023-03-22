## Propsed Code
```python
def a_pow_mod(a,k,n):
    return (k*a)%n

def m_pow_mod(a,k,n):
    return (a**k)%n

def gen(a,op,n):
    return {op(a,k,n) for k in range(n)}

def is_cyclic(G,op,n):
    subg = {a:gen(a,op,n) for a in G}
    divisors = [a for a in range(1,len(G)+1) if n%a == 0]
    ordn = {i:[] for i in divisors}
    for a in G:
        ordn[len(subg[a])].append(a)
    if len(G) in ordn.keys():
        print("G is cyclic and generators are")
    else:
        print("G is not cyclic")
    print("Divisors are",divisors)
    print("Elements of order",ordn)

is_cyclic({0,1,2,3,4},a_pow_mod,5)
```

### Description
```python
def a_pow_mod(a,k,n):
    return (k*a)%n

def m_pow_mod(a,k,n):
    return (a**k)%n
```
Are for addition/multiplication modulo n to the power k.

```python
def gen(a,op,n):
    return {op(a,k,n) for k in range(n)}
```
Returns $\langle a\rangle = \\{a^k | 0\le k \le n\\}$

```python 
def is_cyclic(G,op,n):
    subg = {a:gen(a,op,n) for a in G}
    divisors = [a for a in range(1,len(G)+1) if n%a == 0]
    ordn = {i:[] for i in divisors}
    for a in G:
        ordn[len(subg[a])].append(a)
    if len(G) in ordn.keys():
        print("G is cyclic and generators are")
    else:
        print("G is not cyclic")
    print("Divisors are",divisors)
    print("Elements of order",ordn)
```
Lists the divisors and elements generating subgroup of each order.

## Usual Code
```python
def is_cyclic(G,op,n):
  generators=set()
  for i in G:
    if op=='+':
      gtd_i={(k*i)%n for k in range(1,len(G)+1)}
    else:
      gtd_i={(i**k)%n for k in range(1,len(G)+1)}
    if gtd_i==G:
      generators.add(i)
  if generators == set():
    print("The group", set(G) ,"is not cyclic.")
  else:
    print("The group", set(G), "is cyclic and the set of generators is",generators)
is_cyclic({0,1,2,3},'+',4)
```
