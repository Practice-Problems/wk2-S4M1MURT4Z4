import math

def squares(a, b):
    if (math.sqrt(a) == int(math.sqrt(a))):return len( range( int(math.sqrt(a)), int(math.sqrt(b)) ) ) + 1    
    return len( range( int(math.sqrt(a)), int(math.sqrt(b)) ) )
