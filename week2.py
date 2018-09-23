import math

def squares(a, b):
    if (math.sqrt(a) == int(math.sqrt(a))):return len( range( int(math.sqrt(a)), int(math.sqrt(b)) ) ) + 1    
    return len( range( int(math.sqrt(a)), int(math.sqrt(b)) ) )

def encryption(s):
    s=s.replace(" ", "")
    low, high = int(math.sqrt(len(s))), math.ceil(math.sqrt(len(s)))
    if low*high < len(s):low = high = max(low,high)
    x=  [s[i: i+high] for i in range ( 0, math.ceil(len(s)), high)]
    lst=[]
    for j in range (high):
        stri=""
        for i in range(low):
            try:
                x[i][j]
            except:
                break
            stri+=x[i][j]
        lst.append(stri)
    return " ".join(lst)

