countries = ['A','B','C','D']
adj = {
    'A':['B','C'],
    'B':['A','C','D'],
    'C':['A','B','D'],
    'D':['B','C']
}

colors = ['Red','Green','Blue']
res = {}

def solve(i=0):
    if i == len(countries):
        return True

    c = countries[i]

    for col in colors:
        if all(res.get(n) != col for n in adj[c]):
            res[c] = col

            if solve(i+1):
                return True

            del res[c]

    return False

solve()

for k,v in res.items():
    print(k, "=", v)


#######                OUTPUT                #########

A = Red
B = Green
C = Blue
D = Red
