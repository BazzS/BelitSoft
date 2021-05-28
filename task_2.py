list = [1,2,5,3,6,7,4,5,2]

def first_repeat(a):
    b = []
    for i in a:
        if i not in b:
            b.append(i)
        else:
            return i

print(first_repeat(list))
