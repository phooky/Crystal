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

def make_order_map(n):
    "Create a decent non-sequential permutation"
    # first create an ordering over the full bit width
    bits = int(ceil(log(n,2)))
    max_i = 1<<bits
    map = [-1]*max_i
    for i in range(n):
        br = bit_reverse(i, bits)
        map[bit_reverse(i,bits)] = i
    return filter(lambda x:x>=0, map)

def make_depths(X,Y,dn,df):
    dd = float(df-dn)
    t = float(X*Y)
    points = []
    mx = make_order_map(X)
    my = make_order_map(Y)
    for x in range(X):
        for y in range(Y):
            order = mx[(x+my[my[y]])%X]*Y+my[my[y]]
            d = ((order/t)*dd)+dn
            points.append((x,y,d))
    return points


if __name__ == '__main__':
    X,Y = 1024, 600
    ds = make_depths(X,Y,0,256)
    for i in range(0,256,32):
        im = Image.new("L",(X,Y),'black')
        pix = im.load()
        l,h = i,i+32
        for (x,y,d) in ds:
            if d < h and d >= l:
                pix[x,y] = 256
        im.show()


    
