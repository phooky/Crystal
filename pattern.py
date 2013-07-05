# Generating the Z-height for each x,y in the pattern:
# - find an ordering for all coordinates
# - distribute over the Z range
from math import ceil, log
from PIL import Image

def bit_reverse(n,bits):
    "Reverse the bits in the given number"
    out = 0
    for i in range(bits):
        out <<= 1
        if (n & 1):
            out |= 1
        n >>= 1
    return out

def makeOrderMap(n):
    "Create a decent non-sequential permutation"
    # first create an ordering over the full bit width
    bits = int(ceil(log(n,2)))
    max_i = 1<<bits
    map = [-1]*max_i
    for i in range(n):
        br = bit_reverse(i, bits)
        map[bit_reverse(i,bits)] = i
    return filter(lambda x:x>=0, map)

def makeDepths(X,Y,dn,df):
    dd = float(df-dn)
    t = float(X*Y)
    points = []
    mx = makeOrderMap(X)
    my = makeOrderMap(Y)
    for x in range(X):
        for y in range(Y):
            order = mx[(x+my[my[y]])%X]*Y+my[y]
            d = ((order/t)*dd)+dn
            points.append((x,y,d))
    return points

def render(path,X,Y):
    im = Image.new("L",(X,Y),'white')
    pix = im.load()
    ds = makeDepths(X,Y,0,256)
    for (x,y,d) in ds:
        pix[x,y] = int(d)
    im.save(path)

render('foo.png',1024,600)


    
