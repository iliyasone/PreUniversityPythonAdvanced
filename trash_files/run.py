n = 2
a = [None] * n
L = 0


def add(x):
    global L, n, a
    if L == n:
        n  *= 2
        a_new = [None] * n
        
        for i in range(len(a)):
            a_new[i] = a[i] 
        a = a_new
    
    a[L] = x
    L+=1
    
def print_list():
    for i in range(L):
        print(a[i], end =' ')
    print()

add("X")
add("Y")
print_list()
print(a)
add("Z")          
print_list()
print(a)