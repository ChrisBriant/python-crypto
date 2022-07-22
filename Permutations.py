import cProfile

def faculty(n):
    if n<= 1:
        return n
    else:
        return faculty(n-1)*n

for i in range(10):
    print(faculty(i))

def counter(n):
    cnt = 0
    for i in range(n):
        cnt += 1
    return cnt

cProfile.run("counter(faculty(12))")