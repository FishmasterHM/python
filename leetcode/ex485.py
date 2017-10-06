#Given a binary array, find the maximum number of consecutive 1s in this array.

a = [1,0,1,1,0,1]

def med1(a):
    indicis = [i for i,x in enumerate(a) if x == 0]
    max1 = indicis[0]
    print max1
    for i in range(len(indicis)-1):
        max1 = max(max1, indicis[i+1]-indicis[i])
    print max1

med1(a)
